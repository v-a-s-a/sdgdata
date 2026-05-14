from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_observation import ApiObservation


T = TypeVar("T", bound="ApiSerieData")


@_attrs_define
class ApiSerieData:
    """
    Attributes:
        release (str | Unset): Gets or Sets Series
        code (str | Unset):
        description (str | Unset): Gets or Sets Description
        uri (str | Unset): Gets or Sets URI
        observations (list[ApiObservation] | Unset): Gets or Sets attributes
    """

    release: str | Unset = UNSET
    code: str | Unset = UNSET
    description: str | Unset = UNSET
    uri: str | Unset = UNSET
    observations: list[ApiObservation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release = self.release

        code = self.code

        description = self.description

        uri = self.uri

        observations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.observations, Unset):
            observations = []
            for observations_item_data in self.observations:
                observations_item = observations_item_data.to_dict()
                observations.append(observations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if release is not UNSET:
            field_dict["release"] = release
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if uri is not UNSET:
            field_dict["uri"] = uri
        if observations is not UNSET:
            field_dict["observations"] = observations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_observation import ApiObservation

        d = dict(src_dict)
        release = d.pop("release", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        uri = d.pop("uri", UNSET)

        _observations = d.pop("observations", UNSET)
        observations: list[ApiObservation] | Unset = UNSET
        if _observations is not UNSET:
            observations = []
            for observations_item_data in _observations:
                observations_item = ApiObservation.from_dict(observations_item_data)

                observations.append(observations_item)

        api_serie_data = cls(
            release=release,
            code=code,
            description=description,
            uri=uri,
            observations=observations,
        )

        api_serie_data.additional_properties = d
        return api_serie_data

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
