import pydantic
import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_update_200_generated_success():
    """Tests a PUT request to the /dns_zones/{zone_id}/transfer endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DnsZone

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.dns_zones.transfer.update(
        account_id="string",
        transfer_account_id="string",
        transfer_user_id="string",
        zone_id="string",
    )
    try:
        pydantic.TypeAdapter(models.DnsZone).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a PUT request to the /dns_zones/{zone_id}/transfer endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DnsZone

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.dns_zones.transfer.update(
        account_id="string",
        transfer_account_id="string",
        transfer_user_id="string",
        zone_id="string",
    )
    try:
        pydantic.TypeAdapter(models.DnsZone).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
