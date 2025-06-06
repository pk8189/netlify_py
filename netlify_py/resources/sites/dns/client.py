import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class DnsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DnsZone]:
        """
        GET /sites/{site_id}/dns

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
        client.sites.dns.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dns",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DnsZone],
            request_options=request_options or default_request_options(),
        )

    def update(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DnsZone]:
        """
        PUT /sites/{site_id}/dns

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
        client.sites.dns.update(site_id="string")
        ```
        """
        return self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/dns",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DnsZone],
            request_options=request_options or default_request_options(),
        )


class AsyncDnsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DnsZone]:
        """
        GET /sites/{site_id}/dns

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
        await client.sites.dns.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dns",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DnsZone],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DnsZone]:
        """
        PUT /sites/{site_id}/dns

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
        await client.sites.dns.update(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/dns",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DnsZone],
            request_options=request_options or default_request_options(),
        )
