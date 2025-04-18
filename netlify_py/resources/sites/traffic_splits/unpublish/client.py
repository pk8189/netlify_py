import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class UnpublishClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        site_id: str,
        split_test_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        POST /sites/{site_id}/traffic_splits/{split_test_id}/unpublish

        Args:
            site_id: str
            split_test_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            disabled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.traffic_splits.unpublish.create(
            site_id="string", split_test_id="string"
        )
        ```
        """
        self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/traffic_splits/{split_test_id}/unpublish",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncUnpublishClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        site_id: str,
        split_test_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        POST /sites/{site_id}/traffic_splits/{split_test_id}/unpublish

        Args:
            site_id: str
            split_test_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            disabled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.traffic_splits.unpublish.create(
            site_id="string", split_test_id="string"
        )
        ```
        """
        await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/traffic_splits/{split_test_id}/unpublish",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
