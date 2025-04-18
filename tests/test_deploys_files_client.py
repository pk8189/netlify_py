import pydantic
import pytest

from netlify_py import AsyncClient, Client
from netlify_py.environment import Environment
from netlify_py.types import models


def test_upload_200_success_default():
    """Tests a PUT request to the /deploys/{deploy_id}/files/{path} endpoint.

    Operation: upload
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.File

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.deploys.files.upload(
        data=open("./file.txt", "rb"), deploy_id="string", path="string"
    )
    try:
        pydantic.TypeAdapter(models.File).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_upload_200_success_default():
    """Tests a PUT request to the /deploys/{deploy_id}/files/{path} endpoint.

    Operation: upload
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.File

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.deploys.files.upload(
        data=open("./file.txt", "rb"), deploy_id="string", path="string"
    )
    try:
        pydantic.TypeAdapter(models.File).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
