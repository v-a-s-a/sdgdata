from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiGeoArea")


@_attrs_define
class ApiGeoArea:
    """Represents a geography area that could be a country or a region.

    Attributes:
        geo_area_code (str | Unset): geoAreaCode is equivalent to M49
        geo_area_name (str | Unset): geoArea Name is the offician UN name for that country or region.
    """

    geo_area_code: str | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        api_geo_area = cls(
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
        )

        api_geo_area.additional_properties = d
        return api_geo_area

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
