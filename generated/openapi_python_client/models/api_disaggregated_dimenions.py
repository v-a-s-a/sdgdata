from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDisaggregatedDimenions")


@_attrs_define
class ApiDisaggregatedDimenions:
    """
    Attributes:
        id (str | Unset):
        goal (int | Unset):
        target (str | Unset):
        indicator (str | Unset):
        series_code (str | Unset):
        disaggregated_category (str | Unset):
    """

    id: str | Unset = UNSET
    goal: int | Unset = UNSET
    target: str | Unset = UNSET
    indicator: str | Unset = UNSET
    series_code: str | Unset = UNSET
    disaggregated_category: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        goal = self.goal

        target = self.target

        indicator = self.indicator

        series_code = self.series_code

        disaggregated_category = self.disaggregated_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if goal is not UNSET:
            field_dict["goal"] = goal
        if target is not UNSET:
            field_dict["target"] = target
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if series_code is not UNSET:
            field_dict["seriesCode"] = series_code
        if disaggregated_category is not UNSET:
            field_dict["disaggregatedCategory"] = disaggregated_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        goal = d.pop("goal", UNSET)

        target = d.pop("target", UNSET)

        indicator = d.pop("indicator", UNSET)

        series_code = d.pop("seriesCode", UNSET)

        disaggregated_category = d.pop("disaggregatedCategory", UNSET)

        api_disaggregated_dimenions = cls(
            id=id,
            goal=goal,
            target=target,
            indicator=indicator,
            series_code=series_code,
            disaggregated_category=disaggregated_category,
        )

        api_disaggregated_dimenions.additional_properties = d
        return api_disaggregated_dimenions

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
