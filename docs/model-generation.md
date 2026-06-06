# Model Generation

`data/un-api-openapi.json` is the source of truth for generated models.

Model generation uses `openapi-python-client`, but the generated API client is
not the public package interface. The hand-written `SDGClient` remains the main
client, and `sdgdata.models` preserves the public Pydantic imports used by the
package and tests.

## Generated Outputs

Model generation commits two outputs:

- `generated/openapi_python_client/`: model-related output from
  `openapi-python-client`, kept outside the public package for reviewable diffs.
- `src/sdgdata/models.py`: the Pydantic compatibility layer used by
  `SDGClient` and public imports such as `from sdgdata.models import ApiTarget`.

## Regenerate Models

Regenerate committed model files after changing `data/un-api-openapi.json`:

```bash
uv run python scripts/generate_models.py
```

Inspect the generated diff carefully before committing.

## Check For Stale Models

Check whether generated files are current without changing the working tree:

```bash
uv run python scripts/generate_models.py --check
```

CI runs this check before tests and build.

## Builds Do Not Regenerate Models

Package builds do not run model generation. `uv build` packages the committed
source files, which keeps builds reproducible and avoids mutating tracked files
during packaging.

## Refreshing The OpenAPI Source

Swagger-to-OpenAPI conversion is separate from package builds and model
generation. If you refresh the upstream Swagger document from
`https://unstats.un.org/sdgapi/swagger/v1/swagger.json`, convert it separately,
for example:

```bash
swagger2openapi --outfile data/un-api-openapi.json data/un-api-swagger.json
```
