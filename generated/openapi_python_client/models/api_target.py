from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_indicator import ApiIndicator


T = TypeVar("T", bound="ApiTarget")


@_attrs_define
class ApiTarget:
    """
    Attributes:
        goal (str | Unset): Gets or Sets Code
        code (str | Unset): Gets or Sets Code
        title (str | Unset): Gets or Sets Title
        description (str | Unset): Gets or Sets Description
        uri (str | Unset): Gets or Sets URI
        indicators (list[ApiIndicator] | Unset): Gets or Sets Indicators
    """

    goal: str | Unset = UNSET
    code: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    uri: str | Unset = UNSET
    indicators: list[ApiIndicator] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal = self.goal

        code = self.code

        title = self.title

        description = self.description

        uri = self.uri

        indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.indicators, Unset):
            indicators = []
            for indicators_item_data in self.indicators:
                indicators_item = indicators_item_data.to_dict()
                indicators.append(indicators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goal is not UNSET:
            field_dict["goal"] = goal
        if code is not UNSET:
            field_dict["code"] = code
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if uri is not UNSET:
            field_dict["uri"] = uri
        if indicators is not UNSET:
            field_dict["indicators"] = indicators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_indicator import ApiIndicator

        d = dict(src_dict)
        goal = d.pop("goal", UNSET)

        code = d.pop("code", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        uri = d.pop("uri", UNSET)

        _indicators = d.pop("indicators", UNSET)
        indicators: list[ApiIndicator] | Unset = UNSET
        if _indicators is not UNSET:
            indicators = []
            for indicators_item_data in _indicators:
                indicators_item = ApiIndicator.from_dict(indicators_item_data)

                indicators.append(indicators_item)

        api_target = cls(
            goal=goal,
            code=code,
            title=title,
            description=description,
            uri=uri,
            indicators=indicators,
        )

        api_target.additional_properties = d
        return api_target

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
