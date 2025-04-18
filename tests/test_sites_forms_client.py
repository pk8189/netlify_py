import pydantic
import pytest
import typing

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_list_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/forms endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.Form]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.forms.list(site_id="string")
    try:
        pydantic.TypeAdapter(typing.List[models.Form]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/forms endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.Form]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.forms.list(site_id="string")
    try:
        pydantic.TypeAdapter(typing.List[models.Form]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /sites/{site_id}/forms/{form_id} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.forms.delete(form_id="string", site_id="string")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /sites/{site_id}/forms/{form_id} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.forms.delete(form_id="string", site_id="string")
    assert response is None
