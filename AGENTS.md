# Project Instructions: pyunsdg

## Development Workflow

This project uses `uv` for dependency management and task execution.

### Installation

To install dependencies and create a virtual environment:
```bash
uv sync
```

### Running Tests

Tests use `pytest`. The default test suite is deterministic and mocks the UNSD
API with `respx` using live-derived JSON fixtures committed under
`tests/fixtures/unsd_api/`.

#### Running Default Tests
Run the default test suite with mocked UNSD API responses:
```bash
uv run pytest -m "not live"
```

#### Refreshing Mock Fixtures
Refresh committed mock data from the live UNSD API:
```bash
uv run python scripts/download_test_fixtures.py
```

After refreshing fixtures, run the default tests and inspect the fixture diff
before committing.

#### Running Live Smoke Tests
Live API tests are opt-in because they call the external UNSD API. They compare
the committed mock fixture shape against current live API responses:
```bash
PYUNSDG_LIVE_TESTS=1 uv run pytest -m live
```

### Continuous Integration

GitHub Actions runs on pushes to `main`, pull requests targeting `main`, and
manual workflow runs.

The default CI workflow:
1. Sets up Python 3.12 and `uv`.
2. Installs dependencies with `uv sync --locked --all-groups`.
3. Runs `uv run pytest -m "not live"`.
4. Builds release artifacts with `uv build`.
5. Uploads the `dist/` wheel and source distribution as the `pyunsdg-dist`
   workflow artifact.

The live UNSD API smoke test is manual-only in GitHub Actions. Trigger the CI
workflow manually and enable `run_live_tests` to run it.

The CI workflow currently builds downloadable artifacts only. It does not create
a GitHub Release or publish to PyPI yet.

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
