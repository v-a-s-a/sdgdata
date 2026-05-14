from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="V1SdgCompareTrendsGetAreaBySeriesDisaggregationDimensionsPostBody"
)


@_attrs_define
class V1SdgCompareTrendsGetAreaBySeriesDisaggregationDimensionsPostBody:
    """
    Attributes:
        methodology_type (int): Methodology For timeSeries(1-Original Data,2-Normalized Data 2015,3-Normalized Data
            2010,4-Growth Rate)
        series (list[str] | Unset): SDMX code for that series
    """

    methodology_type: int
    series: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        methodology_type = self.methodology_type

        series: list[str] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "methodologyType": methodology_type,
            }
        )
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        methodology_type = d.pop("methodologyType")

        series = cast(list[str], d.pop("series", UNSET))

        v1_sdg_compare_trends_get_area_by_series_disaggregation_dimensions_post_body = (
            cls(
                methodology_type=methodology_type,
                series=series,
            )
        )

        v1_sdg_compare_trends_get_area_by_series_disaggregation_dimensions_post_body.additional_properties = d
        return (
            v1_sdg_compare_trends_get_area_by_series_disaggregation_dimensions_post_body
        )

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
