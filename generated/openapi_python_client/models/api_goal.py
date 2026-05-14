from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_target import ApiTarget


T = TypeVar("T", bound="ApiGoal")


@_attrs_define
class ApiGoal:
    """
    Attributes:
        code (str | Unset): Gets or Sets Code
        title (str | Unset): Gets or Sets Title
        description (str | Unset): Gets or Sets Description
        uri (str | Unset): Gets or Sets URI
        targets (list[ApiTarget] | Unset): Gets or Sets Targets
    """

    code: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    uri: str | Unset = UNSET
    targets: list[ApiTarget] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        title = self.title

        description = self.description

        uri = self.uri

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if uri is not UNSET:
            field_dict["uri"] = uri
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_target import ApiTarget

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        uri = d.pop("uri", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[ApiTarget] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = ApiTarget.from_dict(targets_item_data)

                targets.append(targets_item)

        api_goal = cls(
            code=code,
            title=title,
            description=description,
            uri=uri,
            targets=targets,
        )

        api_goal.additional_properties = d
        return api_goal

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
