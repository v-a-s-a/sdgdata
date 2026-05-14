from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_countrywise_data import ApiCountrywiseData


T = TypeVar("T", bound="ApiOneSeriesMultiArea")


@_attrs_define
class ApiOneSeriesMultiArea:
    """
    Attributes:
        indicator (str | Unset):
        series_code (str | Unset):
        series_title (str | Unset):
        disaggregation_type (str | Unset):
        units (str | Unset):
        country_data (list[ApiCountrywiseData] | Unset):
    """

    indicator: str | Unset = UNSET
    series_code: str | Unset = UNSET
    series_title: str | Unset = UNSET
    disaggregation_type: str | Unset = UNSET
    units: str | Unset = UNSET
    country_data: list[ApiCountrywiseData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indicator = self.indicator

        series_code = self.series_code

        series_title = self.series_title

        disaggregation_type = self.disaggregation_type

        units = self.units

        country_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.country_data, Unset):
            country_data = []
            for country_data_item_data in self.country_data:
                country_data_item = country_data_item_data.to_dict()
                country_data.append(country_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if series_code is not UNSET:
            field_dict["seriesCode"] = series_code
        if series_title is not UNSET:
            field_dict["seriesTitle"] = series_title
        if disaggregation_type is not UNSET:
            field_dict["disaggregationType"] = disaggregation_type
        if units is not UNSET:
            field_dict["units"] = units
        if country_data is not UNSET:
            field_dict["countryData"] = country_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_countrywise_data import ApiCountrywiseData

        d = dict(src_dict)
        indicator = d.pop("indicator", UNSET)

        series_code = d.pop("seriesCode", UNSET)

        series_title = d.pop("seriesTitle", UNSET)

        disaggregation_type = d.pop("disaggregationType", UNSET)

        units = d.pop("units", UNSET)

        _country_data = d.pop("countryData", UNSET)
        country_data: list[ApiCountrywiseData] | Unset = UNSET
        if _country_data is not UNSET:
            country_data = []
            for country_data_item_data in _country_data:
                country_data_item = ApiCountrywiseData.from_dict(country_data_item_data)

                country_data.append(country_data_item)

        api_one_series_multi_area = cls(
            indicator=indicator,
            series_code=series_code,
            series_title=series_title,
            disaggregation_type=disaggregation_type,
            units=units,
            country_data=country_data,
        )

        api_one_series_multi_area.additional_properties = d
        return api_one_series_multi_area

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
