import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class UnlinkRepoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def update(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Site:
        """
        [Beta] Unlinks the repo from the site.

        This action will also:
        - Delete associated deploy keys
        - Delete outgoing webhooks for the repo
        - Delete the site's build hooks

        PUT /sites/{site_id}/unlink_repo

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.unlink_repo.update(site_id="string")
        ```
        """
        return self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/unlink_repo",
            auth_names=["netlifyAuth"],
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )


class AsyncUnlinkRepoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def update(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Site:
        """
        [Beta] Unlinks the repo from the site.

        This action will also:
        - Delete associated deploy keys
        - Delete outgoing webhooks for the repo
        - Delete the site's build hooks

        PUT /sites/{site_id}/unlink_repo

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.unlink_repo.update(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/unlink_repo",
            auth_names=["netlifyAuth"],
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )
