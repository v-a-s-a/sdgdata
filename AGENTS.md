# Project Instructions: pyunsdg

## Development Workflow

This project uses `uv` for dependency management and task execution.

### Installation

To install dependencies and create a virtual environment:
```bash
uv sync
```

### Running Tests

We use integration tests to verify functionality against the live UNSD API.

#### Running Integration Tests
To run the integration tests using `uv`:
```bash
uv run python tests/integration_test.py
```

### Code Style and Standards
- **Pydantic Models**: All API responses are validated using Pydantic models defined in `src/pyunsdg/models.py`.
- **Client Implementation**: The main entry point is `UNSDClient` in `src/pyunsdg/client.py`.

### Common API Patterns

#### Finding Metadata
1. Use `client.get_geo_areas()` to find M49 codes for locations.
2. Use `client.get_targets()` to find SDG target codes.
3. Use `client.get_series_codes(target_code=...)` to find specific data series for a target.

#### Retrieving Data
Use `client.get_series_data()` with the codes found above.
```python
data = client.get_series_data(
    series_codes=["SERIES_CODE"],
    area_code="M49_CODE",
    start_period="YYYY",
    end_period="YYYY"
)
```
