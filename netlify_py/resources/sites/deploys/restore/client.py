import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class RestoreClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        deploy_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        POST /sites/{site_id}/deploys/{deploy_id}/restore

        Args:
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.deploys.restore.create(deploy_id="string", site_id="string")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/deploys/{deploy_id}/restore",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )


class AsyncRestoreClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        deploy_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        POST /sites/{site_id}/deploys/{deploy_id}/restore

        Args:
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.deploys.restore.create(deploy_id="string", site_id="string")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/deploys/{deploy_id}/restore",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )
