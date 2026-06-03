import json

import httpx
import pytest
import respx

from pyunsdg import UNSDClient, debug, is_single_time_series
from pyunsdg.client import BASE_URL, _release_sort_key
from pyunsdg.models import ApiDimension, ApiGeoArea, ApiSerie, ApiTarget
from tests.helpers import AREA_CODE, SERIES_CODE, TARGET_CODE, load_fixture

pytestmark = pytest.mark.mock


@pytest.fixture(autouse=True)
def disable_debug_output():
    debug.disable()
    yield
    debug.disable()


@respx.mock
def test_get_geo_areas_returns_live_derived_pydantic_models():
    fixture = load_fixture("geo_area_list.json")
    route = respx.get(f"{BASE_URL}/sdg/GeoArea/List").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    areas = UNSDClient().get_geo_areas()

    assert route.called
    assert areas == [ApiGeoArea(**item) for item in fixture]


@respx.mock
def test_debug_output_is_disabled_by_default(capsys):
    fixture = load_fixture("geo_area_list.json")
    respx.get(f"{BASE_URL}/sdg/GeoArea/List").mock(return_value=httpx.Response(200, json=fixture))

    UNSDClient().get_geo_areas()

    captured = capsys.readouterr()
    assert captured.err == ""


@respx.mock
def test_debug_output_prints_constructed_query(capsys):
    fixture = load_fixture("target_list_without_children.json")
    respx.get(f"{BASE_URL}/sdg/Target/List").mock(return_value=httpx.Response(200, json=fixture))

    debug.enable()
    UNSDClient().get_targets()

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == (f"pyunsdg query: {BASE_URL}/sdg/Target/List?includechildren=false\n")


@respx.mock
def test_get_targets_excludes_children_using_live_derived_data():
    fixture = load_fixture("target_list_without_children.json")
    route = respx.get(f"{BASE_URL}/sdg/Target/List").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    targets = UNSDClient().get_targets()

    request = route.calls.last.request
    assert request.url.params["includechildren"] == "false"
    assert targets == [ApiTarget(**item) for item in fixture]
    assert targets[0].code == TARGET_CODE


def _target_series_fixture(fixture):
    return [
        ApiSerie(**item)
        for target in fixture
        if target["code"] == TARGET_CODE
        for indicator in target["indicators"]
        for item in indicator["series"]
        if isinstance(item, dict)
    ]


def _latest_series_by_code(series_items):
    latest_by_code = {}
    for series in series_items:
        current = latest_by_code.get(series.code)
        if current is None or _release_sort_key(series.release) > _release_sort_key(
            current.release
        ):
            latest_by_code[series.code] = series
    return list(latest_by_code.values())


def _series_dimensions_fixture():
    return load_fixture("series_data_page_1.json")["dimensions"]


def _mock_series_dimensions(series_code=SERIES_CODE):
    return respx.get(f"{BASE_URL}/sdg/Series/{series_code}/Dimensions").mock(
        return_value=httpx.Response(200, json=_series_dimensions_fixture())
    )


def _mock_target_list_with_children():
    fixture = load_fixture("target_list_with_children.json")
    route = respx.get(f"{BASE_URL}/sdg/Target/List").mock(
        return_value=httpx.Response(200, json=fixture)
    )
    return fixture, route


def _unique_series_codes_for_target(fixture, target_code=TARGET_CODE):
    return {
        series["code"]
        for target in fixture
        if target["code"] == target_code
        for indicator in target["indicators"]
        for series in indicator["series"]
        if series.get("code")
    }


def _mock_dimensions_for_series_codes(series_codes):
    return {series_code: _mock_series_dimensions(series_code) for series_code in series_codes}


def _coarsest_dimension_payload():
    return [
        {"name": "Age", "values": ["ALLAGE"]},
        {"name": "Location", "values": ["ALLAREA"]},
        {"name": "Quantile", "values": ["_T"]},
        {"name": "Reporting Type", "values": ["G"]},
        {"name": "Sex", "values": ["BOTHSEX"]},
        {"name": "Type_of_household", "values": ["_T"]},
    ]


def test_release_sort_key_orders_structured_unsd_releases():
    assert _release_sort_key("2025.Q3.G.02") > _release_sort_key("2025.Q3.G.01")
    assert _release_sort_key("2025.Q4.G.01") > _release_sort_key("2025.Q3.G.99")
    assert _release_sort_key("2026.Q1.G.01") > _release_sort_key("2025.Q4.G.02")
    assert _release_sort_key("2025.Q3.G.02") > _release_sort_key(None)
    assert _release_sort_key("2025.Q3.G.02") > _release_sort_key("not-a-release")


@respx.mock
def test_get_series_codes_returns_latest_releases_by_default():
    fixture = load_fixture("target_list_with_children.json")
    route = respx.get(f"{BASE_URL}/sdg/Target/List").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    series = UNSDClient().get_series_codes(target_code=TARGET_CODE)
    all_releases = _target_series_fixture(fixture)

    request = route.calls.last.request
    assert request.url.params["includechildren"] == "true"
    assert series == _latest_series_by_code(all_releases)
    assert len(series) == len({item.code for item in all_releases})
    assert {item.code for item in series}
    assert SERIES_CODE in {item.code for item in series}


@respx.mock
def test_get_series_codes_can_return_all_releases():
    fixture = load_fixture("target_list_with_children.json")
    route = respx.get(f"{BASE_URL}/sdg/Target/List").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    series = UNSDClient().get_series_codes(target_code=TARGET_CODE, all_releases=True)

    request = route.calls.last.request
    assert request.url.params["includechildren"] == "true"
    assert series == _target_series_fixture(fixture)
    assert len(series) > len({item.code for item in series})


@respx.mock
def test_get_indicator_series_returns_grouped_metadata_and_dimensions():
    fixture, route = _mock_target_list_with_children()
    dimension_routes = _mock_dimensions_for_series_codes({"SH_ACS_UNHC", "SH_ACS_UNHC_25"})

    metadata = UNSDClient().get_indicator_series("3.8.1")

    request = route.calls.last.request
    assert request.url.params["includechildren"] == "true"
    assert metadata.code == "3.8.1"
    assert metadata.description == "Coverage of essential health services"
    assert metadata.tier == "1"
    assert metadata.uri == "/v1/sdg/Indicator/3.8.1"
    assert [series.code for series in metadata.series] == ["SH_ACS_UNHC", "SH_ACS_UNHC_25"]

    series_by_code = {series.code: series for series in metadata.series}
    assert series_by_code["SH_ACS_UNHC"].latest_release == "2025.Q3.G.02"
    assert series_by_code["SH_ACS_UNHC_25"].latest_release == "2026.Q1.G.01"
    assert series_by_code["SH_ACS_UNHC"].releases[0] == "2018.Q2.G.01"
    assert series_by_code["SH_ACS_UNHC"].releases[-1] == "2025.Q3.G.02"
    assert series_by_code["SH_ACS_UNHC"].dimensions == [
        ApiDimension(**item) for item in _series_dimensions_fixture()
    ]
    assert all(route.call_count == 1 for route in dimension_routes.values())

    target = next(target for target in fixture if target["code"] == TARGET_CODE)
    indicator = next(
        indicator for indicator in target["indicators"] if indicator["code"] == "3.8.1"
    )
    assert len(series_by_code["SH_ACS_UNHC"].releases) == len(
        {series["release"] for series in indicator["series"] if series["code"] == "SH_ACS_UNHC"}
    )


@respx.mock
def test_get_target_series_returns_nested_indicator_metadata():
    fixture, route = _mock_target_list_with_children()
    dimension_routes = _mock_dimensions_for_series_codes(_unique_series_codes_for_target(fixture))

    metadata = UNSDClient().get_target_series(TARGET_CODE)

    request = route.calls.last.request
    assert request.url.params["includechildren"] == "true"
    assert metadata.code == TARGET_CODE
    assert metadata.indicators
    assert "3.8.1" in {indicator.code for indicator in metadata.indicators}

    indicator_by_code = {indicator.code: indicator for indicator in metadata.indicators}
    indicator_381 = indicator_by_code["3.8.1"]
    assert [series.code for series in indicator_381.series] == ["SH_ACS_UNHC", "SH_ACS_UNHC_25"]
    assert indicator_381.series[0].dimensions == [
        ApiDimension(**item) for item in _series_dimensions_fixture()
    ]
    assert all(route.call_count == 1 for route in dimension_routes.values())


@respx.mock
def test_get_indicator_series_raises_for_unknown_indicator():
    _mock_target_list_with_children()

    with pytest.raises(ValueError, match="indicator code 'not-an-indicator' was not found"):
        UNSDClient().get_indicator_series("not-an-indicator")


@respx.mock
def test_get_target_series_raises_for_unknown_target():
    _mock_target_list_with_children()

    with pytest.raises(ValueError, match="target code 'not-a-target' was not found"):
        UNSDClient().get_target_series("not-a-target")


@respx.mock
def test_get_series_dimensions_returns_live_derived_pydantic_models():
    fixture = _series_dimensions_fixture()
    route = respx.get(f"{BASE_URL}/sdg/Series/{SERIES_CODE}/Dimensions").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    dimensions = UNSDClient().get_series_dimensions(SERIES_CODE)

    assert route.called
    assert dimensions == [ApiDimension(**item) for item in fixture]
    assert dimensions[0].id == "Age"
    assert dimensions[0].codes[0].code == "ALLAGE"
    assert dimensions[0].codes[0].description == "All age ranges or no breaks by age"
    assert dimensions[0].codes[0].sdmx == "_T"


@respx.mock
def test_get_series_data_uses_live_derived_response_and_query_params():
    fixture = load_fixture("series_data_page_1.json")
    dimensions_route = _mock_series_dimensions()
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    data = UNSDClient().get_series_data(
        [SERIES_CODE],
        area_code=AREA_CODE,
        release_code="2026.Q1.G.01",
    )

    request = route.calls.last.request
    assert dimensions_route.called
    assert request.url.params["seriesCode"] == SERIES_CODE
    assert request.url.params["areaCode"] == AREA_CODE
    assert request.url.params["releaseCode"] == "2026.Q1.G.01"
    assert json.loads(request.url.params["dimensions"]) == _coarsest_dimension_payload()
    assert request.url.params["pageSize"] == "1000"
    assert request.url.params["page"] == "1"
    assert data == fixture["data"]
    assert data


@respx.mock
def test_get_series_data_can_request_all_dimensions():
    fixture = load_fixture("series_data_page_1.json")
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    data = UNSDClient().get_series_data(
        [SERIES_CODE],
        area_code=AREA_CODE,
        dimensions="all",
    )

    request = route.calls.last.request
    assert "dimensions" not in request.url.params
    assert data == fixture["data"]


@respx.mock
def test_get_series_data_sends_custom_dimensions():
    fixture = load_fixture("series_data_page_1.json")
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    data = UNSDClient().get_series_data(
        [SERIES_CODE],
        area_code=AREA_CODE,
        dimensions={"Age": "ALLAGE", "Sex": ["BOTHSEX"]},
    )

    request = route.calls.last.request
    assert json.loads(request.url.params["dimensions"]) == [
        {"name": "Age", "values": ["ALLAGE"]},
        {"name": "Sex", "values": ["BOTHSEX"]},
    ]
    assert data == fixture["data"]


@respx.mock
def test_get_series_data_sends_time_period_range():
    _mock_series_dimensions()
    observations = load_fixture("series_data_page_1.json")["data"][:3]
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        side_effect=[
            httpx.Response(200, json={"data": [observation], "totalPages": 1})
            for observation in observations
        ]
    )

    data = UNSDClient().get_series_data(
        [SERIES_CODE],
        area_code=AREA_CODE,
        start_period="2015",
        end_period="2017",
    )

    assert route.call_count == 3
    for call, time_period in zip(route.calls, ["2015", "2016", "2017"], strict=True):
        request = call.request
        assert request.url.params.get_list("timePeriod") == [time_period]
        assert "timePeriodStart" not in request.url.params
        assert "timePeriodEnd" not in request.url.params
    assert data == observations


@respx.mock
def test_get_series_data_omits_time_period_params_by_default():
    _mock_series_dimensions()
    fixture = load_fixture("series_data_page_1.json")
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    UNSDClient().get_series_data([SERIES_CODE], area_code=AREA_CODE)

    request = route.calls.last.request
    assert "timePeriod" not in request.url.params
    assert "timePeriodStart" not in request.url.params
    assert "timePeriodEnd" not in request.url.params


@respx.mock
def test_get_series_data_returns_empty_for_inverted_time_period_range():
    dimensions_route = _mock_series_dimensions()
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        return_value=httpx.Response(200, json={"data": []})
    )

    data = UNSDClient().get_series_data(
        [SERIES_CODE],
        start_period="2017",
        end_period="2015",
    )

    assert data == []
    assert not dimensions_route.called
    assert not route.called


def test_get_series_data_requires_end_period_with_start_period():
    with pytest.raises(
        ValueError,
        match="start_period and end_period must be provided together",
    ):
        UNSDClient().get_series_data([SERIES_CODE], start_period="2015")


def test_get_series_data_requires_start_period_with_end_period():
    with pytest.raises(
        ValueError,
        match="start_period and end_period must be provided together",
    ):
        UNSDClient().get_series_data([SERIES_CODE], end_period="2017")


@respx.mock
def test_get_series_data_paginates_until_partial_page():
    _mock_series_dimensions()
    fixture = load_fixture("series_data_page_1.json")
    observation = fixture["data"][0]
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        side_effect=[
            httpx.Response(200, json={"data": [observation] * 1000}),
            httpx.Response(200, json={"data": [observation]}),
        ]
    )

    data = UNSDClient().get_series_data([SERIES_CODE], area_code=AREA_CODE)

    assert len(data) == 1001
    assert route.call_count == 2
    assert route.calls[0].request.url.params["page"] == "1"
    assert route.calls[1].request.url.params["page"] == "2"


@respx.mock
def test_debug_output_prints_each_paginated_series_data_query(capsys):
    fixture = load_fixture("series_data_page_1.json")
    observation = fixture["data"][0]
    respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        side_effect=[
            httpx.Response(200, json={"data": [observation] * 1000}),
            httpx.Response(200, json={"data": [observation]}),
        ]
    )

    debug.enable()
    UNSDClient().get_series_data([SERIES_CODE], area_code=AREA_CODE, dimensions="all")

    lines = capsys.readouterr().err.splitlines()
    assert len(lines) == 2
    assert all(line.startswith(f"pyunsdg query: {BASE_URL}/sdg/Series/Data?") for line in lines)
    assert "page=1" in lines[0]
    assert "page=2" in lines[1]


@respx.mock
def test_get_series_data_uses_total_pages_when_available():
    _mock_series_dimensions()
    fixture = load_fixture("series_data_page_1.json")
    observation = fixture["data"][0]
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        side_effect=[
            httpx.Response(
                200,
                json={"data": [observation] * 1000, "totalPages": 2},
            ),
            httpx.Response(
                200,
                json={"data": [observation] * 1000, "totalPages": 2},
            ),
        ]
    )

    data = UNSDClient().get_series_data([SERIES_CODE], area_code=AREA_CODE)

    assert len(data) == 2000
    assert route.call_count == 2
    assert route.calls[0].request.url.params["page"] == "1"
    assert route.calls[1].request.url.params["page"] == "2"


@respx.mock
def test_get_series_data_fetches_coarsest_dimensions_per_series():
    other_series_code = "OTHER_SERIES"
    observation = load_fixture("series_data_page_1.json")["data"][0]
    other_observation = {**observation, "series": other_series_code}
    _mock_series_dimensions(SERIES_CODE)
    _mock_series_dimensions(other_series_code)
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        side_effect=[
            httpx.Response(200, json={"data": [observation]}),
            httpx.Response(200, json={"data": [other_observation]}),
        ]
    )

    data = UNSDClient().get_series_data([SERIES_CODE, other_series_code])

    assert data == [observation, other_observation]
    assert route.call_count == 2
    assert route.calls[0].request.url.params["seriesCode"] == SERIES_CODE
    assert route.calls[1].request.url.params["seriesCode"] == other_series_code
    assert json.loads(route.calls[0].request.url.params["dimensions"]) == (
        _coarsest_dimension_payload()
    )
    assert json.loads(route.calls[1].request.url.params["dimensions"]) == (
        _coarsest_dimension_payload()
    )


def test_is_single_time_series_detects_one_series_across_years():
    observation = load_fixture("series_data_page_1.json")["data"][0]
    records = [
        observation,
        {**observation, "timePeriodStart": observation["timePeriodStart"] + 1},
    ]

    assert is_single_time_series(records)


def test_is_single_time_series_rejects_empty_or_mixed_data():
    fixture_records = load_fixture("series_data_page_1.json")["data"]
    base_record = fixture_records[0]

    assert not is_single_time_series([])
    assert not is_single_time_series([base_record, fixture_records[1]])
    assert not is_single_time_series([base_record, {**base_record, "geoAreaCode": "8"}])
    assert not is_single_time_series([base_record, {**base_record, "series": "OTHER_SERIES"}])
