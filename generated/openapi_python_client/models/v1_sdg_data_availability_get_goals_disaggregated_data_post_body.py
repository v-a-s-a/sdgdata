from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgDataAvailabilityGetGoalsDisaggregatedDataPostBody")


@_attrs_define
class V1SdgDataAvailabilityGetGoalsDisaggregatedDataPostBody:
    """
    Attributes:
        data_point_type (int): Data points for country (int) e.g 1 -Data for atleast 1 year since 2015,2-Data for
            atleast 2 years since 2015,3-Data for at least two years since 2015 and at least two years before 2015
        area_code (str | Unset): Array of region ids e.g [343,353]
        nature_of_data (str | Unset): Nature of data (string) e.g {'All':All,'C':Country Data,'CNA':Country data and
            adjusted country data}
        disaggregation_type (int | Unset): Disaggregation type (int). e.g 0 : Any type of disaggregation.
    """

    data_point_type: int
    area_code: str | Unset = UNSET
    nature_of_data: str | Unset = UNSET
    disaggregation_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_point_type = self.data_point_type

        area_code = self.area_code

        nature_of_data = self.nature_of_data

        disaggregation_type = self.disaggregation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPointType": data_point_type,
            }
        )
        if area_code is not UNSET:
            field_dict["areaCode"] = area_code
        if nature_of_data is not UNSET:
            field_dict["natureOfData"] = nature_of_data
        if disaggregation_type is not UNSET:
            field_dict["disaggregationType"] = disaggregation_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_point_type = d.pop("dataPointType")

        area_code = d.pop("areaCode", UNSET)

        nature_of_data = d.pop("natureOfData", UNSET)

        disaggregation_type = d.pop("disaggregationType", UNSET)

        v1_sdg_data_availability_get_goals_disaggregated_data_post_body = cls(
            data_point_type=data_point_type,
            area_code=area_code,
            nature_of_data=nature_of_data,
            disaggregation_type=disaggregation_type,
        )

        v1_sdg_data_availability_get_goals_disaggregated_data_post_body.additional_properties = d
        return v1_sdg_data_availability_get_goals_disaggregated_data_post_body

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
