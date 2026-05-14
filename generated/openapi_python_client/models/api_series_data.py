from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_year_wise_data import ApiYearWiseData


T = TypeVar("T", bound="ApiSeriesData")


@_attrs_define
class ApiSeriesData:
    """
    Attributes:
        indicator (str | Unset):
        series_code (str | Unset):
        series_title (str | Unset):
        disaggregation_type (str | Unset):
        units (str | Unset):
        chart_color (str | Unset):
        year_wise_data (list[ApiYearWiseData] | Unset):
    """

    indicator: str | Unset = UNSET
    series_code: str | Unset = UNSET
    series_title: str | Unset = UNSET
    disaggregation_type: str | Unset = UNSET
    units: str | Unset = UNSET
    chart_color: str | Unset = UNSET
    year_wise_data: list[ApiYearWiseData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indicator = self.indicator

        series_code = self.series_code

        series_title = self.series_title

        disaggregation_type = self.disaggregation_type

        units = self.units

        chart_color = self.chart_color

        year_wise_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.year_wise_data, Unset):
            year_wise_data = []
            for year_wise_data_item_data in self.year_wise_data:
                year_wise_data_item = year_wise_data_item_data.to_dict()
                year_wise_data.append(year_wise_data_item)

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
        if chart_color is not UNSET:
            field_dict["chartColor"] = chart_color
        if year_wise_data is not UNSET:
            field_dict["yearWiseData"] = year_wise_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_year_wise_data import ApiYearWiseData

        d = dict(src_dict)
        indicator = d.pop("indicator", UNSET)

        series_code = d.pop("seriesCode", UNSET)

        series_title = d.pop("seriesTitle", UNSET)

        disaggregation_type = d.pop("disaggregationType", UNSET)

        units = d.pop("units", UNSET)

        chart_color = d.pop("chartColor", UNSET)

        _year_wise_data = d.pop("yearWiseData", UNSET)
        year_wise_data: list[ApiYearWiseData] | Unset = UNSET
        if _year_wise_data is not UNSET:
            year_wise_data = []
            for year_wise_data_item_data in _year_wise_data:
                year_wise_data_item = ApiYearWiseData.from_dict(
                    year_wise_data_item_data
                )

                year_wise_data.append(year_wise_data_item)

        api_series_data = cls(
            indicator=indicator,
            series_code=series_code,
            series_title=series_title,
            disaggregation_type=disaggregation_type,
            units=units,
            chart_color=chart_color,
            year_wise_data=year_wise_data,
        )

        api_series_data.additional_properties = d
        return api_series_data

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
