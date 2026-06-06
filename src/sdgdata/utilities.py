import json
import re
from collections.abc import Mapping, Sequence
from typing import Literal

from sdgdata.models import ApiDimension

_RELEASE_PATTERN = re.compile(r"^(\d{4})\.Q(\d+)\.G\.(\d+)$")
DimensionMode = Literal["coarsest", "all"]
DimensionFilters = Mapping[str, str | Sequence[str]]
DimensionArgument = DimensionMode | DimensionFilters


def _series_code_list(series_codes: Sequence[str]) -> list[str]:
    if isinstance(series_codes, str | bytes):
        raise TypeError('series_codes must be a sequence of strings, such as ["SERIES_CODE"]')
    return list(series_codes)


def _normalize_singleton_list(value):
    if isinstance(value, list) and len(value) == 1:
        return value[0]
    return value


def _normalize_time_period_start(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def _normalize_observation(observation: dict) -> dict:
    normalized = {**observation}
    for key in ("goal", "target", "indicator"):
        normalized[key] = _normalize_singleton_list(normalized.get(key))
    if "timePeriodStart" in normalized:
        normalized["timePeriodStart"] = _normalize_time_period_start(normalized["timePeriodStart"])
    return normalized


def _release_sort_key(release: str | None) -> tuple[int, int, int]:
    match = _RELEASE_PATTERN.match(release or "")
    if match is None:
        return (-1, -1, -1)
    return tuple(int(part) for part in match.groups())


def _period_value(period: str | None) -> int | None:
    if period is None:
        return None
    return int(period)


def _period_query_params(
    start_period: str | None,
    end_period: str | None,
) -> dict[str, list[str]] | None:
    start = _period_value(start_period)
    end = _period_value(end_period)
    if start is None and end is None:
        return None
    if end is None:
        raise ValueError("start_period and end_period must be provided together")
    if start is None:
        raise ValueError("start_period and end_period must be provided together")
    if end < start:
        return {}
    return {"timePeriod": [str(period) for period in range(start, end + 1)]}


def _dimension_payload(dimensions: DimensionFilters) -> str:
    payload = []
    for name, values in dimensions.items():
        if isinstance(values, str):
            values = [values]
        payload.append({"name": name, "values": list(values)})
    return json.dumps(payload, separators=(",", ":"))


def _coarsest_dimension_filters(dimensions: list[ApiDimension]) -> dict[str, str]:
    filters = {}
    preferred_codes = {
        "age": ["ALLAGE"],
        "sex": ["BOTHSEX"],
        "location": ["ALLAREA"],
        "reporting type": ["G", "N", "R"],
    }
    total_description_markers = (
        "total",
        "all ",
        "all age",
        "both",
        "no break",
        "no breakdown",
        "national average",
    )

    for dimension in dimensions:
        if dimension.id is None or not dimension.codes:
            continue

        dimension_id = dimension.id.lower()
        selected_code = None

        for preferred_code in preferred_codes.get(dimension_id, []):
            selected_code = next(
                (code for code in dimension.codes if code.code == preferred_code),
                None,
            )
            if selected_code is not None:
                break

        if selected_code is None:
            selected_code = next(
                (code for code in dimension.codes if code.code == "_T" or code.sdmx == "_T"),
                None,
            )

        if selected_code is None:
            selected_code = next(
                (
                    code
                    for code in dimension.codes
                    if code.description
                    and any(
                        marker in code.description.lower() for marker in total_description_markers
                    )
                ),
                None,
            )

        if selected_code is None:
            selected_code = dimension.codes[0]

        if selected_code.code is not None:
            filters[dimension.id] = selected_code.code

    return filters


def _time_series_key(record: dict) -> tuple:
    dimensions = record.get("dimensions") or {}
    return (
        record.get("series"),
        record.get("geoAreaCode"),
        tuple(sorted(dimensions.items())),
    )


def is_single_time_series(records: list[dict]) -> bool:
    """
    Returns whether records contain exactly one series/area/dimension time series.
    """
    if not records:
        return False
    return len({_time_series_key(record) for record in records}) == 1
