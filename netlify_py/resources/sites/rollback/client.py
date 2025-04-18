import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class RollbackClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def update(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        PUT /sites/{site_id}/rollback

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.rollback.update(site_id="string")
        ```
        """
        self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/rollback",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncRollbackClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def update(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        PUT /sites/{site_id}/rollback

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.rollback.update(site_id="string")
        ```
        """
        await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/rollback",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
