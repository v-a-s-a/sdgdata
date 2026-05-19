import json
import re
from collections.abc import Mapping, Sequence
from typing import Literal, List, Optional

import httpx

from pyunsdg.models import (
    ApiTarget, 
    ApiObservationPage, 
    ApiGeoArea, 
    ApiGoal, 
    ConceptsMasterData, 
    SDMXMetaDataResponse,
    ApiSerie,
    ApiDimension,
)

# standard UNSD API base URL
BASE_URL = "https://unstats.un.org/sdgapi/v1"
_RELEASE_PATTERN = re.compile(r"^(\d{4})\.Q(\d+)\.G\.(\d+)$")
DimensionMode = Literal["coarsest", "all"]
DimensionFilters = Mapping[str, str | Sequence[str]]
DimensionArgument = DimensionMode | DimensionFilters


def _release_sort_key(release: Optional[str]) -> tuple[int, int, int]:
    match = _RELEASE_PATTERN.match(release or "")
    if match is None:
        return (-1, -1, -1)
    return tuple(int(part) for part in match.groups())


def _period_value(period: Optional[str]) -> Optional[int]:
    if period is None:
        return None
    return int(period)


def _period_query_params(
    start_period: Optional[str],
    end_period: Optional[str],
) -> Optional[dict[str, str]]:
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
    return {"timePeriodStart": str(start), "timePeriodEnd": str(end)}


def _dimension_payload(dimensions: DimensionFilters) -> str:
    payload = []
    for name, values in dimensions.items():
        if isinstance(values, str):
            values = [values]
        payload.append({"name": name, "values": list(values)})
    return json.dumps(payload, separators=(",", ":"))


def _coarsest_dimension_filters(dimensions: List[ApiDimension]) -> dict[str, str]:
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
                (
                    code
                    for code in dimension.codes
                    if code.code == "_T" or code.sdmx == "_T"
                ),
                None,
            )

        if selected_code is None:
            selected_code = next(
                (
                    code
                    for code in dimension.codes
                    if code.description
                    and any(
                        marker in code.description.lower()
                        for marker in total_description_markers
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


class UNSDClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL, timeout=30.0)

    def get_targets(self) -> List[ApiTarget]:
        """
        Returns all targets and descriptions.
        """
        return self.get_target_list(include_children=False)

    def get_series_codes(
        self, target_code: Optional[str] = None, *, all_releases: bool = False
    ) -> List[ApiSerie]:
        """
        Returns latest series codes and descriptions, optionally filtered by target code.
        """
        targets = self.get_target_list(include_children=True)
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

    def get_geo_areas(self) -> List[ApiGeoArea]:
        """
        Returns a list of geographic areas and their M49 codes.
        """
        return self.get_geo_area_list()

    def get_target_list(self, include_children: bool = True) -> List[ApiTarget]:
        """
        Fetches all targets, optionally including their indicators and series.
        """
        response = self.client.get("/sdg/Target/List", params={"includechildren": include_children})
        response.raise_for_status()
        data = response.json()
        return [ApiTarget(**item) for item in data]
    
    def get_goal_list(self) -> List[ApiGoal]:
        """
        Fetches all SDG goals.
        """
        response = self.client.get("/sdg/Goal/List")
        response.raise_for_status()
        data = response.json()
        return [ApiGoal(**item) for item in data]
    
    def get_indicator_list(self, include_series: bool = True) -> List[ApiTarget]:
        """
        Fetches all indicators, optionally including their series.
        """
        response = self.client.get("/sdg/Indicator/List", params={"includechildren": include_series})
        response.raise_for_status()
        data = response.json()
        return [ApiTarget(**item) for item in data]
    
    def get_geo_area_list(self) -> List[ApiGeoArea]:
        """
        Fetches all geographic areas.
        """
        response = self.client.get("/sdg/GeoArea/List")
        response.raise_for_status()
        data = response.json()
        return [ApiGeoArea(**item) for item in data]

    def get_concept_list(self) -> List[ConceptsMasterData]:
        """
        Fetches all concepts. The API does not provide a structured model for concepts, so we return raw dicts.
        """
        response = self.client.get("sdg/SDMXMetadata/GetConceptsMasterList")
        response.raise_for_status()
        return [ConceptsMasterData(**item) for item in response.json()]
    
    def get_sdmx_series_list(self) -> List[SDMXMetaDataResponse]:
        """
        Fetches all SDMX series metadata. The API does not provide a structured model for SDMX metadata, so we return raw dicts.
        """
        response = self.client.get("sdg/SDMXMetadata/GetSeries")
        response.raise_for_status()
        return response.json()

    def get_series_dimensions(self, series_code: str) -> List[ApiDimension]:
        """
        Fetches available disaggregation dimensions for a series.
        """
        response = self.client.get(f"/sdg/Series/{series_code}/Dimensions")
        response.raise_for_status()
        return [ApiDimension(**item) for item in response.json()]

    def get_series_data(
        self, 
        series_codes: List[str], 
        area_code: Optional[str] = None,
        start_period: Optional[str] = None,
        end_period: Optional[str] = None,
        release_code: Optional[str] = None,
        dimensions: DimensionArgument = "coarsest",
    ) -> List[dict]:
        """
        Pulls actual data observations for given series codes across all pages.
        Returns a list of dictionaries, making it easy to create a Polars or Pandas DataFrame.
        """
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
                    series_params["dimensions"] = _dimension_payload(
                        coarsest_dimensions
                    )
                all_observations.extend(self._fetch_series_data(series_params))
            return all_observations

        params["seriesCode"] = ",".join(series_codes)
        if dimensions != "all":
            if not isinstance(dimensions, Mapping):
                raise ValueError('dimensions must be "coarsest", "all", or a mapping')
            params["dimensions"] = _dimension_payload(dimensions)

        return self._fetch_series_data(params)

    def _fetch_series_data(self, params: dict) -> List[dict]:
        params = {**params, "page": 1}
        all_observations = []

        while True:
            # /sdg/Series/Data is often more direct than generic Observation for this
            response = self.client.get("/sdg/Series/Data", params=params)
            response.raise_for_status()
            
            page_data = response.json()
            observations = page_data.get("data", [])
            all_observations.extend(observations)

            total_pages = page_data.get("totalPages")
            if total_pages is not None and params["page"] >= int(total_pages):
                break

            # UNSD may omit totalPages, so fall back to response size.
            if not observations or len(observations) < params.get("pageSize", 100):
                break
                
            params["page"] += 1

        return all_observations
