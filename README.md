# sdgdata

[![CI](https://github.com/v-a-s-a/sdgdata/actions/workflows/ci.yml/badge.svg)](https://github.com/v-a-s-a/sdgdata/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/sdgdata.svg)](https://pypi.org/project/sdgdata/)
[![Python](https://img.shields.io/pypi/pyversions/sdgdata.svg)](https://pypi.org/project/sdgdata/)
[![License](https://img.shields.io/pypi/l/sdgdata.svg)](https://github.com/v-a-s-a/sdgdata/blob/main/LICENSE)
[![Status](https://img.shields.io/pypi/status/sdgdata.svg)](https://pypi.org/project/sdgdata/)

`sdgdata` is an unofficial Python client for retrieving SDG data from the UNSD SDG API.

It provides a lightweight client to retrieve Sustainable Development Goal (SDG) data and metadata from the API hosted by the United Nations Statistics Division (UNSD). The python data models are derived from the UNSD SDG API schema.

## Installation

Install from PyPI:

```bash
uv add sdgdata
```

or:

```bash
pip install sdgdata
```

## Quick Start

```python
from sdgdata import SDGClient
from sdgdata.client import is_single_time_series

client = SDGClient()

# Find available geographic areas and SDG targets.
areas = client.get_geo_areas()
targets = client.get_targets()

# Pick a series code and country
series = client.get_series_codes(target_code="3.8")
series_code = series[-1].code
area_code = areas[0].geoAreaCode

# Inspect available disaggregation dimensions for a series.
dimensions = client.get_series_dimensions(series_code)

# Fetch the coarsest available disaggregation by default.
data = client.get_series_data(
    series_codes=[series_code],
    area_code=area_code,
    start_period="2015",
    end_period="2026",
)

assert is_single_time_series(data)

# To fetch every disaggregation, opt into the unfiltered API response.
all_disaggregations = client.get_series_data(
    series_codes=[series_code],
    area_code=area_code,
    start_period="2015",
    end_period="2026",
    dimensions="all",
)

# Or request a specific disaggregation slice.
custom_slice = client.get_series_data(
    series_codes=[series_code],
    area_code=area_code,
    dimensions={"Reporting Type": "G"},
)
```

`get_series_data()` returns a list of dictionaries, making it straightforward
to create a dataframe for analysis. By default, it filters to the coarsest available disaggregation, such
as all ages, both sexes, and total groups when those dimension values exist.
For the upstream observation field descriptions, see the
[UNSD SDG API Swagger documentation](https://unstats.un.org/sdgapi/swagger/).

## Documentation

- [Development](docs/development.md): setup, tests, fixture refreshes, builds, and CI behavior.
- [Model generation](docs/model-generation.md): generated models, stale checks, and OpenAPI source data.
