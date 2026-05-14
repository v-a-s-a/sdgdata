from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SDMXMetaDataResponse")


@_attrs_define
class SDMXMetaDataResponse:
    """
    Attributes:
        series (str | Unset):
        series_desc (str | Unset):
        indicator_desc (str | Unset):
        concept_id (str | Unset):
        concept_name (str | Unset):
        concept_desc (str | Unset):
        concept_html (str | Unset):
        parent_id (str | Unset):
    """

    series: str | Unset = UNSET
    series_desc: str | Unset = UNSET
    indicator_desc: str | Unset = UNSET
    concept_id: str | Unset = UNSET
    concept_name: str | Unset = UNSET
    concept_desc: str | Unset = UNSET
    concept_html: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series = self.series

        series_desc = self.series_desc

        indicator_desc = self.indicator_desc

        concept_id = self.concept_id

        concept_name = self.concept_name

        concept_desc = self.concept_desc

        concept_html = self.concept_html

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series is not UNSET:
            field_dict["series"] = series
        if series_desc is not UNSET:
            field_dict["seriesDesc"] = series_desc
        if indicator_desc is not UNSET:
            field_dict["indicatorDesc"] = indicator_desc
        if concept_id is not UNSET:
            field_dict["conceptId"] = concept_id
        if concept_name is not UNSET:
            field_dict["conceptName"] = concept_name
        if concept_desc is not UNSET:
            field_dict["conceptDesc"] = concept_desc
        if concept_html is not UNSET:
            field_dict["conceptHTML"] = concept_html
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series = d.pop("series", UNSET)

        series_desc = d.pop("seriesDesc", UNSET)

        indicator_desc = d.pop("indicatorDesc", UNSET)

        concept_id = d.pop("conceptId", UNSET)

        concept_name = d.pop("conceptName", UNSET)

        concept_desc = d.pop("conceptDesc", UNSET)

        concept_html = d.pop("conceptHTML", UNSET)

        parent_id = d.pop("parentId", UNSET)

        sdmx_meta_data_response = cls(
            series=series,
            series_desc=series_desc,
            indicator_desc=indicator_desc,
            concept_id=concept_id,
            concept_name=concept_name,
            concept_desc=concept_desc,
            concept_html=concept_html,
            parent_id=parent_id,
        )

        sdmx_meta_data_response.additional_properties = d
        return sdmx_meta_data_response

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
