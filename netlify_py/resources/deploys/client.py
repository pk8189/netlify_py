import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.resources.deploys.files import AsyncFilesClient, FilesClient
from netlify_py.resources.deploys.functions import AsyncFunctionsClient, FunctionsClient
from netlify_py.types import models


class DeploysClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.files = FilesClient(base_client=self._base_client)
        self.functions = FunctionsClient(base_client=self._base_client)

    def delete(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /deploys/{deploy_id}

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploys.delete(deploy_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        GET /deploys/{deploy_id}

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploys.get(deploy_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        POST /deploys/{deploy_id}/cancel

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Cancelled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploys.cancel(deploy_id="string")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/deploys/{deploy_id}/cancel",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    def lock(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        POST /deploys/{deploy_id}/lock

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploys.lock(deploy_id="string")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/deploys/{deploy_id}/lock",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    def unlock(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        POST /deploys/{deploy_id}/unlock

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.deploys.unlock(deploy_id="string")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/deploys/{deploy_id}/unlock",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )


class AsyncDeploysClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.files = AsyncFilesClient(base_client=self._base_client)
        self.functions = AsyncFunctionsClient(base_client=self._base_client)

    async def delete(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /deploys/{deploy_id}

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploys.delete(deploy_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        GET /deploys/{deploy_id}

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploys.get(deploy_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        POST /deploys/{deploy_id}/cancel

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Cancelled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploys.cancel(deploy_id="string")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/deploys/{deploy_id}/cancel",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    async def lock(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        POST /deploys/{deploy_id}/lock

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploys.lock(deploy_id="string")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/deploys/{deploy_id}/lock",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    async def unlock(
        self, *, deploy_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Deploy:
        """
        POST /deploys/{deploy_id}/unlock

        Args:
            deploy_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.deploys.unlock(deploy_id="string")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/deploys/{deploy_id}/unlock",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )
