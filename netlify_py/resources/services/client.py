import typing

from netlify_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from netlify_py.resources.services.manifest import AsyncManifestClient, ManifestClient
from netlify_py.types import models


class ServicesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.manifest = ManifestClient(base_client=self._base_client)

    def list(
        self,
        *,
        search: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Service]:
        """
        GET /services/

        Args:
            search: str
            request_options: Additional options to customize the HTTP request

        Returns:
            services

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.services.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(search, type_utils.NotGiven):
            encode_query_param(
                _query,
                "search",
                to_encodable(item=search, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/services/",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Service],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        addon_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Service:
        """
        GET /services/{addonName}

        Args:
            addonName: str
            request_options: Additional options to customize the HTTP request

        Returns:
            services

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.services.get(addon_name="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/services/{addon_name}",
            auth_names=["netlifyAuth"],
            cast_to=models.Service,
            request_options=request_options or default_request_options(),
        )


class AsyncServicesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.manifest = AsyncManifestClient(base_client=self._base_client)

    async def list(
        self,
        *,
        search: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Service]:
        """
        GET /services/

        Args:
            search: str
            request_options: Additional options to customize the HTTP request

        Returns:
            services

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.services.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(search, type_utils.NotGiven):
            encode_query_param(
                _query,
                "search",
                to_encodable(item=search, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/services/",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Service],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        addon_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Service:
        """
        GET /services/{addonName}

        Args:
            addonName: str
            request_options: Additional options to customize the HTTP request

        Returns:
            services

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.services.get(addon_name="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/services/{addon_name}",
            auth_names=["netlifyAuth"],
            cast_to=models.Service,
            request_options=request_options or default_request_options(),
        )
