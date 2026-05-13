import json
from pathlib import Path
from typing import Any

import httpx


BASE_URL = "https://unstats.un.org/sdgapi/v1"
FIXTURE_DIR = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "unsd_api"
TARGET_CODE = "3.8"
NON_MATCHING_TARGET_CODE = "4.1"
SERIES_CODE = "SH_OOP_XPD_EARNNET40"
AREA_CODE = "4"


def fetch_json(
    client: httpx.Client, path: str, params: dict[str, Any] | None = None
) -> Any:
    response = client.get(path, params=params)
    response.raise_for_status()
    return response.json()


def find_target(targets: list[dict[str, Any]], code: str) -> dict[str, Any]:
    for target in targets:
        if target.get("code") == code:
            return target
    raise RuntimeError(f"Target {code} was not found in live UNSD API response")


def write_fixture(name: str, data: Any) -> None:
    path = FIXTURE_DIR / name
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    FIXTURE_DIR.mkdir(parents=True, exist_ok=True)

    with httpx.Client(base_url=BASE_URL, timeout=60.0) as client:
        geo_areas = fetch_json(client, "/sdg/GeoArea/List")
        targets_without_children = fetch_json(
            client, "/sdg/Target/List", {"includechildren": False}
        )
        targets_with_children = fetch_json(
            client, "/sdg/Target/List", {"includechildren": True}
        )
        series_data = fetch_json(
            client,
            "/sdg/Series/Data",
            {
                "seriesCode": SERIES_CODE,
                "areaCode": AREA_CODE,
                "pageSize": 1000,
                "page": 1,
            },
        )

    target_without_children = find_target(targets_without_children, TARGET_CODE)
    target_with_children = find_target(targets_with_children, TARGET_CODE)
    non_matching_target = find_target(targets_with_children, NON_MATCHING_TARGET_CODE)

    write_fixture("geo_area_list.json", geo_areas[:5])
    write_fixture("target_list_without_children.json", [target_without_children])
    write_fixture(
        "target_list_with_children.json",
        [target_with_children, non_matching_target],
    )
    write_fixture("series_data_page_1.json", series_data)


if __name__ == "__main__":
    main()
