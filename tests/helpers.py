import json
from pathlib import Path
from typing import Any


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "unsd_api"
TARGET_CODE = "3.8"
SERIES_CODE = "SH_OOP_XPD_EARNNET40"
AREA_CODE = "4"


def load_fixture(name: str) -> Any:
    return json.loads((FIXTURE_DIR / name).read_text())


def unique_series_codes(target: dict[str, Any]) -> set[str]:
    codes = set()
    for indicator in target.get("indicators") or []:
        for series in indicator.get("series") or []:
            if series.get("code"):
                codes.add(series["code"])
    return codes


def assert_record_contains_keys(
    fixture_record: dict[str, Any],
    live_records: list[dict[str, Any]],
    key_field: str,
) -> None:
    fixture_key = fixture_record[key_field]
    live_record = next(
        (record for record in live_records if record.get(key_field) == fixture_key),
        None,
    )
    assert live_record is not None, f"{key_field}={fixture_key!r} was not live"
    assert set(fixture_record).issubset(live_record)
