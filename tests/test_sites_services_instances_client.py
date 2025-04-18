import pydantic
import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_update_204_success_default():
    """Tests a PUT request to the /sites/{site_id}/services/{addon}/instances/{instance_id} endpoint.

    Operation: update
    Test Case ID: success_default
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
    response = client.sites.services.instances.update(
        addon="string", data={}, instance_id="string", site_id="string"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_update_204_success_default():
    """Tests a PUT request to the /sites/{site_id}/services/{addon}/instances/{instance_id} endpoint.

    Operation: update
    Test Case ID: success_default
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
    response = await client.sites.services.instances.update(
        addon="string", data={}, instance_id="string", site_id="string"
    )
    assert response is None


def test_create_201_success_default():
    """Tests a POST request to the /sites/{site_id}/services/{addon}/instances endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.ServiceInstance

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.services.instances.create(
        addon="string", data={}, site_id="string"
    )
    try:
        pydantic.TypeAdapter(models.ServiceInstance).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /sites/{site_id}/services/{addon}/instances endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.ServiceInstance

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.services.instances.create(
        addon="string", data={}, site_id="string"
    )
    try:
        pydantic.TypeAdapter(models.ServiceInstance).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/services/{addon}/instances/{instance_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ServiceInstance

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.services.instances.get(
        addon="string", instance_id="string", site_id="string"
    )
    try:
        pydantic.TypeAdapter(models.ServiceInstance).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/services/{addon}/instances/{instance_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ServiceInstance

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.services.instances.get(
        addon="string", instance_id="string", site_id="string"
    )
    try:
        pydantic.TypeAdapter(models.ServiceInstance).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /sites/{site_id}/services/{addon}/instances/{instance_id} endpoint.

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
    response = client.sites.services.instances.delete(
        addon="string", instance_id="string", site_id="string"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /sites/{site_id}/services/{addon}/instances/{instance_id} endpoint.

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
    response = await client.sites.services.instances.delete(
        addon="string", instance_id="string", site_id="string"
    )
    assert response is None
