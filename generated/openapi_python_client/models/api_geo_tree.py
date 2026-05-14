from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiGeoTree")


@_attrs_define
class ApiGeoTree:
    """
    Attributes:
        geo_area_code (int | Unset): Gets or Sets code
        geo_area_name (str | Unset): Gets or Sets name
        type_ (str | Unset): Gets or Sets type
        children (list[ApiGeoTree] | Unset): Gets or Sets children
    """

    geo_area_code: int | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    children: list[ApiGeoTree] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        type_ = self.type_

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        type_ = d.pop("type", UNSET)

        _children = d.pop("children", UNSET)
        children: list[ApiGeoTree] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ApiGeoTree.from_dict(children_item_data)

                children.append(children_item)

        api_geo_tree = cls(
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
            type_=type_,
            children=children,
        )

        api_geo_tree.additional_properties = d
        return api_geo_tree

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
