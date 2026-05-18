import httpx
import pytest
import respx

from pyunsdg import UNSDClient
from pyunsdg.client import BASE_URL, _release_sort_key
from pyunsdg.models import ApiGeoArea, ApiSerie, ApiTarget
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
def test_get_series_data_uses_live_derived_response_and_query_params():
    fixture = load_fixture("series_data_page_1.json")
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    data = UNSDClient().get_series_data(
        [SERIES_CODE],
        area_code=AREA_CODE,
        release_code="2026.Q1.G.01",
    )

    request = route.calls.last.request
    assert request.url.params["seriesCode"] == SERIES_CODE
    assert request.url.params["areaCode"] == AREA_CODE
    assert request.url.params["releaseCode"] == "2026.Q1.G.01"
    assert request.url.params["pageSize"] == "1000"
    assert request.url.params["page"] == "1"
    assert data == fixture["data"]
    assert data


@respx.mock
def test_get_series_data_sends_expanded_time_period_range():
    observations = [
        {"timePeriodStart": 2015.0, "value": "start"},
        {"timePeriodStart": 2016.0, "value": "inside"},
        {"timePeriodStart": 2017.0, "value": "end"},
    ]
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
    assert "timePeriodStart" not in request.url.params
    assert "timePeriodEnd" not in request.url.params
    assert request.url.params.get_list("timePeriod") == ["2015", "2016", "2017"]
    assert [item["value"] for item in data] == ["start", "inside", "end"]


@respx.mock
def test_get_series_data_paginates_until_partial_page():
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
