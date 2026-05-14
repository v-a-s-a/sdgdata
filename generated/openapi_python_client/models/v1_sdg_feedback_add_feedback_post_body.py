from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SdgFeedbackAddFeedbackPostBody")


@_attrs_define
class V1SdgFeedbackAddFeedbackPostBody:
    """
    Attributes:
        feedback_type (int): Feedback type (int) e.g 1 - Comments,2 - Questions
        feedback_description (str | Unset): Can be any text
        first_name (str | Unset): Name of the person
        last_name (str | Unset): Name of the person
        email (str | Unset): Email ID of the person
        feedback_page (str | Unset): This tells the feedback is for which Page e.g Home Or DataAvailability
    """

    feedback_type: int
    feedback_description: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    feedback_page: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feedback_type = self.feedback_type

        feedback_description = self.feedback_description

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        feedback_page = self.feedback_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedbackType": feedback_type,
            }
        )
        if feedback_description is not UNSET:
            field_dict["feedbackDescription"] = feedback_description
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if feedback_page is not UNSET:
            field_dict["feedbackPage"] = feedback_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feedback_type = d.pop("feedbackType")

        feedback_description = d.pop("feedbackDescription", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        feedback_page = d.pop("feedbackPage", UNSET)

        v1_sdg_feedback_add_feedback_post_body = cls(
            feedback_type=feedback_type,
            feedback_description=feedback_description,
            first_name=first_name,
            last_name=last_name,
            email=email,
            feedback_page=feedback_page,
        )

        v1_sdg_feedback_add_feedback_post_body.additional_properties = d
        return v1_sdg_feedback_add_feedback_post_body

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
