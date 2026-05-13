
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
uv run pytest
```

Refresh the live-derived mock fixtures:

```bash
uv run python scripts/download_test_fixtures.py
```

Run the opt-in live UNSD API smoke test:

```bash
PYUNSDG_LIVE_TESTS=1 uv run pytest -m live
```


# Documentation

Workflow:
- Pulled the API spec from the UNSD website: https://unstats.un.org/sdgapi/swagger/v1/swagger.json
- The `openapi-python-client` does not support Swagger formatted specifications. I convert to an OpenAPI formatted specification using the [`swagger2openapi`](https://www.npmjs.com/package/swagger2openapi) package, with the following command:
    
        swagger2openapi --outfile data/un-api-openapi.json data/un-api-swagger.json

There are a few endpoints whose parameters names do not match
