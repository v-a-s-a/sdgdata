# Development

This page is for contributors working on `sdgdata` itself. The project uses
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

## Linting and Formatting

This project uses Ruff for linting, import sorting, and code formatting.

Fix lint and formatting issues before committing:

```bash
uv run ruff check . --fix
uv run ruff format .
```

Check lint and formatting without mutating files:

```bash
uv run ruff check .
uv run ruff format --check .
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
SDGDATA_LIVE_TESTS=1 uv run pytest -m live
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

## Versioning

`sdgdata` uses semantic version numbers in the form `MAJOR.MINOR.PATCH`.

While the package is in `0.x`, minor releases may include breaking public API
changes and patch releases should remain compatible bug fixes. Move to `1.0.0`
when the public API is intentionally stable.

## Release Checklist

1. Merge release preparation work to `main`.
2. Update the version in `pyproject.toml`.
3. Update `CHANGELOG.md` with the release notes.
4. Run the local preflight checks:

   ```bash
   uv run ruff check .
   uv run ruff format --check .
   uv run python scripts/generate_models.py --check
   uv run pytest -m mock
   uv build
   ```

5. Optionally install the built wheel into a clean temporary environment and
   verify `import sdgdata`.

## Continuous Integration

GitHub Actions runs on pushes to `main`, pull requests targeting `main`, and
manual workflow runs.

The default CI workflow:

1. Sets up Python 3.12 and `uv`.
2. Installs dependencies with `uv sync --locked --all-groups`.
3. Checks lint with `uv run ruff check .`.
4. Checks formatting with `uv run ruff format --check .`.
5. Checks generated models with `uv run python scripts/generate_models.py --check`.
6. Runs `uv run pytest -m mock`.
7. Builds release artifacts with `uv build`.
8. Uploads the `dist/` wheel and source distribution as the `sdgdata-dist`
   workflow artifact.

The live UNSD API smoke test is manual-only in GitHub Actions. Trigger the CI
workflow manually and enable `run_live_tests` to run it.

The CI workflow builds downloadable artifacts only. It does not publish to PyPI.
