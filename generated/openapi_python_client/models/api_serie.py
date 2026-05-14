from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSerie")


@_attrs_define
class ApiSerie:
    """
    Attributes:
        goal (list[str] | Unset): Gets or Sets Goal
        target (list[str] | Unset): Gets or Sets Target
        indicator (list[str] | Unset): Gets or Sets Indicator
        release (str | Unset): Gets or Sets Release
        code (str | Unset): Gets or Sets Code
        description (str | Unset): Gets or Sets Description
        uri (str | Unset): Gets or Sets URI
    """

    goal: list[str] | Unset = UNSET
    target: list[str] | Unset = UNSET
    indicator: list[str] | Unset = UNSET
    release: str | Unset = UNSET
    code: str | Unset = UNSET
    description: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal: list[str] | Unset = UNSET
        if not isinstance(self.goal, Unset):
            goal = self.goal

        target: list[str] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target

        indicator: list[str] | Unset = UNSET
        if not isinstance(self.indicator, Unset):
            indicator = self.indicator

        release = self.release

        code = self.code

        description = self.description

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goal is not UNSET:
            field_dict["goal"] = goal
        if target is not UNSET:
            field_dict["target"] = target
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if release is not UNSET:
            field_dict["release"] = release
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal = cast(list[str], d.pop("goal", UNSET))

        target = cast(list[str], d.pop("target", UNSET))

        indicator = cast(list[str], d.pop("indicator", UNSET))

        release = d.pop("release", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        uri = d.pop("uri", UNSET)

        api_serie = cls(
            goal=goal,
            target=target,
            indicator=indicator,
            release=release,
            code=code,
            description=description,
            uri=uri,
        )

        api_serie.additional_properties = d
        return api_serie

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
