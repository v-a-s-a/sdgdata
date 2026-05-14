
# pyunsdg

Using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) to generate a clean python SDK.

## Local development install

From another local Python project, install this package in editable mode:

```bash
python -m pip install -e /Users/vasa/Projects/pyunsdg
```

Or with uv:

```bash
uv add --editable /Users/vasa/Projects/pyunsdg
```

To build distributable artifacts:

```bash
uv build
```

Install the built wheel into another environment with:

```bash
python -m pip install /Users/vasa/Projects/pyunsdg/dist/pyunsdg-0.1.0-py3-none-any.whl
```

## Testing

Run the default test suite with mocked UNSD API responses:

```bash
uv run pytest -m "not live"
```

Refresh the live-derived mock fixtures:

```bash
uv run python scripts/download_test_fixtures.py
```

Run the opt-in live UNSD API smoke test:

```bash
PYUNSDG_LIVE_TESTS=1 uv run pytest -m live
```

## Continuous integration

GitHub Actions runs CI on pushes to `main`, pull requests targeting `main`,
and manual workflow runs.

The default CI job:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs dependencies with `uv sync --locked --all-groups`.
4. Runs the mocked test suite with `uv run pytest -m "not live"`.
5. Builds the wheel and source distribution with `uv build`.
6. Uploads the files from `dist/` as a workflow artifact named `pyunsdg-dist`.

These uploaded artifacts are downloadable from the GitHub Actions run page. They
are build outputs only: the workflow does not create a GitHub Release and does
not publish to PyPI yet.

The live UNSD API smoke test is manual-only. From the Actions tab, run the CI
workflow manually and enable `run_live_tests` to compare the committed mock
fixtures with the live API.

Future release automation can build on this by adding a tag-triggered workflow
that creates a GitHub Release and publishes the same wheel/source distribution
to PyPI.


# Documentation

Workflow:
- Pulled the API spec from the UNSD website: https://unstats.un.org/sdgapi/swagger/v1/swagger.json
- The `openapi-python-client` does not support Swagger formatted specifications. I convert to an OpenAPI formatted specification using the [`swagger2openapi`](https://www.npmjs.com/package/swagger2openapi) package, with the following command:
    
        swagger2openapi --outfile data/un-api-openapi.json data/un-api-swagger.json

There are a few endpoints whose parameters names do not match
