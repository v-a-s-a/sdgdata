import os

import httpx
import pytest

from pyunsdg.client import BASE_URL
from tests.helpers import (
    AREA_CODE,
    SERIES_CODE,
    assert_record_contains_keys,
    load_fixture,
    unique_series_codes,
)


@pytest.mark.live
@pytest.mark.skipif(
    os.environ.get("PYUNSDG_LIVE_TESTS") != "1",
    reason="set PYUNSDG_LIVE_TESTS=1 to call the live UNSD API",
)
def test_live_unsd_api_matches_mock_fixture_shape():
    fixtures = {
        "geo_areas": load_fixture("geo_area_list.json"),
        "targets_without_children": load_fixture("target_list_without_children.json"),
        "targets_with_children": load_fixture("target_list_with_children.json"),
        "series_data": load_fixture("series_data_page_1.json"),
    }

    with httpx.Client(base_url=BASE_URL, timeout=60.0) as client:
        live_geo_areas = client.get("/sdg/GeoArea/List").raise_for_status().json()
        live_targets_without_children = (
            client.get("/sdg/Target/List", params={"includechildren": False})
            .raise_for_status()
            .json()
        )
        live_targets_with_children = (
            client.get("/sdg/Target/List", params={"includechildren": True})
            .raise_for_status()
            .json()
        )
        live_series_data = (
            client.get(
                "/sdg/Series/Data",
                params={
                    "seriesCode": SERIES_CODE,
                    "areaCode": AREA_CODE,
                    "pageSize": 1000,
                    "page": 1,
                },
            )
            .raise_for_status()
            .json()
        )

    for fixture_area in fixtures["geo_areas"]:
        assert_record_contains_keys(fixture_area, live_geo_areas, "geoAreaCode")

    assert_record_contains_keys(
        fixtures["targets_without_children"][0],
        live_targets_without_children,
        "code",
    )

    fixture_target = fixtures["targets_with_children"][0]
    live_target = next(
        target
        for target in live_targets_with_children
        if target.get("code") == fixture_target["code"]
    )
    assert set(fixture_target).issubset(live_target)
    assert SERIES_CODE in unique_series_codes(live_target)

    assert set(fixtures["series_data"]).issubset(live_series_data)
    assert isinstance(live_series_data.get("data"), list)
    assert live_series_data["data"], (
        "The committed series-data fixture query returned no live observations. "
        "Run `uv run python scripts/download_test_fixtures.py` to refresh fixtures."
    )
