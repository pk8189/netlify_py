import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class DeployKeysClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, key_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /deploy_keys/{key_id}

        Args:
            key_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Not Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploy_keys.delete(key_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/deploy_keys/{key_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DeployKey]:
        """
        GET /deploy_keys

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploy_keys.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/deploy_keys",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DeployKey],
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, key_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeployKey:
        """
        GET /deploy_keys/{key_id}

        Args:
            key_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploy_keys.get(key_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/deploy_keys/{key_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DeployKey,
            request_options=request_options or default_request_options(),
        )

    def create(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeployKey:
        """
        POST /deploy_keys

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploy_keys.create()
        ```
        """
        return self._base_client.request(
            method="POST",
            path="/deploy_keys",
            auth_names=["netlifyAuth"],
            cast_to=models.DeployKey,
            request_options=request_options or default_request_options(),
        )


class AsyncDeployKeysClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, key_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /deploy_keys/{key_id}

        Args:
            key_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Not Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploy_keys.delete(key_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/deploy_keys/{key_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DeployKey]:
        """
        GET /deploy_keys

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploy_keys.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/deploy_keys",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DeployKey],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, key_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeployKey:
        """
        GET /deploy_keys/{key_id}

        Args:
            key_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploy_keys.get(key_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/deploy_keys/{key_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DeployKey,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeployKey:
        """
        POST /deploy_keys

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploy_keys.create()
        ```
        """
        return await self._base_client.request(
            method="POST",
            path="/deploy_keys",
            auth_names=["netlifyAuth"],
            cast_to=models.DeployKey,
            request_options=request_options or default_request_options(),
        )
