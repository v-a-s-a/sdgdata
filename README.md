
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

Check that generated models are current:

```bash
uv run python scripts/generate_models.py --check
```

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
4. Checks generated models with `uv run python scripts/generate_models.py --check`.
5. Runs the mocked test suite with `uv run pytest -m "not live"`.
6. Builds the wheel and source distribution with `uv build`.
7. Uploads the files from `dist/` as a workflow artifact named `pyunsdg-dist`.

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

## Model generation

The committed `data/un-api-openapi.json` file is the source of truth for
generated models. Model generation uses `openapi-python-client` and commits two
outputs:

- `generated/openapi_python_client/`: the model-related output from
  `openapi-python-client`, kept outside the public package for reviewable diffs.
- `src/pyunsdg/models.py`: the Pydantic compatibility layer used by the
  hand-written `UNSDClient` and existing public imports such as
  `from pyunsdg.models import ApiTarget`.

Regenerate committed model files after changing `data/un-api-openapi.json`:

```bash
uv run python scripts/generate_models.py
```

Check whether generated files are stale without changing the working tree:

```bash
uv run python scripts/generate_models.py --check
```

Package builds do not regenerate models. `uv build` packages the committed
source files, and CI runs the stale-generation check before tests and build.

Swagger-to-OpenAPI conversion is separate from package builds and model
generation. If you refresh the upstream Swagger document from
https://unstats.un.org/sdgapi/swagger/v1/swagger.json, convert it separately,
for example:

```bash
swagger2openapi --outfile data/un-api-openapi.json data/un-api-swagger.json
```
