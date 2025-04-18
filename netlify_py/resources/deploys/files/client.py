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


class FilesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def upload(
        self,
        *,
        data: httpx._types.FileTypes,
        deploy_id: str,
        path: str,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.File:
        """
        PUT /deploys/{deploy_id}/files/{path}

        Args:
            size: int
            data: httpx._types.FileTypes
            deploy_id: str
            path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploys.files.upload(
            data=open("./file.txt", "rb"), deploy_id="string", path="string"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "size",
                to_encodable(item=size, dump_with=int),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return self._base_client.request(
            method="PUT",
            path=f"/deploys/{deploy_id}/files/{path}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.File,
            request_options=request_options or default_request_options(),
        )


class AsyncFilesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def upload(
        self,
        *,
        data: httpx._types.FileTypes,
        deploy_id: str,
        path: str,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.File:
        """
        PUT /deploys/{deploy_id}/files/{path}

        Args:
            size: int
            data: httpx._types.FileTypes
            deploy_id: str
            path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploys.files.upload(
            data=open("./file.txt", "rb"), deploy_id="string", path="string"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "size",
                to_encodable(item=size, dump_with=int),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return await self._base_client.request(
            method="PUT",
            path=f"/deploys/{deploy_id}/files/{path}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.File,
            request_options=request_options or default_request_options(),
        )
