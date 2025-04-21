import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class ManifestClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        addon_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        GET /services/{addonName}/manifest

        Args:
            addonName: str
            request_options: Additional options to customize the HTTP request

        Returns:
            retrieving from provider

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.services.manifest.list(addon_name="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/services/{addon_name}/manifest",
            auth_names=["netlifyAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )


class AsyncManifestClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        addon_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        GET /services/{addonName}/manifest

        Args:
            addonName: str
            request_options: Additional options to customize the HTTP request

        Returns:
            retrieving from provider

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.services.manifest.list(addon_name="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/services/{addon_name}/manifest",
            auth_names=["netlifyAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
