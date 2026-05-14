from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgGoalDataExcelPostBody")


@_attrs_define
class V1SdgGoalDataExcelPostBody:
    """
    Attributes:
        goal (list[int] | Unset): SDMX code for that goals
        area_codes (list[int] | Unset): List of M49 values
        time_period_start (float | Unset): Time series start point
        time_period_end (float | Unset): Tine sertues end point
    """

    goal: list[int] | Unset = UNSET
    area_codes: list[int] | Unset = UNSET
    time_period_start: float | Unset = UNSET
    time_period_end: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal: list[int] | Unset = UNSET
        if not isinstance(self.goal, Unset):
            goal = self.goal

        area_codes: list[int] | Unset = UNSET
        if not isinstance(self.area_codes, Unset):
            area_codes = self.area_codes

        time_period_start = self.time_period_start

        time_period_end = self.time_period_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goal is not UNSET:
            field_dict["goal"] = goal
        if area_codes is not UNSET:
            field_dict["areaCodes"] = area_codes
        if time_period_start is not UNSET:
            field_dict["timePeriodStart"] = time_period_start
        if time_period_end is not UNSET:
            field_dict["timePeriodEnd"] = time_period_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal = cast(list[int], d.pop("goal", UNSET))

        area_codes = cast(list[int], d.pop("areaCodes", UNSET))

        time_period_start = d.pop("timePeriodStart", UNSET)

        time_period_end = d.pop("timePeriodEnd", UNSET)

        v1_sdg_goal_data_excel_post_body = cls(
            goal=goal,
            area_codes=area_codes,
            time_period_start=time_period_start,
            time_period_end=time_period_end,
        )

        v1_sdg_goal_data_excel_post_body.additional_properties = d
        return v1_sdg_goal_data_excel_post_body

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
