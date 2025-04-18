import httpx
import typing

from netlify_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_content,
    to_encodable,
    type_utils,
)
from netlify_py.types import models


class FunctionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def upload(
        self,
        *,
        data: httpx._types.FileTypes,
        deploy_id: str,
        name: str,
        invocation_mode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        runtime: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeout: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Function:
        """
        PUT /deploys/{deploy_id}/functions/{name}

        Args:
            invocation_mode: str
            runtime: str
            size: int
            timeout: int
            data: httpx._types.FileTypes
            deploy_id: str
            name: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploys.functions.upload(
            data=open("./file.txt", "rb"), deploy_id="string", name="string"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(invocation_mode, type_utils.NotGiven):
            encode_query_param(
                _query,
                "invocation_mode",
                to_encodable(item=invocation_mode, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(runtime, type_utils.NotGiven):
            encode_query_param(
                _query,
                "runtime",
                to_encodable(item=runtime, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "size",
                to_encodable(item=size, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(timeout, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeout",
                to_encodable(item=timeout, dump_with=int),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return self._base_client.request(
            method="PUT",
            path=f"/deploys/{deploy_id}/functions/{name}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.Function,
            request_options=request_options or default_request_options(),
        )


class AsyncFunctionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def upload(
        self,
        *,
        data: httpx._types.FileTypes,
        deploy_id: str,
        name: str,
        invocation_mode: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        runtime: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeout: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Function:
        """
        PUT /deploys/{deploy_id}/functions/{name}

        Args:
            invocation_mode: str
            runtime: str
            size: int
            timeout: int
            data: httpx._types.FileTypes
            deploy_id: str
            name: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploys.functions.upload(
            data=open("./file.txt", "rb"), deploy_id="string", name="string"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(invocation_mode, type_utils.NotGiven):
            encode_query_param(
                _query,
                "invocation_mode",
                to_encodable(item=invocation_mode, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(runtime, type_utils.NotGiven):
            encode_query_param(
                _query,
                "runtime",
                to_encodable(item=runtime, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "size",
                to_encodable(item=size, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(timeout, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeout",
                to_encodable(item=timeout, dump_with=int),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return await self._base_client.request(
            method="PUT",
            path=f"/deploys/{deploy_id}/functions/{name}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.Function,
            request_options=request_options or default_request_options(),
        )
