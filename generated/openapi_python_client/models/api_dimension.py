from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_code_list import ApiCodeList


T = TypeVar("T", bound="ApiDimension")


@_attrs_define
class ApiDimension:
    """
    Attributes:
        id (str | Unset): Gets or Sets id
        codes (list[ApiCodeList] | Unset): Gets or Sets codeList
    """

    id: str | Unset = UNSET
    codes: list[ApiCodeList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.codes, Unset):
            codes = []
            for codes_item_data in self.codes:
                codes_item = codes_item_data.to_dict()
                codes.append(codes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if codes is not UNSET:
            field_dict["codes"] = codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_code_list import ApiCodeList

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _codes = d.pop("codes", UNSET)
        codes: list[ApiCodeList] | Unset = UNSET
        if _codes is not UNSET:
            codes = []
            for codes_item_data in _codes:
                codes_item = ApiCodeList.from_dict(codes_item_data)

                codes.append(codes_item)

        api_dimension = cls(
            id=id,
            codes=codes,
        )

        api_dimension.additional_properties = d
        return api_dimension

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
