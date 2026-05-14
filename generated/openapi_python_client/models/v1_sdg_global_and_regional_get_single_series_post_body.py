from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgGlobalAndRegionalGetSingleSeriesPostBody")


@_attrs_define
class V1SdgGlobalAndRegionalGetSingleSeriesPostBody:
    """
    Attributes:
        indicators (str | Unset):
        series_code (str | Unset): Series Code e.g SI_POV_EMP1
        area_code (list[str] | Unset): List of country codes e.g 202
        years (list[int] | Unset): List of year e.g 2002
    """

    indicators: str | Unset = UNSET
    series_code: str | Unset = UNSET
    area_code: list[str] | Unset = UNSET
    years: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indicators = self.indicators

        series_code = self.series_code

        area_code: list[str] | Unset = UNSET
        if not isinstance(self.area_code, Unset):
            area_code = self.area_code

        years: list[int] | Unset = UNSET
        if not isinstance(self.years, Unset):
            years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indicators is not UNSET:
            field_dict["indicators"] = indicators
        if series_code is not UNSET:
            field_dict["seriesCode"] = series_code
        if area_code is not UNSET:
            field_dict["areaCode"] = area_code
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indicators = d.pop("indicators", UNSET)

        series_code = d.pop("seriesCode", UNSET)

        area_code = cast(list[str], d.pop("areaCode", UNSET))

        years = cast(list[int], d.pop("years", UNSET))

        v1_sdg_global_and_regional_get_single_series_post_body = cls(
            indicators=indicators,
            series_code=series_code,
            area_code=area_code,
            years=years,
        )

        v1_sdg_global_and_regional_get_single_series_post_body.additional_properties = d
        return v1_sdg_global_and_regional_get_single_series_post_body

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
