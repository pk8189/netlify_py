import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment


def test_update_204_generated_success():
    """Tests a PUT request to the /sites/{site_id}/rollback endpoint.

    Operation: update
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
    response = client.sites.rollback.update(site_id="string")
    assert response is None


@pytest.mark.asyncio
async def test_await_update_204_generated_success():
    """Tests a PUT request to the /sites/{site_id}/rollback endpoint.

    Operation: update
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
    response = await client.sites.rollback.update(site_id="string")
    assert response is None
