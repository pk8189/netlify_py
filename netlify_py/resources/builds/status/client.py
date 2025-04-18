import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class StatusClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.BuildStatus]:
        """
        GET /{account_id}/builds/status

        Args:
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.builds.status.list(account_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/{account_id}/builds/status",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.BuildStatus],
            request_options=request_options or default_request_options(),
        )


class AsyncStatusClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.BuildStatus]:
        """
        GET /{account_id}/builds/status

        Args:
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.builds.status.list(account_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/{account_id}/builds/status",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.BuildStatus],
            request_options=request_options or default_request_options(),
        )
