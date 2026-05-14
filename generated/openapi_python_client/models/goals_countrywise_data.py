from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoalsCountrywiseData")


@_attrs_define
class GoalsCountrywiseData:
    """
    Attributes:
        geo_area_code (int | Unset):
        geo_area_name (str | Unset):
        goal1 (float | Unset):
        goal2 (float | Unset):
        goal3 (float | Unset):
        goal4 (float | Unset):
        goal5 (float | Unset):
        goal6 (float | Unset):
        goal7 (float | Unset):
        goal8 (float | Unset):
        goal9 (float | Unset):
        goal10 (float | Unset):
        goal11 (float | Unset):
        goal12 (float | Unset):
        goal13 (float | Unset):
        goal14 (float | Unset):
        goal15 (float | Unset):
        goal16 (float | Unset):
        goal17 (float | Unset):
    """

    geo_area_code: int | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    goal1: float | Unset = UNSET
    goal2: float | Unset = UNSET
    goal3: float | Unset = UNSET
    goal4: float | Unset = UNSET
    goal5: float | Unset = UNSET
    goal6: float | Unset = UNSET
    goal7: float | Unset = UNSET
    goal8: float | Unset = UNSET
    goal9: float | Unset = UNSET
    goal10: float | Unset = UNSET
    goal11: float | Unset = UNSET
    goal12: float | Unset = UNSET
    goal13: float | Unset = UNSET
    goal14: float | Unset = UNSET
    goal15: float | Unset = UNSET
    goal16: float | Unset = UNSET
    goal17: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        goal1 = self.goal1

        goal2 = self.goal2

        goal3 = self.goal3

        goal4 = self.goal4

        goal5 = self.goal5

        goal6 = self.goal6

        goal7 = self.goal7

        goal8 = self.goal8

        goal9 = self.goal9

        goal10 = self.goal10

        goal11 = self.goal11

        goal12 = self.goal12

        goal13 = self.goal13

        goal14 = self.goal14

        goal15 = self.goal15

        goal16 = self.goal16

        goal17 = self.goal17

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name
        if goal1 is not UNSET:
            field_dict["goal1"] = goal1
        if goal2 is not UNSET:
            field_dict["goal2"] = goal2
        if goal3 is not UNSET:
            field_dict["goal3"] = goal3
        if goal4 is not UNSET:
            field_dict["goal4"] = goal4
        if goal5 is not UNSET:
            field_dict["goal5"] = goal5
        if goal6 is not UNSET:
            field_dict["goal6"] = goal6
        if goal7 is not UNSET:
            field_dict["goal7"] = goal7
        if goal8 is not UNSET:
            field_dict["goal8"] = goal8
        if goal9 is not UNSET:
            field_dict["goal9"] = goal9
        if goal10 is not UNSET:
            field_dict["goal10"] = goal10
        if goal11 is not UNSET:
            field_dict["goal11"] = goal11
        if goal12 is not UNSET:
            field_dict["goal12"] = goal12
        if goal13 is not UNSET:
            field_dict["goal13"] = goal13
        if goal14 is not UNSET:
            field_dict["goal14"] = goal14
        if goal15 is not UNSET:
            field_dict["goal15"] = goal15
        if goal16 is not UNSET:
            field_dict["goal16"] = goal16
        if goal17 is not UNSET:
            field_dict["goal17"] = goal17

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        goal1 = d.pop("goal1", UNSET)

        goal2 = d.pop("goal2", UNSET)

        goal3 = d.pop("goal3", UNSET)

        goal4 = d.pop("goal4", UNSET)

        goal5 = d.pop("goal5", UNSET)

        goal6 = d.pop("goal6", UNSET)

        goal7 = d.pop("goal7", UNSET)

        goal8 = d.pop("goal8", UNSET)

        goal9 = d.pop("goal9", UNSET)

        goal10 = d.pop("goal10", UNSET)

        goal11 = d.pop("goal11", UNSET)

        goal12 = d.pop("goal12", UNSET)

        goal13 = d.pop("goal13", UNSET)

        goal14 = d.pop("goal14", UNSET)

        goal15 = d.pop("goal15", UNSET)

        goal16 = d.pop("goal16", UNSET)

        goal17 = d.pop("goal17", UNSET)

        goals_countrywise_data = cls(
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
            goal1=goal1,
            goal2=goal2,
            goal3=goal3,
            goal4=goal4,
            goal5=goal5,
            goal6=goal6,
            goal7=goal7,
            goal8=goal8,
            goal9=goal9,
            goal10=goal10,
            goal11=goal11,
            goal12=goal12,
            goal13=goal13,
            goal14=goal14,
            goal15=goal15,
            goal16=goal16,
            goal17=goal17,
        )

        goals_countrywise_data.additional_properties = d
        return goals_countrywise_data

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
