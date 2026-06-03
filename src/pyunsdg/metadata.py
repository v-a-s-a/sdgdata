from pydantic import BaseModel, Field

from pyunsdg.models import ApiDimension


class SeriesMetadata(BaseModel):
    code: str
    description: str | None = None
    uri: str | None = None
    latest_release: str | None = None
    releases: list[str] = Field(default_factory=list)
    dimensions: list[ApiDimension] = Field(default_factory=list)


class IndicatorSeriesMetadata(BaseModel):
    code: str
    description: str | None = None
    tier: str | None = None
    uri: str | None = None
    series: list[SeriesMetadata] = Field(default_factory=list)


class TargetSeriesMetadata(BaseModel):
    code: str
    title: str | None = None
    description: str | None = None
    uri: str | None = None
    indicators: list[IndicatorSeriesMetadata] = Field(default_factory=list)
