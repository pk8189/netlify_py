import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)


class MetadataClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        GET /sites/{site_id}/metadata

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
        client.sites.metadata.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/metadata",
            auth_names=["netlifyAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/metadata

        Args:
            data: typing.Dict[str, typing.Any]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.metadata.update(data={}, site_id="string")
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/metadata",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncMetadataClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        GET /sites/{site_id}/metadata

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
        await client.sites.metadata.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/metadata",
            auth_names=["netlifyAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/metadata

        Args:
            data: typing.Dict[str, typing.Any]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.metadata.update(data={}, site_id="string")
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/metadata",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
