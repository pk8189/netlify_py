import pydantic
import pytest
import typing

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /dns_zones/{zone_id}/dns_records endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.DnsRecord

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.dns_zones.dns_records.create(zone_id="string")
    try:
        pydantic.TypeAdapter(models.DnsRecord).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /dns_zones/{zone_id}/dns_records endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.DnsRecord

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.dns_zones.dns_records.create(zone_id="string")
    try:
        pydantic.TypeAdapter(models.DnsRecord).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /dns_zones/{zone_id}/dns_records/{dns_record_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DnsRecord

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.dns_zones.dns_records.get(
        dns_record_id="string", zone_id="string"
    )
    try:
        pydantic.TypeAdapter(models.DnsRecord).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /dns_zones/{zone_id}/dns_records/{dns_record_id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DnsRecord

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.dns_zones.dns_records.get(
        dns_record_id="string", zone_id="string"
    )
    try:
        pydantic.TypeAdapter(models.DnsRecord).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /dns_zones/{zone_id}/dns_records endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.DnsRecord]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.dns_zones.dns_records.list(zone_id="string")
    try:
        pydantic.TypeAdapter(typing.List[models.DnsRecord]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /dns_zones/{zone_id}/dns_records endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.DnsRecord]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.dns_zones.dns_records.list(zone_id="string")
    try:
        pydantic.TypeAdapter(typing.List[models.DnsRecord]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /dns_zones/{zone_id}/dns_records/{dns_record_id} endpoint.

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
    response = client.dns_zones.dns_records.delete(
        dns_record_id="string", zone_id="string"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /dns_zones/{zone_id}/dns_records/{dns_record_id} endpoint.

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
    response = await client.dns_zones.dns_records.delete(
        dns_record_id="string", zone_id="string"
    )
    assert response is None
