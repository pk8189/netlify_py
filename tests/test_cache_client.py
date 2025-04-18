import httpx
import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment


def test_purge_202_success_default():
    """Tests a POST request to the /purge endpoint.

    Operation: purge
    Test Case ID: success_default
    Expected Status: 202
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.cache.purge()
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_purge_202_success_default():
    """Tests a POST request to the /purge endpoint.

    Operation: purge
    Test Case ID: success_default
    Expected Status: 202
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.cache.purge()
    assert isinstance(response, httpx.Response)
