from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_indicator_percentage import ApiIndicatorPercentage


T = TypeVar("T", bound="ApiCompareIndicatorsAcrossCountries")


@_attrs_define
class ApiCompareIndicatorsAcrossCountries:
    """
    Attributes:
        goal_id (str | Unset):
        goal_name (str | Unset):
        indicators (list[ApiIndicatorPercentage] | Unset):
    """

    goal_id: str | Unset = UNSET
    goal_name: str | Unset = UNSET
    indicators: list[ApiIndicatorPercentage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_id = self.goal_id

        goal_name = self.goal_name

        indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.indicators, Unset):
            indicators = []
            for indicators_item_data in self.indicators:
                indicators_item = indicators_item_data.to_dict()
                indicators.append(indicators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goal_id is not UNSET:
            field_dict["goalId"] = goal_id
        if goal_name is not UNSET:
            field_dict["goalName"] = goal_name
        if indicators is not UNSET:
            field_dict["indicators"] = indicators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_indicator_percentage import ApiIndicatorPercentage

        d = dict(src_dict)
        goal_id = d.pop("goalId", UNSET)

        goal_name = d.pop("goalName", UNSET)

        _indicators = d.pop("indicators", UNSET)
        indicators: list[ApiIndicatorPercentage] | Unset = UNSET
        if _indicators is not UNSET:
            indicators = []
            for indicators_item_data in _indicators:
                indicators_item = ApiIndicatorPercentage.from_dict(indicators_item_data)

                indicators.append(indicators_item)

        api_compare_indicators_across_countries = cls(
            goal_id=goal_id,
            goal_name=goal_name,
            indicators=indicators,
        )

        api_compare_indicators_across_countries.additional_properties = d
        return api_compare_indicators_across_countries

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
