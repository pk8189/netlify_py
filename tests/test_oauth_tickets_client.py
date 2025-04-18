import pydantic
import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_exchange_201_generated_success():
    """Tests a POST request to the /oauth/tickets/{ticket_id}/exchange endpoint.

    Operation: exchange
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.AccessToken

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth.tickets.exchange(ticket_id="string")
    try:
        pydantic.TypeAdapter(models.AccessToken).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_exchange_201_generated_success():
    """Tests a POST request to the /oauth/tickets/{ticket_id}/exchange endpoint.

    Operation: exchange
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.AccessToken

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth.tickets.exchange(ticket_id="string")
    try:
        pydantic.TypeAdapter(models.AccessToken).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_generated_success():
    """Tests a POST request to the /oauth/tickets endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Ticket

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth.tickets.create(client_id="string")
    try:
        pydantic.TypeAdapter(models.Ticket).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_generated_success():
    """Tests a POST request to the /oauth/tickets endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Ticket

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth.tickets.create(client_id="string")
    try:
        pydantic.TypeAdapter(models.Ticket).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /oauth/tickets/{ticket_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Ticket

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth.tickets.get(ticket_id="string")
    try:
        pydantic.TypeAdapter(models.Ticket).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /oauth/tickets/{ticket_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Ticket

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth.tickets.get(ticket_id="string")
    try:
        pydantic.TypeAdapter(models.Ticket).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
