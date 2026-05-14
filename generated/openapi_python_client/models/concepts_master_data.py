from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConceptsMasterData")


@_attrs_define
class ConceptsMasterData:
    """
    Attributes:
        concept_id (str | Unset):
        concept_name (str | Unset):
        parent_id (str | Unset):
    """

    concept_id: str | Unset = UNSET
    concept_name: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concept_id = self.concept_id

        concept_name = self.concept_name

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concept_id is not UNSET:
            field_dict["conceptId"] = concept_id
        if concept_name is not UNSET:
            field_dict["conceptName"] = concept_name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        concept_id = d.pop("conceptId", UNSET)

        concept_name = d.pop("conceptName", UNSET)

        parent_id = d.pop("parentId", UNSET)

        concepts_master_data = cls(
            concept_id=concept_id,
            concept_name=concept_name,
            parent_id=parent_id,
        )

        concepts_master_data.additional_properties = d
        return concepts_master_data

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
