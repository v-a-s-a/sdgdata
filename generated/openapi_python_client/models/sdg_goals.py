from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SDGGoals")


@_attrs_define
class SDGGoals:
    """
    Attributes:
        goal_id (int | Unset):
        goal_name (str | Unset):
    """

    goal_id: int | Unset = UNSET
    goal_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_id = self.goal_id

        goal_name = self.goal_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goal_id is not UNSET:
            field_dict["goalId"] = goal_id
        if goal_name is not UNSET:
            field_dict["goalName"] = goal_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal_id = d.pop("goalId", UNSET)

        goal_name = d.pop("goalName", UNSET)

        sdg_goals = cls(
            goal_id=goal_id,
            goal_name=goal_name,
        )

        sdg_goals.additional_properties = d
        return sdg_goals

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
