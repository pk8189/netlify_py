import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.resources.builds.log import AsyncLogClient, LogClient
from netlify_py.resources.builds.start import AsyncStartClient, StartClient
from netlify_py.resources.builds.status import AsyncStatusClient, StatusClient
from netlify_py.types import models


class BuildsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.status = StatusClient(base_client=self._base_client)
        self.log = LogClient(base_client=self._base_client)
        self.start = StartClient(base_client=self._base_client)

    def get(
        self, *, build_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Build:
        """
        GET /builds/{build_id}

        Args:
            build_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.builds.get(build_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/builds/{build_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Build,
            request_options=request_options or default_request_options(),
        )


class AsyncBuildsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.status = AsyncStatusClient(base_client=self._base_client)
        self.log = AsyncLogClient(base_client=self._base_client)
        self.start = AsyncStartClient(base_client=self._base_client)

    async def get(
        self, *, build_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Build:
        """
        GET /builds/{build_id}

        Args:
            build_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.builds.get(build_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/builds/{build_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Build,
            request_options=request_options or default_request_options(),
        )
