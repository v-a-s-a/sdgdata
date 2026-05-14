from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stream")


@_attrs_define
class Stream:
    """
    Attributes:
        can_read (bool | Unset):
        can_seek (bool | Unset):
        can_timeout (bool | Unset):
        can_write (bool | Unset):
        length (int | Unset):
        position (int | Unset):
        read_timeout (int | Unset):
        write_timeout (int | Unset):
    """

    can_read: bool | Unset = UNSET
    can_seek: bool | Unset = UNSET
    can_timeout: bool | Unset = UNSET
    can_write: bool | Unset = UNSET
    length: int | Unset = UNSET
    position: int | Unset = UNSET
    read_timeout: int | Unset = UNSET
    write_timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_read = self.can_read

        can_seek = self.can_seek

        can_timeout = self.can_timeout

        can_write = self.can_write

        length = self.length

        position = self.position

        read_timeout = self.read_timeout

        write_timeout = self.write_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_read is not UNSET:
            field_dict["canRead"] = can_read
        if can_seek is not UNSET:
            field_dict["canSeek"] = can_seek
        if can_timeout is not UNSET:
            field_dict["canTimeout"] = can_timeout
        if can_write is not UNSET:
            field_dict["canWrite"] = can_write
        if length is not UNSET:
            field_dict["length"] = length
        if position is not UNSET:
            field_dict["position"] = position
        if read_timeout is not UNSET:
            field_dict["readTimeout"] = read_timeout
        if write_timeout is not UNSET:
            field_dict["writeTimeout"] = write_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_read = d.pop("canRead", UNSET)

        can_seek = d.pop("canSeek", UNSET)

        can_timeout = d.pop("canTimeout", UNSET)

        can_write = d.pop("canWrite", UNSET)

        length = d.pop("length", UNSET)

        position = d.pop("position", UNSET)

        read_timeout = d.pop("readTimeout", UNSET)

        write_timeout = d.pop("writeTimeout", UNSET)

        stream = cls(
            can_read=can_read,
            can_seek=can_seek,
            can_timeout=can_timeout,
            can_write=can_write,
            length=length,
            position=position,
            read_timeout=read_timeout,
            write_timeout=write_timeout,
        )

        stream.additional_properties = d
        return stream

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
