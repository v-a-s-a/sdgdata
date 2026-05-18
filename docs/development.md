# Development

This page is for contributors working on `pyunsdg` itself. The project uses
`uv` for dependency management and task execution.

## Setup

Install dependencies and create a virtual environment:

```bash
uv sync
```

Install all dependency groups, as CI does:

```bash
uv sync --locked --all-groups
```

## Testing

Run the default deterministic test suite with mocked UNSD API responses:

```bash
uv run pytest -m mock
```

The mocked tests use live-derived JSON fixtures committed under
`tests/fixtures/unsd_api/`.

Run the opt-in live UNSD API smoke tests:

```bash
PYUNSDG_LIVE_TESTS=1 uv run pytest -m live
```

Live tests call the external UNSD API and compare current API responses with the
committed fixture shape.

## Refreshing Fixtures

Refresh committed mock data from the live UNSD API:

```bash
uv run python scripts/download_test_fixtures.py
```

After refreshing fixtures, run the default tests and inspect the fixture diff
before committing.

## Build

Build the wheel and source distribution:

```bash
uv build
```

The build packages committed source files. It does not regenerate models or
refresh fixtures.

## Continuous Integration

GitHub Actions runs on pushes to `main`, pull requests targeting `main`, and
manual workflow runs.

The default CI workflow:

1. Sets up Python 3.12 and `uv`.
2. Installs dependencies with `uv sync --locked --all-groups`.
3. Checks generated models with `uv run python scripts/generate_models.py --check`.
4. Runs `uv run pytest -m mock`.
5. Builds release artifacts with `uv build`.
6. Uploads the `dist/` wheel and source distribution as the `pyunsdg-dist`
   workflow artifact.

The live UNSD API smoke test is manual-only in GitHub Actions. Trigger the CI
workflow manually and enable `run_live_tests` to run it.

The CI workflow currently builds downloadable artifacts only. It does not create
a GitHub Release or publish to PyPI.
