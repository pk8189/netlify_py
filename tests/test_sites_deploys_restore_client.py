import pydantic
import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_create_201_generated_success():
    """Tests a POST request to the /sites/{site_id}/deploys/{deploy_id}/restore endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Deploy

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.deploys.restore.create(deploy_id="string", site_id="string")
    try:
        pydantic.TypeAdapter(models.Deploy).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_generated_success():
    """Tests a POST request to the /sites/{site_id}/deploys/{deploy_id}/restore endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Deploy

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.deploys.restore.create(
        deploy_id="string", site_id="string"
    )
    try:
        pydantic.TypeAdapter(models.Deploy).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
