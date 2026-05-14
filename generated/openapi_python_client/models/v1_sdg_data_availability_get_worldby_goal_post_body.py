from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgDataAvailabilityGetWorldbyGoalPostBody")


@_attrs_define
class V1SdgDataAvailabilityGetWorldbyGoalPostBody:
    """
    Attributes:
        data_point_type (int): Data points for country (int) e.g 1 -Data for atleast 1 year since 2015,2-Data for
            atleast 2 years since 2015,3-Data for at least two years since 2015 and at least two years before 2015
        nature_of_data (str | Unset): Nature of data (string) e.g {'All':All,'C':Country Data,'CNA':Country data and
            adjusted country data}
    """

    data_point_type: int
    nature_of_data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_point_type = self.data_point_type

        nature_of_data = self.nature_of_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPointType": data_point_type,
            }
        )
        if nature_of_data is not UNSET:
            field_dict["natureOfData"] = nature_of_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_point_type = d.pop("dataPointType")

        nature_of_data = d.pop("natureOfData", UNSET)

        v1_sdg_data_availability_get_worldby_goal_post_body = cls(
            data_point_type=data_point_type,
            nature_of_data=nature_of_data,
        )

        v1_sdg_data_availability_get_worldby_goal_post_body.additional_properties = d
        return v1_sdg_data_availability_get_worldby_goal_post_body

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
