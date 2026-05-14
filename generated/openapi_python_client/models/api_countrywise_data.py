from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_year_wise_data import ApiYearWiseData


T = TypeVar("T", bound="ApiCountrywiseData")


@_attrs_define
class ApiCountrywiseData:
    """
    Attributes:
        geo_area_code (str | Unset):
        geo_area_name (str | Unset):
        chart_color (str | Unset):
        year_wise_data (list[ApiYearWiseData] | Unset):
    """

    geo_area_code: str | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    chart_color: str | Unset = UNSET
    year_wise_data: list[ApiYearWiseData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        chart_color = self.chart_color

        year_wise_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.year_wise_data, Unset):
            year_wise_data = []
            for year_wise_data_item_data in self.year_wise_data:
                year_wise_data_item = year_wise_data_item_data.to_dict()
                year_wise_data.append(year_wise_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name
        if chart_color is not UNSET:
            field_dict["chartColor"] = chart_color
        if year_wise_data is not UNSET:
            field_dict["yearWiseData"] = year_wise_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_year_wise_data import ApiYearWiseData

        d = dict(src_dict)
        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        chart_color = d.pop("chartColor", UNSET)

        _year_wise_data = d.pop("yearWiseData", UNSET)
        year_wise_data: list[ApiYearWiseData] | Unset = UNSET
        if _year_wise_data is not UNSET:
            year_wise_data = []
            for year_wise_data_item_data in _year_wise_data:
                year_wise_data_item = ApiYearWiseData.from_dict(
                    year_wise_data_item_data
                )

                year_wise_data.append(year_wise_data_item)

        api_countrywise_data = cls(
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
            chart_color=chart_color,
            year_wise_data=year_wise_data,
        )

        api_countrywise_data.additional_properties = d
        return api_countrywise_data

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
