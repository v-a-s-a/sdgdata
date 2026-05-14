from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_slice_data_dimensions_item import ApiSliceDataDimensionsItem


T = TypeVar("T", bound="ApiSliceData")


@_attrs_define
class ApiSliceData:
    """
    Attributes:
        series (str | Unset): Gets or Sets Series
        geo_area_code (int | Unset): Gets or Sets geoAreaCode
        geo_area_name (str | Unset): Gets or Sets geoAreaName
        dimensions (list[ApiSliceDataDimensionsItem] | Unset): Gets or Sets Dimensions for slice data
    """

    series: str | Unset = UNSET
    geo_area_code: int | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    dimensions: list[ApiSliceDataDimensionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series = self.series

        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        dimensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series is not UNSET:
            field_dict["series"] = series
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_slice_data_dimensions_item import ApiSliceDataDimensionsItem

        d = dict(src_dict)
        series = d.pop("series", UNSET)

        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: list[ApiSliceDataDimensionsItem] | Unset = UNSET
        if _dimensions is not UNSET:
            dimensions = []
            for dimensions_item_data in _dimensions:
                dimensions_item = ApiSliceDataDimensionsItem.from_dict(
                    dimensions_item_data
                )

                dimensions.append(dimensions_item)

        api_slice_data = cls(
            series=series,
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
            dimensions=dimensions,
        )

        api_slice_data.additional_properties = d
        return api_slice_data

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
