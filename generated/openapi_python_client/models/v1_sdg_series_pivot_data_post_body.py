from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgSeriesPivotDataPostBody")


@_attrs_define
class V1SdgSeriesPivotDataPostBody:
    """
    Attributes:
        series_code (list[str] | Unset): SDMX code for that series
        release_code (str | Unset): Code of the releases that we are querying
        area_code (list[int] | Unset): List of M49 values
        dimensions (str | Unset): Array of name - values eg: [{name:"Age",values:["15+","15-24"]}]
        page (int | Unset): Page number
        page_size (int | Unset): Number of records per page
    """

    series_code: list[str] | Unset = UNSET
    release_code: str | Unset = UNSET
    area_code: list[int] | Unset = UNSET
    dimensions: str | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_code: list[str] | Unset = UNSET
        if not isinstance(self.series_code, Unset):
            series_code = self.series_code

        release_code = self.release_code

        area_code: list[int] | Unset = UNSET
        if not isinstance(self.area_code, Unset):
            area_code = self.area_code

        dimensions = self.dimensions

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series_code is not UNSET:
            field_dict["seriesCode"] = series_code
        if release_code is not UNSET:
            field_dict["releaseCode"] = release_code
        if area_code is not UNSET:
            field_dict["areaCode"] = area_code
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series_code = cast(list[str], d.pop("seriesCode", UNSET))

        release_code = d.pop("releaseCode", UNSET)

        area_code = cast(list[int], d.pop("areaCode", UNSET))

        dimensions = d.pop("dimensions", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        v1_sdg_series_pivot_data_post_body = cls(
            series_code=series_code,
            release_code=release_code,
            area_code=area_code,
            dimensions=dimensions,
            page=page,
            page_size=page_size,
        )

        v1_sdg_series_pivot_data_post_body.additional_properties = d
        return v1_sdg_series_pivot_data_post_body

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
