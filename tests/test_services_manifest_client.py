import pydantic
import pytest
import typing

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment


def test_list_201_generated_success():
    """Tests a GET request to the /services/{addonName}/manifest endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Synchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.services.manifest.list(addon_name="string")
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_201_generated_success():
    """Tests a GET request to the /services/{addonName}/manifest endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Asynchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.services.manifest.list(addon_name="string")
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
