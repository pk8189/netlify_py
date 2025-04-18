import pydantic
import pytest
import typing

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_update_201_success_default():
    """Tests a PUT request to the /sites/{site_id}/traffic_splits/{split_test_id} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.SplitTest

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.traffic_splits.update(
        site_id="string", split_test_id="string"
    )
    try:
        pydantic.TypeAdapter(models.SplitTest).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_201_success_default():
    """Tests a PUT request to the /sites/{site_id}/traffic_splits/{split_test_id} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.SplitTest

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.traffic_splits.update(
        site_id="string", split_test_id="string"
    )
    try:
        pydantic.TypeAdapter(models.SplitTest).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_default():
    """Tests a POST request to the /sites/{site_id}/traffic_splits endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.SplitTest

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.traffic_splits.create(site_id="string")
    try:
        pydantic.TypeAdapter(models.SplitTest).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /sites/{site_id}/traffic_splits endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.SplitTest

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.traffic_splits.create(site_id="string")
    try:
        pydantic.TypeAdapter(models.SplitTest).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/traffic_splits/{split_test_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SplitTest

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.traffic_splits.get(site_id="string", split_test_id="string")
    try:
        pydantic.TypeAdapter(models.SplitTest).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/traffic_splits/{split_test_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SplitTest

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.traffic_splits.get(
        site_id="string", split_test_id="string"
    )
    try:
        pydantic.TypeAdapter(models.SplitTest).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/traffic_splits endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.SplitTest]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.sites.traffic_splits.list(site_id="string")
    try:
        pydantic.TypeAdapter(typing.List[models.SplitTest]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /sites/{site_id}/traffic_splits endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.SplitTest]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.sites.traffic_splits.list(site_id="string")
    try:
        pydantic.TypeAdapter(typing.List[models.SplitTest]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
