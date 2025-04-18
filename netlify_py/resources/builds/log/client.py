import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class LogClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self, *, build_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        POST /builds/{build_id}/log

        Args:
            build_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.builds.log.create(build_id="string")
        ```
        """
        self._base_client.request(
            method="POST",
            path=f"/builds/{build_id}/log",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncLogClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self, *, build_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        POST /builds/{build_id}/log

        Args:
            build_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.builds.log.create(build_id="string")
        ```
        """
        await self._base_client.request(
            method="POST",
            path=f"/builds/{build_id}/log",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
