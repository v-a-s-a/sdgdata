# pyunsdg

`pyunsdg` is a Python client for the United Nations Statistics Division SDG API.

It provides a simple client to retrieve Sustainable Development Goal metadata
and data from Python, with models derived from the UNSD SDG API schema.

## Features

- Fetch SDG goals, targets, indicators, and series metadata.
- Look up geographic areas and M49 area codes.
- Retrieve paginated SDG series observations with simple Python calls.
- Validate structured API responses with Pydantic models.
- Load observation data into analysis tools such as pandas or Polars.

## Installation

```bash
uv add git+https://github.com/v-a-s-a/pyunsdg.git
```

## Quick Start

```python
from pyunsdg import UNSDClient, is_single_time_series

client = UNSDClient()

# Find available geographic areas and SDG targets.
areas = client.get_geo_areas()
targets = client.get_targets()

# Find latest-release series codes for a target.
series = client.get_series_codes(target_code="3.8")

# Inspect available disaggregation dimensions for a series.
dimensions = client.get_series_dimensions(series[-1].code)

# Fetch the coarsest available disaggregation by default.
data = client.get_series_data(
    series_codes=[series[-1].code],
    area_code=areas[0].geoAreaCode,
    start_period="2015",
    end_period="2026",
)

assert is_single_time_series(data)

# To fetch every disaggregation, opt into the unfiltered API response.
all_disaggregations = client.get_series_data(
    series_codes=[series[-1].code],
    area_code=areas[0].geoAreaCode,
    start_period="2015",
    end_period="2026",
    dimensions="all",
)

# Or request a specific disaggregation slice.
custom_slice = client.get_series_data(
    series_codes=[series[-1].code],
    area_code=areas[0].geoAreaCode,
    dimensions={"Reporting Type": "G"},
)
```

`get_series_data()` returns a list of dictionaries, making it straightforward
to create a dataframe for analysis. By default, it filters to the coarsest
available disaggregation, such as all ages, both sexes, and total groups when
those dimension values exist.

## Documentation

- [Development](docs/development.md): setup, tests, fixture refreshes, builds, and CI behavior.
- [Model generation](docs/model-generation.md): generated models, stale checks, and OpenAPI source data.
