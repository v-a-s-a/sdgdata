from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgCompareTrendsGetDataOneSeriesMultiAreaPostBody")


@_attrs_define
class V1SdgCompareTrendsGetDataOneSeriesMultiAreaPostBody:
    """
    Attributes:
        methodology_type (int): Methodology For timeSeries(1-Original Data,2-Normalized Data 2015,3-Normalized Data
            2010,4-Growth Rate)
        from_period (int): From Year value e.g 2005
        to_period (int): Upto Year value e.g 2015
        series (str | Unset): Series Code e.g SI_POV_EMP1
        disaggregated_category (str | Unset): Disaggregated dimension value e.g 15+ | FEMALE
        area_code (list[int] | Unset): Array of country codes e.g 432
    """

    methodology_type: int
    from_period: int
    to_period: int
    series: str | Unset = UNSET
    disaggregated_category: str | Unset = UNSET
    area_code: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        methodology_type = self.methodology_type

        from_period = self.from_period

        to_period = self.to_period

        series = self.series

        disaggregated_category = self.disaggregated_category

        area_code: list[int] | Unset = UNSET
        if not isinstance(self.area_code, Unset):
            area_code = self.area_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "methodologyType": methodology_type,
                "fromPeriod": from_period,
                "toPeriod": to_period,
            }
        )
        if series is not UNSET:
            field_dict["series"] = series
        if disaggregated_category is not UNSET:
            field_dict["disaggregatedCategory"] = disaggregated_category
        if area_code is not UNSET:
            field_dict["areaCode"] = area_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        methodology_type = d.pop("methodologyType")

        from_period = d.pop("fromPeriod")

        to_period = d.pop("toPeriod")

        series = d.pop("series", UNSET)

        disaggregated_category = d.pop("disaggregatedCategory", UNSET)

        area_code = cast(list[int], d.pop("areaCode", UNSET))

        v1_sdg_compare_trends_get_data_one_series_multi_area_post_body = cls(
            methodology_type=methodology_type,
            from_period=from_period,
            to_period=to_period,
            series=series,
            disaggregated_category=disaggregated_category,
            area_code=area_code,
        )

        v1_sdg_compare_trends_get_data_one_series_multi_area_post_body.additional_properties = d
        return v1_sdg_compare_trends_get_data_one_series_multi_area_post_body

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
