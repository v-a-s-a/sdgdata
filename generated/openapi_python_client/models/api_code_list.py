from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCodeList")


@_attrs_define
class ApiCodeList:
    """
    Attributes:
        code (str | Unset): Gets or Sets code
        description (str | Unset): Gets or Sets code
        sdmx (str | Unset): Gets or Sets code
    """

    code: str | Unset = UNSET
    description: str | Unset = UNSET
    sdmx: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        description = self.description

        sdmx = self.sdmx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if sdmx is not UNSET:
            field_dict["sdmx"] = sdmx

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        sdmx = d.pop("sdmx", UNSET)

        api_code_list = cls(
            code=code,
            description=description,
            sdmx=sdmx,
        )

        api_code_list.additional_properties = d
        return api_code_list

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
