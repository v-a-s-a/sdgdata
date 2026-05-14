from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.goals_countrywise_data import GoalsCountrywiseData
    from ..models.sdg_goals import SDGGoals


T = TypeVar("T", bound="ApiCountriesAcrossAllGoals")


@_attrs_define
class ApiCountriesAcrossAllGoals:
    """
    Attributes:
        goals (list[SDGGoals] | Unset):
        goals_country_details (list[GoalsCountrywiseData] | Unset):
    """

    goals: list[SDGGoals] | Unset = UNSET
    goals_country_details: list[GoalsCountrywiseData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goals, Unset):
            goals = []
            for goals_item_data in self.goals:
                goals_item = goals_item_data.to_dict()
                goals.append(goals_item)

        goals_country_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goals_country_details, Unset):
            goals_country_details = []
            for goals_country_details_item_data in self.goals_country_details:
                goals_country_details_item = goals_country_details_item_data.to_dict()
                goals_country_details.append(goals_country_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goals is not UNSET:
            field_dict["goals"] = goals
        if goals_country_details is not UNSET:
            field_dict["goalsCountryDetails"] = goals_country_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.goals_countrywise_data import GoalsCountrywiseData
        from ..models.sdg_goals import SDGGoals

        d = dict(src_dict)
        _goals = d.pop("goals", UNSET)
        goals: list[SDGGoals] | Unset = UNSET
        if _goals is not UNSET:
            goals = []
            for goals_item_data in _goals:
                goals_item = SDGGoals.from_dict(goals_item_data)

                goals.append(goals_item)

        _goals_country_details = d.pop("goalsCountryDetails", UNSET)
        goals_country_details: list[GoalsCountrywiseData] | Unset = UNSET
        if _goals_country_details is not UNSET:
            goals_country_details = []
            for goals_country_details_item_data in _goals_country_details:
                goals_country_details_item = GoalsCountrywiseData.from_dict(
                    goals_country_details_item_data
                )

                goals_country_details.append(goals_country_details_item)

        api_countries_across_all_goals = cls(
            goals=goals,
            goals_country_details=goals_country_details,
        )

        api_countries_across_all_goals.additional_properties = d
        return api_countries_across_all_goals

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
