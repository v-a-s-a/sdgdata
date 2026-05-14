from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_series_data import ApiSeriesData


T = TypeVar("T", bound="ApiMultiSeriesOneArea")


@_attrs_define
class ApiMultiSeriesOneArea:
    """
    Attributes:
        geo_area_code (str | Unset):
        geo_area_name (str | Unset):
        ct_series_wise_data (list[ApiSeriesData] | Unset):
    """

    geo_area_code: str | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    ct_series_wise_data: list[ApiSeriesData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        ct_series_wise_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ct_series_wise_data, Unset):
            ct_series_wise_data = []
            for ct_series_wise_data_item_data in self.ct_series_wise_data:
                ct_series_wise_data_item = ct_series_wise_data_item_data.to_dict()
                ct_series_wise_data.append(ct_series_wise_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name
        if ct_series_wise_data is not UNSET:
            field_dict["ctSeriesWiseData"] = ct_series_wise_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_series_data import ApiSeriesData

        d = dict(src_dict)
        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        _ct_series_wise_data = d.pop("ctSeriesWiseData", UNSET)
        ct_series_wise_data: list[ApiSeriesData] | Unset = UNSET
        if _ct_series_wise_data is not UNSET:
            ct_series_wise_data = []
            for ct_series_wise_data_item_data in _ct_series_wise_data:
                ct_series_wise_data_item = ApiSeriesData.from_dict(
                    ct_series_wise_data_item_data
                )

                ct_series_wise_data.append(ct_series_wise_data_item)

        api_multi_series_one_area = cls(
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
            ct_series_wise_data=ct_series_wise_data,
        )

        api_multi_series_one_area.additional_properties = d
        return api_multi_series_one_area

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
