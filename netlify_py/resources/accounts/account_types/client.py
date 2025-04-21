import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class AccountTypesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.AccountType]:
        """
        GET /accounts/types

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.account_types.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/accounts/types",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.AccountType],
            request_options=request_options or default_request_options(),
        )


class AsyncAccountTypesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.AccountType]:
        """
        GET /accounts/types

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.account_types.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/accounts/types",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.AccountType],
            request_options=request_options or default_request_options(),
        )
