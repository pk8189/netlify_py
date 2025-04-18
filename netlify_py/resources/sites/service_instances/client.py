import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class ServiceInstancesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.ServiceInstance]:
        """
        GET /sites/{site_id}/service-instances

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
        client.sites.service_instances.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/service-instances",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.ServiceInstance],
            request_options=request_options or default_request_options(),
        )


class AsyncServiceInstancesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.ServiceInstance]:
        """
        GET /sites/{site_id}/service-instances

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
        await client.sites.service_instances.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/service-instances",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.ServiceInstance],
            request_options=request_options or default_request_options(),
        )
