from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgCompareTrendsGetDataMultiSeriesOneAreaPostBody")


@_attrs_define
class V1SdgCompareTrendsGetDataMultiSeriesOneAreaPostBody:
    """
    Attributes:
        methodology_type (int): Methodology For timeSeries(1-Original Data,2-Normalized Data 2015,3-Normalized Data
            2010,4-Growth Rate)
        area_code (int): Country code e.g 64
        from_period (int): From Year value e.g 2005
        to_period (int): Upto Year value e.g 2015
        series (list[str] | Unset): Array of series codes e.g SP_ACS_BSRVH2O~RURAL,SP_ACS_BSRVH2O~ALLAREA
    """

    methodology_type: int
    area_code: int
    from_period: int
    to_period: int
    series: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        methodology_type = self.methodology_type

        area_code = self.area_code

        from_period = self.from_period

        to_period = self.to_period

        series: list[str] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "methodologyType": methodology_type,
                "areaCode": area_code,
                "fromPeriod": from_period,
                "toPeriod": to_period,
            }
        )
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        methodology_type = d.pop("methodologyType")

        area_code = d.pop("areaCode")

        from_period = d.pop("fromPeriod")

        to_period = d.pop("toPeriod")

        series = cast(list[str], d.pop("series", UNSET))

        v1_sdg_compare_trends_get_data_multi_series_one_area_post_body = cls(
            methodology_type=methodology_type,
            area_code=area_code,
            from_period=from_period,
            to_period=to_period,
            series=series,
        )

        v1_sdg_compare_trends_get_data_multi_series_one_area_post_body.additional_properties = d
        return v1_sdg_compare_trends_get_data_multi_series_one_area_post_body

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
