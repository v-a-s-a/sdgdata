from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_dimension import ApiDimension
    from ..models.api_observation_pivot import ApiObservationPivot


T = TypeVar("T", bound="ApiObservationPivotPage")


@_attrs_define
class ApiObservationPivotPage:
    """
    Attributes:
        size (int | Unset): Gets or Sets Size
            The number of elements in the page
        total_elements (int | Unset): Gets or Sets TotalElements
            The total number of elements
        total_pages (int | Unset): Gets or Sets totalPages
            The total number of pages
        page_number (int | Unset): Gets or Sets pageNumber
            The current page number
        attributes (list[ApiDimension] | Unset): Gets or Sets attributes
        dimensions (list[ApiDimension] | Unset): Gets or Sets dimensions
        data (list[ApiObservationPivot] | Unset): Gets or Sets data
    """

    size: int | Unset = UNSET
    total_elements: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    page_number: int | Unset = UNSET
    attributes: list[ApiDimension] | Unset = UNSET
    dimensions: list[ApiDimension] | Unset = UNSET
    data: list[ApiObservationPivot] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        total_elements = self.total_elements

        total_pages = self.total_pages

        page_number = self.page_number

        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        dimensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_dimension import ApiDimension
        from ..models.api_observation_pivot import ApiObservationPivot

        d = dict(src_dict)
        size = d.pop("size", UNSET)

        total_elements = d.pop("totalElements", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: list[ApiDimension] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = ApiDimension.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: list[ApiDimension] | Unset = UNSET
        if _dimensions is not UNSET:
            dimensions = []
            for dimensions_item_data in _dimensions:
                dimensions_item = ApiDimension.from_dict(dimensions_item_data)

                dimensions.append(dimensions_item)

        _data = d.pop("data", UNSET)
        data: list[ApiObservationPivot] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ApiObservationPivot.from_dict(data_item_data)

                data.append(data_item)

        api_observation_pivot_page = cls(
            size=size,
            total_elements=total_elements,
            total_pages=total_pages,
            page_number=page_number,
            attributes=attributes,
            dimensions=dimensions,
            data=data,
        )

        api_observation_pivot_page.additional_properties = d
        return api_observation_pivot_page

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
