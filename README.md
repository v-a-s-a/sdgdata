
# pyunsdg

Using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) to generate a clean python SDK.


# Documentation

Workflow:
- Pulled the API spec from the UNSD website: https://unstats.un.org/sdgapi/swagger/v1/swagger.json
- The `openapi-python-client` does not support Swagger formatted specifications. I convert to an OpenAPI formatted specification using the [`swagger2openapi`](https://www.npmjs.com/package/swagger2openapi) package, with the following command:
    
        swagger2openapi --outfile data/un-api-openapi.json data/un-api-swagger.json

There are a few endpoints whose parameters names do not match


