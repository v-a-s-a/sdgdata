from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiObservationPivot")


@_attrs_define
class ApiObservationPivot:
    """
    Attributes:
        goal (str | Unset): Gets or Sets Goal
        target (str | Unset): Gets or Sets Target
        indicator (str | Unset): Gets or Sets Indicator
        series (str | Unset): Gets or Sets Series
        series_description (str | Unset): Gets or Sets Series
        series_count (str | Unset): Gets or Sets Series
        geo_area_code (str | Unset): Gets or Sets geoAreaCode
        geo_area_name (str | Unset): Gets or Sets geoAreaName
        time_coverage (str | Unset): Gets or Sets TimeCoverage
        upper_bound (str | Unset): Gets or Sets UpperBound
        lower_bound (str | Unset): Gets or Sets LowerBound
        base_period (str | Unset): Gets or Sets BasePeriod
        source (str | Unset): Gets or Sets Source
        geo_info_url (str | Unset): Gets or Sets GeoInfoUrl
        age (str | Unset): Gets or Sets age
        freq (str | Unset): Gets or Sets freq
        sex (str | Unset): Gets or Sets sex
        location (str | Unset): Gets or Sets location
        units (str | Unset): Gets or Sets Units
        level_status (str | Unset): Gets or Sets level/status
        name_of_international_agreement (str | Unset): Gets or Sets name of international agreement
        education_level (str | Unset): Gets or Sets education level
        type_of_product (str | Unset): Gets or Sets type of product
        type_of_facilities (str | Unset): Gets or Sets type of facilities
        name_of_international_institution (str | Unset): Gets or Sets name of international institution
        type_of_occupation (str | Unset): Gets or Sets type of occupation
        tariff_regime_status (str | Unset): Gets or Sets tariff regime status
        mode_of_transportation (str | Unset): Gets or Sets mode of transportation
        type_of_mobile_technology (str | Unset): Gets or Sets type of mobile technology
        name_of_non_communicable_disease (str | Unset): Gets or Sets name of non-communicable disease
        type_of_skill (str | Unset): Gets or Sets type of skill
        type_of_speed (str | Unset): Gets or Sets type of speed
        migratory_status (str | Unset): Gets or Sets migratory status
        disability_status (str | Unset): Gets or Sets disability status
        hazard_type (str | Unset): Gets or Sets hazard type
        ihr_capacity (str | Unset): Gets or Sets ihr capacity
        reporting_type (str | Unset): Gets or Sets Units
        cities (str | Unset): Gets or Sets cities
        activity (str | Unset): Gets or Sets Activity
        policy_domains (str | Unset): Gets or Sets Policy Domains
        years (str | Unset): Gets or Sets years
    """

    goal: str | Unset = UNSET
    target: str | Unset = UNSET
    indicator: str | Unset = UNSET
    series: str | Unset = UNSET
    series_description: str | Unset = UNSET
    series_count: str | Unset = UNSET
    geo_area_code: str | Unset = UNSET
    geo_area_name: str | Unset = UNSET
    time_coverage: str | Unset = UNSET
    upper_bound: str | Unset = UNSET
    lower_bound: str | Unset = UNSET
    base_period: str | Unset = UNSET
    source: str | Unset = UNSET
    geo_info_url: str | Unset = UNSET
    age: str | Unset = UNSET
    freq: str | Unset = UNSET
    sex: str | Unset = UNSET
    location: str | Unset = UNSET
    units: str | Unset = UNSET
    level_status: str | Unset = UNSET
    name_of_international_agreement: str | Unset = UNSET
    education_level: str | Unset = UNSET
    type_of_product: str | Unset = UNSET
    type_of_facilities: str | Unset = UNSET
    name_of_international_institution: str | Unset = UNSET
    type_of_occupation: str | Unset = UNSET
    tariff_regime_status: str | Unset = UNSET
    mode_of_transportation: str | Unset = UNSET
    type_of_mobile_technology: str | Unset = UNSET
    name_of_non_communicable_disease: str | Unset = UNSET
    type_of_skill: str | Unset = UNSET
    type_of_speed: str | Unset = UNSET
    migratory_status: str | Unset = UNSET
    disability_status: str | Unset = UNSET
    hazard_type: str | Unset = UNSET
    ihr_capacity: str | Unset = UNSET
    reporting_type: str | Unset = UNSET
    cities: str | Unset = UNSET
    activity: str | Unset = UNSET
    policy_domains: str | Unset = UNSET
    years: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal = self.goal

        target = self.target

        indicator = self.indicator

        series = self.series

        series_description = self.series_description

        series_count = self.series_count

        geo_area_code = self.geo_area_code

        geo_area_name = self.geo_area_name

        time_coverage = self.time_coverage

        upper_bound = self.upper_bound

        lower_bound = self.lower_bound

        base_period = self.base_period

        source = self.source

        geo_info_url = self.geo_info_url

        age = self.age

        freq = self.freq

        sex = self.sex

        location = self.location

        units = self.units

        level_status = self.level_status

        name_of_international_agreement = self.name_of_international_agreement

        education_level = self.education_level

        type_of_product = self.type_of_product

        type_of_facilities = self.type_of_facilities

        name_of_international_institution = self.name_of_international_institution

        type_of_occupation = self.type_of_occupation

        tariff_regime_status = self.tariff_regime_status

        mode_of_transportation = self.mode_of_transportation

        type_of_mobile_technology = self.type_of_mobile_technology

        name_of_non_communicable_disease = self.name_of_non_communicable_disease

        type_of_skill = self.type_of_skill

        type_of_speed = self.type_of_speed

        migratory_status = self.migratory_status

        disability_status = self.disability_status

        hazard_type = self.hazard_type

        ihr_capacity = self.ihr_capacity

        reporting_type = self.reporting_type

        cities = self.cities

        activity = self.activity

        policy_domains = self.policy_domains

        years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goal is not UNSET:
            field_dict["goal"] = goal
        if target is not UNSET:
            field_dict["target"] = target
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if series is not UNSET:
            field_dict["series"] = series
        if series_description is not UNSET:
            field_dict["seriesDescription"] = series_description
        if series_count is not UNSET:
            field_dict["seriesCount"] = series_count
        if geo_area_code is not UNSET:
            field_dict["geoAreaCode"] = geo_area_code
        if geo_area_name is not UNSET:
            field_dict["geoAreaName"] = geo_area_name
        if time_coverage is not UNSET:
            field_dict["timeCoverage"] = time_coverage
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if base_period is not UNSET:
            field_dict["basePeriod"] = base_period
        if source is not UNSET:
            field_dict["source"] = source
        if geo_info_url is not UNSET:
            field_dict["geoInfoUrl"] = geo_info_url
        if age is not UNSET:
            field_dict["age"] = age
        if freq is not UNSET:
            field_dict["freq"] = freq
        if sex is not UNSET:
            field_dict["sex"] = sex
        if location is not UNSET:
            field_dict["location"] = location
        if units is not UNSET:
            field_dict["units"] = units
        if level_status is not UNSET:
            field_dict["level_status"] = level_status
        if name_of_international_agreement is not UNSET:
            field_dict["name_of_international_agreement"] = (
                name_of_international_agreement
            )
        if education_level is not UNSET:
            field_dict["education_level"] = education_level
        if type_of_product is not UNSET:
            field_dict["type_of_product"] = type_of_product
        if type_of_facilities is not UNSET:
            field_dict["type_of_facilities"] = type_of_facilities
        if name_of_international_institution is not UNSET:
            field_dict["name_of_international_institution"] = (
                name_of_international_institution
            )
        if type_of_occupation is not UNSET:
            field_dict["type_of_occupation"] = type_of_occupation
        if tariff_regime_status is not UNSET:
            field_dict["tariff_regime_status"] = tariff_regime_status
        if mode_of_transportation is not UNSET:
            field_dict["mode_of_transportation"] = mode_of_transportation
        if type_of_mobile_technology is not UNSET:
            field_dict["type_of_mobile_technology"] = type_of_mobile_technology
        if name_of_non_communicable_disease is not UNSET:
            field_dict["name_of_non_communicable_disease"] = (
                name_of_non_communicable_disease
            )
        if type_of_skill is not UNSET:
            field_dict["type_of_skill"] = type_of_skill
        if type_of_speed is not UNSET:
            field_dict["type_of_speed"] = type_of_speed
        if migratory_status is not UNSET:
            field_dict["migratory_status"] = migratory_status
        if disability_status is not UNSET:
            field_dict["disability_status"] = disability_status
        if hazard_type is not UNSET:
            field_dict["hazard_type"] = hazard_type
        if ihr_capacity is not UNSET:
            field_dict["ihr_capacity"] = ihr_capacity
        if reporting_type is not UNSET:
            field_dict["reporting_type"] = reporting_type
        if cities is not UNSET:
            field_dict["cities"] = cities
        if activity is not UNSET:
            field_dict["activity"] = activity
        if policy_domains is not UNSET:
            field_dict["policy_domains"] = policy_domains
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal = d.pop("goal", UNSET)

        target = d.pop("target", UNSET)

        indicator = d.pop("indicator", UNSET)

        series = d.pop("series", UNSET)

        series_description = d.pop("seriesDescription", UNSET)

        series_count = d.pop("seriesCount", UNSET)

        geo_area_code = d.pop("geoAreaCode", UNSET)

        geo_area_name = d.pop("geoAreaName", UNSET)

        time_coverage = d.pop("timeCoverage", UNSET)

        upper_bound = d.pop("upperBound", UNSET)

        lower_bound = d.pop("lowerBound", UNSET)

        base_period = d.pop("basePeriod", UNSET)

        source = d.pop("source", UNSET)

        geo_info_url = d.pop("geoInfoUrl", UNSET)

        age = d.pop("age", UNSET)

        freq = d.pop("freq", UNSET)

        sex = d.pop("sex", UNSET)

        location = d.pop("location", UNSET)

        units = d.pop("units", UNSET)

        level_status = d.pop("level_status", UNSET)

        name_of_international_agreement = d.pop(
            "name_of_international_agreement", UNSET
        )

        education_level = d.pop("education_level", UNSET)

        type_of_product = d.pop("type_of_product", UNSET)

        type_of_facilities = d.pop("type_of_facilities", UNSET)

        name_of_international_institution = d.pop(
            "name_of_international_institution", UNSET
        )

        type_of_occupation = d.pop("type_of_occupation", UNSET)

        tariff_regime_status = d.pop("tariff_regime_status", UNSET)

        mode_of_transportation = d.pop("mode_of_transportation", UNSET)

        type_of_mobile_technology = d.pop("type_of_mobile_technology", UNSET)

        name_of_non_communicable_disease = d.pop(
            "name_of_non_communicable_disease", UNSET
        )

        type_of_skill = d.pop("type_of_skill", UNSET)

        type_of_speed = d.pop("type_of_speed", UNSET)

        migratory_status = d.pop("migratory_status", UNSET)

        disability_status = d.pop("disability_status", UNSET)

        hazard_type = d.pop("hazard_type", UNSET)

        ihr_capacity = d.pop("ihr_capacity", UNSET)

        reporting_type = d.pop("reporting_type", UNSET)

        cities = d.pop("cities", UNSET)

        activity = d.pop("activity", UNSET)

        policy_domains = d.pop("policy_domains", UNSET)

        years = d.pop("years", UNSET)

        api_observation_pivot = cls(
            goal=goal,
            target=target,
            indicator=indicator,
            series=series,
            series_description=series_description,
            series_count=series_count,
            geo_area_code=geo_area_code,
            geo_area_name=geo_area_name,
            time_coverage=time_coverage,
            upper_bound=upper_bound,
            lower_bound=lower_bound,
            base_period=base_period,
            source=source,
            geo_info_url=geo_info_url,
            age=age,
            freq=freq,
            sex=sex,
            location=location,
            units=units,
            level_status=level_status,
            name_of_international_agreement=name_of_international_agreement,
            education_level=education_level,
            type_of_product=type_of_product,
            type_of_facilities=type_of_facilities,
            name_of_international_institution=name_of_international_institution,
            type_of_occupation=type_of_occupation,
            tariff_regime_status=tariff_regime_status,
            mode_of_transportation=mode_of_transportation,
            type_of_mobile_technology=type_of_mobile_technology,
            name_of_non_communicable_disease=name_of_non_communicable_disease,
            type_of_skill=type_of_skill,
            type_of_speed=type_of_speed,
            migratory_status=migratory_status,
            disability_status=disability_status,
            hazard_type=hazard_type,
            ihr_capacity=ihr_capacity,
            reporting_type=reporting_type,
            cities=cities,
            activity=activity,
            policy_domains=policy_domains,
            years=years,
        )

        api_observation_pivot.additional_properties = d
        return api_observation_pivot

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
