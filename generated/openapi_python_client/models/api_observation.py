from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_observation_attributes import ApiObservationAttributes
    from ..models.api_observation_dimensions import ApiObservationDimensions


T = TypeVar("T", bound="ApiObservation")


@_attrs_define
class ApiObservation:
    """
    Attributes:
        goal (list[str] | Unset): Gets or Sets Goal
        target (list[str] | Unset): Gets or Sets Target
        indicator (list[str] | Unset): Gets or Sets Indicator
        series (str | Unset): Gets or Sets Series
        series_description (str | Unset): Gets or Sets Series Description
        series_count (str | Unset): Gets or Sets Series Count
        geo_area_code (str | Unset): Gets or Sets geoAreaCode
        geo_area_name (str | Unset): Gets or Sets geoAreaName
        time_period_start (float | Unset): Gets or Sets timePeriod Start
        value (str | Unset): Gets or Sets Value
        value_type (str | Unset): Gets or Sets ValueType
        time_detail (str | Unset): Gets or Sets TimeDetail
        time_coverage (str | Unset): Gets or Sets TimeCoverage
        upper_bound (str | Unset): Gets or Sets UpperBound
        lower_bound (str | Unset): Gets or Sets LowerBound
        base_period (str | Unset): Gets or Sets BasePeriod
        source (str | Unset): Gets or Sets Source
        geo_info_url (str | Unset): Gets or Sets GeoInfoUrl
        footnotes (list[str] | Unset): Gets or Sets Footnotes
        attributes (ApiObservationAttributes | Unset): Gets or Sets Attributes
        dimensions (ApiObservationDimensions | Unset): Gets or Sets Dimensions
    """

    goal: list[str] | Unset = UNSET
    target: list[str] | Unset = UNSET
    indicator: list[str] | Unset = UNSET
    series: str | Unset = UNSET
    series_description: str | Unset = UNSET
    series_count: str | Unset = UNSET
    geo_area_code: str | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    time_period_start: float | Unset = UNSET
    value: str | Unset = UNSET
    value_type: str | Unset = UNSET
    time_detail: str | Unset = UNSET
    time_coverage: str | Unset = UNSET
    upper_bound: str | Unset = UNSET
    lower_bound: str | Unset = UNSET
    base_period: str | Unset = UNSET
    source: str | Unset = UNSET
    geo_info_url: str | Unset = UNSET
    footnotes: list[str] | Unset = UNSET
    attributes: ApiObservationAttributes | Unset = UNSET
    dimensions: ApiObservationDimensions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal: list[str] | Unset = UNSET
        if not isinstance(self.goal, Unset):
            goal = self.goal

        target: list[str] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target

        indicator: list[str] | Unset = UNSET
        if not isinstance(self.indicator, Unset):
            indicator = self.indicator

        series = self.series

        series_description = self.series_description

        series_count = self.series_count

        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        time_period_start = self.time_period_start

        value = self.value

        value_type = self.value_type

        time_detail = self.time_detail

        time_coverage = self.time_coverage

        upper_bound = self.upper_bound

        lower_bound = self.lower_bound

        base_period = self.base_period

        source = self.source

        geo_info_url = self.geo_info_url

        footnotes: list[str] | Unset = UNSET
        if not isinstance(self.footnotes, Unset):
            footnotes = self.footnotes

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goal is not UNSET:
            field_dict["goal"] = goal
        if target is not UNSET:
            field_dict["target"] = target
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if series is not UNSET:
            field_dict["series"] = series
        if series_description is not UNSET:
            field_dict["seriesDescription"] = series_description
        if series_count is not UNSET:
            field_dict["seriesCount"] = series_count
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name
        if time_period_start is not UNSET:
            field_dict["timePeriodStart"] = time_period_start
        if value is not UNSET:
            field_dict["value"] = value
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if time_detail is not UNSET:
            field_dict["time_detail"] = time_detail
        if time_coverage is not UNSET:
            field_dict["timeCoverage"] = time_coverage
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if base_period is not UNSET:
            field_dict["basePeriod"] = base_period
        if source is not UNSET:
            field_dict["source"] = source
        if geo_info_url is not UNSET:
            field_dict["geoInfoUrl"] = geo_info_url
        if footnotes is not UNSET:
            field_dict["footnotes"] = footnotes
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_observation_attributes import ApiObservationAttributes
        from ..models.api_observation_dimensions import ApiObservationDimensions

        d = dict(src_dict)
        goal = cast(list[str], d.pop("goal", UNSET))

        target = cast(list[str], d.pop("target", UNSET))

        indicator = cast(list[str], d.pop("indicator", UNSET))

        series = d.pop("series", UNSET)

        series_description = d.pop("seriesDescription", UNSET)

        series_count = d.pop("seriesCount", UNSET)

        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        time_period_start = d.pop("timePeriodStart", UNSET)

        value = d.pop("value", UNSET)

        value_type = d.pop("valueType", UNSET)

        time_detail = d.pop("time_detail", UNSET)

        time_coverage = d.pop("timeCoverage", UNSET)

        upper_bound = d.pop("upperBound", UNSET)

        lower_bound = d.pop("lowerBound", UNSET)

        base_period = d.pop("basePeriod", UNSET)

        source = d.pop("source", UNSET)

        geo_info_url = d.pop("geoInfoUrl", UNSET)

        footnotes = cast(list[str], d.pop("footnotes", UNSET))

        _attributes = d.pop("attributes", UNSET)
        attributes: ApiObservationAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ApiObservationAttributes.from_dict(_attributes)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: ApiObservationDimensions | Unset
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = ApiObservationDimensions.from_dict(_dimensions)

        api_observation = cls(
            goal=goal,
            target=target,
            indicator=indicator,
            series=series,
            series_description=series_description,
            series_count=series_count,
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
            time_period_start=time_period_start,
            value=value,
            value_type=value_type,
            time_detail=time_detail,
            time_coverage=time_coverage,
            upper_bound=upper_bound,
            lower_bound=lower_bound,
            base_period=base_period,
            source=source,
            geo_info_url=geo_info_url,
            footnotes=footnotes,
            attributes=attributes,
            dimensions=dimensions,
        )

        api_observation.additional_properties = d
        return api_observation

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
