from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgSeriesDataCountPostBody")


@_attrs_define
class V1SdgSeriesDataCountPostBody:
    """
    Attributes:
        series_codes (list[str] | Unset): SDMX code for that series
        area_codes (list[int] | Unset): Code for a group of regions
        time_period_start (float | Unset): Time series start point
        time_period_end (float | Unset): Tine sertues end point
    """

    series_codes: list[str] | Unset = UNSET
    area_codes: list[int] | Unset = UNSET
    time_period_start: float | Unset = UNSET
    time_period_end: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_codes: list[str] | Unset = UNSET
        if not isinstance(self.series_codes, Unset):
            series_codes = self.series_codes

        area_codes: list[int] | Unset = UNSET
        if not isinstance(self.area_codes, Unset):
            area_codes = self.area_codes

        time_period_start = self.time_period_start

        time_period_end = self.time_period_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series_codes is not UNSET:
            field_dict["seriesCodes"] = series_codes
        if area_codes is not UNSET:
            field_dict["areaCodes"] = area_codes
        if time_period_start is not UNSET:
            field_dict["timePeriodStart"] = time_period_start
        if time_period_end is not UNSET:
            field_dict["timePeriodEnd"] = time_period_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series_codes = cast(list[str], d.pop("seriesCodes", UNSET))

        area_codes = cast(list[int], d.pop("areaCodes", UNSET))

        time_period_start = d.pop("timePeriodStart", UNSET)

        time_period_end = d.pop("timePeriodEnd", UNSET)

        v1_sdg_series_data_count_post_body = cls(
            series_codes=series_codes,
            area_codes=area_codes,
            time_period_start=time_period_start,
            time_period_end=time_period_end,
        )

        v1_sdg_series_data_count_post_body.additional_properties = d
        return v1_sdg_series_data_count_post_body

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
