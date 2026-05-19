import json

import httpx
import pytest
import respx

from pyunsdg import UNSDClient, is_single_time_series
from pyunsdg.client import BASE_URL, _release_sort_key
from pyunsdg.models import ApiDimension, ApiGeoArea, ApiSerie, ApiTarget
from tests.helpers import AREA_CODE, SERIES_CODE, TARGET_CODE, load_fixture


pytestmark = pytest.mark.mock


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
        return_value=httpx.Response(
            200,
            json={"data": observations, "totalPages": 1},
        )
    )

    data = UNSDClient().get_series_data(
        [SERIES_CODE],
        area_code=AREA_CODE,
        start_period="2015",
        end_period="2017",
    )

    request = route.calls.last.request
    assert "timePeriod" not in request.url.params
    assert request.url.params["timePeriodStart"] == "2015"
    assert request.url.params["timePeriodEnd"] == "2017"
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
    assert not is_single_time_series(
        [base_record, {**base_record, "series": "OTHER_SERIES"}]
    )
