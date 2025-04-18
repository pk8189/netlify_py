import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment


def test_create_204_generated_success():
    """Tests a POST request to the /sites/{site_id}/traffic_splits/{split_test_id}/publish endpoint.

    Operation: create
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
    response = client.sites.traffic_splits.publish.create(
        site_id="string", split_test_id="string"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_create_204_generated_success():
    """Tests a POST request to the /sites/{site_id}/traffic_splits/{split_test_id}/publish endpoint.

    Operation: create
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
    response = await client.sites.traffic_splits.publish.create(
        site_id="string", split_test_id="string"
    )
    assert response is None
