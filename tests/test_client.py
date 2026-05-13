import httpx
import respx

from pyunsdg import UNSDClient
from pyunsdg.client import BASE_URL
from pyunsdg.models import ApiGeoArea, ApiSerie, ApiTarget
from tests.helpers import AREA_CODE, SERIES_CODE, TARGET_CODE, load_fixture


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


@respx.mock
def test_get_series_codes_filters_by_target_code_using_live_derived_data():
    fixture = load_fixture("target_list_with_children.json")
    route = respx.get(f"{BASE_URL}/sdg/Target/List").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    series = UNSDClient().get_series_codes(target_code=TARGET_CODE)

    request = route.calls.last.request
    assert request.url.params["includechildren"] == "true"
    assert series == [
        ApiSerie(**item)
        for indicator in fixture[0]["indicators"]
        for item in indicator["series"]
    ]
    assert {item.code for item in series}
    assert SERIES_CODE in {item.code for item in series}


@respx.mock
def test_get_series_data_uses_live_derived_response_and_query_params():
    fixture = load_fixture("series_data_page_1.json")
    route = respx.get(f"{BASE_URL}/sdg/Series/Data").mock(
        return_value=httpx.Response(200, json=fixture)
    )

    data = UNSDClient().get_series_data([SERIES_CODE], area_code=AREA_CODE)

    request = route.calls.last.request
    assert request.url.params["seriesCode"] == SERIES_CODE
    assert request.url.params["areaCode"] == AREA_CODE
    assert request.url.params["pageSize"] == "1000"
    assert request.url.params["page"] == "1"
    assert data == fixture["data"]
    assert data


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
