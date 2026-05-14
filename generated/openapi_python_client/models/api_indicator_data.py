from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_serie_data import ApiSerieData


T = TypeVar("T", bound="ApiIndicatorData")


@_attrs_define
class ApiIndicatorData:
    """
    Attributes:
        code (str | Unset): Gets or Sets Code
        description (str | Unset): Gets or Sets Description
        tier (str | Unset): Gets or Sets Tier
        uri (str | Unset): Gets or Sets URI
        series (list[ApiSerieData] | Unset): Gets or Sets Series
    """

    code: str | Unset = UNSET
    description: str | Unset = UNSET
    tier: str | Unset = UNSET
    uri: str | Unset = UNSET
    series: list[ApiSerieData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        description = self.description

        tier = self.tier

        uri = self.uri

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if tier is not UNSET:
            field_dict["tier"] = tier
        if uri is not UNSET:
            field_dict["uri"] = uri
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_serie_data import ApiSerieData

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        tier = d.pop("tier", UNSET)

        uri = d.pop("uri", UNSET)

        _series = d.pop("series", UNSET)
        series: list[ApiSerieData] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = ApiSerieData.from_dict(series_item_data)

                series.append(series_item)

        api_indicator_data = cls(
            code=code,
            description=description,
            tier=tier,
            uri=uri,
            series=series,
        )

        api_indicator_data.additional_properties = d
        return api_indicator_data

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
