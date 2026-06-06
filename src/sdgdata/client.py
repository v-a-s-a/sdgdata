import json
import re
from collections.abc import Mapping, Sequence
from typing import Literal

import httpx

from sdgdata.models import (
    ApiDimension,
    ApiGeoArea,
    ApiGoal,
    ApiIndicator,
    ApiSerie,
    ApiTarget,
    ConceptsMasterData,
    SDMXMetaDataResponse,
)

from . import debug
from .metadata import IndicatorSeriesMetadata, SeriesMetadata, TargetSeriesMetadata

# standard UNSD API base URL
BASE_URL = "https://unstats.un.org/sdgapi/v1"
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


def _group_series_metadata(
    series_items: list[ApiSerie],
    dimensions_by_code: Mapping[str, list[ApiDimension]],
) -> list[SeriesMetadata]:
    """
    Groups repeated UNSD release rows into one discovery record per series code.
    """
    series_by_code: dict[str, list[ApiSerie]] = {}
    for series in series_items:
        if series.code is None:
            continue
        series_by_code.setdefault(series.code, []).append(series)

    grouped_series = []
    for code, releases in series_by_code.items():
        latest = max(releases, key=lambda item: _release_sort_key(item.release))
        release_codes = sorted(
            {release.release for release in releases if release.release is not None},
            key=_release_sort_key,
        )
        grouped_series.append(
            SeriesMetadata(
                code=code,
                description=latest.description,
                uri=latest.uri,
                latest_release=latest.release,
                releases=release_codes,
                dimensions=dimensions_by_code.get(code, []),
            )
        )

    return sorted(grouped_series, key=lambda series: series.code)


def _indicator_series_metadata(
    indicator: ApiIndicator,
    dimensions_by_code: Mapping[str, list[ApiDimension]],
) -> IndicatorSeriesMetadata:
    """
    Builds the public discovery model for one generated UNSD indicator model.
    """
    return IndicatorSeriesMetadata(
        code=indicator.code or "",
        description=indicator.description,
        tier=indicator.tier,
        uri=indicator.uri,
        series=_group_series_metadata(indicator.series or [], dimensions_by_code),
    )


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


class SDGClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL, timeout=30.0)

    def _get(self, url: str, *, params: dict | None = None) -> httpx.Response:
        request = self.client.build_request("GET", url, params=params)
        debug.print_query(request)
        return self.client.send(request)

    def get_targets(self, include_children: bool = False) -> list[ApiTarget]:
        """
        Fetches all targets, optionally including their indicators and series.
        """
        response = self._get("/sdg/Target/List", params={"includechildren": include_children})
        response.raise_for_status()
        data = response.json()
        return [ApiTarget(**item) for item in data]

    def get_series_codes(
        self, target_code: str | None = None, *, all_releases: bool = False
    ) -> list[ApiSerie]:
        """
        Returns latest series codes and descriptions, optionally filtered by target code.
        """
        targets = self.get_targets(include_children=True)
        series_list = []
        for target in targets:
            if target_code and target.code != target_code:
                continue
            if target.indicators:
                for indicator in target.indicators:
                    if indicator.series:
                        series_list.extend(indicator.series)
        if all_releases:
            return series_list

        latest_by_code = {}
        for series in series_list:
            if series.code is None:
                continue
            current = latest_by_code.get(series.code)
            if current is None or _release_sort_key(series.release) > _release_sort_key(
                current.release
            ):
                latest_by_code[series.code] = series

        return list(latest_by_code.values())

    def get_indicator_series(self, indicator_code: str) -> IndicatorSeriesMetadata:
        """
        Returns grouped series metadata and dimensions for an indicator.
        """
        for target in self.get_targets(include_children=True):
            for indicator in target.indicators or []:
                if indicator.code == indicator_code:
                    series_codes = {
                        series.code for series in indicator.series or [] if series.code is not None
                    }
                    dimensions_by_code = {
                        code: self.get_series_dimensions(code) for code in series_codes
                    }
                    return _indicator_series_metadata(indicator, dimensions_by_code)

        raise ValueError(f"indicator code {indicator_code!r} was not found")

    def get_target_series(self, target_code: str) -> TargetSeriesMetadata:
        """
        Returns grouped indicator and series metadata for a target.
        """
        for target in self.get_targets(include_children=True):
            if target.code != target_code:
                continue

            series_codes = {
                series.code
                for indicator in target.indicators or []
                for series in indicator.series or []
                if series.code is not None
            }
            dimensions_by_code = {code: self.get_series_dimensions(code) for code in series_codes}
            return TargetSeriesMetadata(
                code=target.code or "",
                title=target.title,
                description=target.description,
                uri=target.uri,
                indicators=[
                    _indicator_series_metadata(indicator, dimensions_by_code)
                    for indicator in target.indicators or []
                ],
            )

        raise ValueError(f"target code {target_code!r} was not found")

    def get_geo_areas(self) -> list[ApiGeoArea]:
        """
        Returns a list of geographic areas and their M49 codes.
        """
        response = self._get("/sdg/GeoArea/List")
        response.raise_for_status()
        data = response.json()
        return [ApiGeoArea(**item) for item in data]

    def get_goals(self) -> list[ApiGoal]:
        """
        Fetches all SDG goals.
        """
        response = self._get("/sdg/Goal/List")
        response.raise_for_status()
        data = response.json()
        return [ApiGoal(**item) for item in data]

    def get_indicators(self, include_series: bool = True) -> list[ApiTarget]:
        """
        Fetches all indicators, optionally including their series.
        """
        response = self._get("/sdg/Indicator/List", params={"includechildren": include_series})
        response.raise_for_status()
        data = response.json()
        return [ApiTarget(**item) for item in data]

    def get_concepts(self) -> list[ConceptsMasterData]:
        """
        Fetches all concepts.
        """
        response = self._get("sdg/SDMXMetadata/GetConceptsMasterList")
        response.raise_for_status()
        return [ConceptsMasterData(**item) for item in response.json()]

    def get_sdmx_series(self) -> list[SDMXMetaDataResponse]:
        """
        Fetches all SDMX series metadata.
        """
        response = self._get("sdg/SDMXMetadata/GetSeries")
        response.raise_for_status()
        return [SDMXMetaDataResponse(**item) for item in response.json()]

    def get_series_dimensions(self, series_code: str) -> list[ApiDimension]:
        """
        Fetches available disaggregation dimensions for a series.
        """
        response = self._get(f"/sdg/Series/{series_code}/Dimensions")
        response.raise_for_status()
        return [ApiDimension(**item) for item in response.json()]

    def get_series_data(
        self,
        series_codes: Sequence[str],
        area_code: str | None = None,
        start_period: str | None = None,
        end_period: str | None = None,
        release_code: str | None = None,
        dimensions: DimensionArgument = "coarsest",
    ) -> list[dict]:
        """
        Pulls actual data observations for given series codes across all pages.
        Returns a list of dictionaries, making it easy to create a Polars or Pandas DataFrame.
        """
        series_codes = _series_code_list(series_codes)
        params = {"pageSize": 1000}
        if area_code:
            params["areaCode"] = area_code
        if release_code:
            params["releaseCode"] = release_code
        time_period_params = _period_query_params(start_period, end_period)
        if time_period_params == {}:
            return []
        if time_period_params is not None:
            params.update(time_period_params)

        if dimensions == "coarsest":
            all_observations = []
            for series_code in series_codes:
                series_params = {**params, "seriesCode": series_code}
                coarsest_dimensions = _coarsest_dimension_filters(
                    self.get_series_dimensions(series_code)
                )
                if coarsest_dimensions:
                    series_params["dimensions"] = _dimension_payload(coarsest_dimensions)
                all_observations.extend(self._fetch_series_data(series_params))
            return all_observations

        params["seriesCode"] = ",".join(series_codes)
        if dimensions != "all":
            if not isinstance(dimensions, Mapping):
                raise ValueError('dimensions must be "coarsest", "all", or a mapping')
            params["dimensions"] = _dimension_payload(dimensions)

        return self._fetch_series_data(params)

    def _fetch_series_data(self, params: dict) -> list[dict]:
        time_periods = params.get("timePeriod")
        if isinstance(time_periods, list) and len(time_periods) > 1 and "dimensions" in params:
            all_observations = []
            for time_period in time_periods:
                period_params = {**params, "timePeriod": [time_period]}
                all_observations.extend(self._fetch_series_data(period_params))
            return all_observations

        params = {**params, "page": 1}
        all_observations = []

        while True:
            # /sdg/Series/Data is often more direct than generic Observation for this
            response = self._get("/sdg/Series/Data", params=params)
            response.raise_for_status()

            page_data = response.json()
            observations = page_data.get("data", [])
            all_observations.extend(_normalize_observation(item) for item in observations)

            total_pages = page_data.get("totalPages")
            if total_pages is not None and params["page"] >= int(total_pages):
                break

            # UNSD may omit totalPages, so fall back to response size.
            if not observations or len(observations) < params.get("pageSize", 100):
                break

            params["page"] += 1

        return all_observations
