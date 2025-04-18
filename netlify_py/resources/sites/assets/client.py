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
from netlify_py.types import models


class AssetsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        asset_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/assets/{asset_id}

        Args:
            asset_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.assets.delete(asset_id="string", site_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/assets/{asset_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Asset]:
        """
        GET /sites/{site_id}/assets

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
        client.sites.assets.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/assets",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Asset],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        asset_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Asset:
        """
        GET /sites/{site_id}/assets/{asset_id}

        Args:
            asset_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.assets.get(asset_id="string", site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/assets/{asset_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Asset,
            request_options=request_options or default_request_options(),
        )

    def get_public_signature(
        self,
        *,
        asset_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssetPublicSignature:
        """
        GET /sites/{site_id}/assets/{asset_id}/public_signature

        Args:
            asset_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.assets.get_public_signature(asset_id="string", site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/assets/{asset_id}/public_signature",
            auth_names=["netlifyAuth"],
            cast_to=models.AssetPublicSignature,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        content_type: str,
        name: str,
        site_id: str,
        size: int,
        visibility: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssetSignature:
        """
        POST /sites/{site_id}/assets

        Args:
            visibility: str
            content_type: str
            name: str
            site_id: str
            size: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.assets.create(
            content_type="string", name="string", site_id="string", size=123
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "content_type",
            to_encodable(item=content_type, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "name",
            to_encodable(item=name, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "size",
            to_encodable(item=size, dump_with=int),
            style="form",
            explode=True,
        )
        if not isinstance(visibility, type_utils.NotGiven):
            encode_query_param(
                _query,
                "visibility",
                to_encodable(item=visibility, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/assets",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.AssetSignature,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        asset_id: str,
        site_id: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Asset:
        """
        PUT /sites/{site_id}/assets/{asset_id}

        Args:
            asset_id: str
            site_id: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.assets.update(asset_id="string", site_id="string", state="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "state",
            to_encodable(item=state, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/assets/{asset_id}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.Asset,
            request_options=request_options or default_request_options(),
        )


class AsyncAssetsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        asset_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/assets/{asset_id}

        Args:
            asset_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.assets.delete(asset_id="string", site_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/assets/{asset_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Asset]:
        """
        GET /sites/{site_id}/assets

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
        await client.sites.assets.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/assets",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Asset],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        asset_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Asset:
        """
        GET /sites/{site_id}/assets/{asset_id}

        Args:
            asset_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.assets.get(asset_id="string", site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/assets/{asset_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Asset,
            request_options=request_options or default_request_options(),
        )

    async def get_public_signature(
        self,
        *,
        asset_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssetPublicSignature:
        """
        GET /sites/{site_id}/assets/{asset_id}/public_signature

        Args:
            asset_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.assets.get_public_signature(
            asset_id="string", site_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/assets/{asset_id}/public_signature",
            auth_names=["netlifyAuth"],
            cast_to=models.AssetPublicSignature,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        content_type: str,
        name: str,
        site_id: str,
        size: int,
        visibility: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssetSignature:
        """
        POST /sites/{site_id}/assets

        Args:
            visibility: str
            content_type: str
            name: str
            site_id: str
            size: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.assets.create(
            content_type="string", name="string", site_id="string", size=123
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "content_type",
            to_encodable(item=content_type, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "name",
            to_encodable(item=name, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "size",
            to_encodable(item=size, dump_with=int),
            style="form",
            explode=True,
        )
        if not isinstance(visibility, type_utils.NotGiven):
            encode_query_param(
                _query,
                "visibility",
                to_encodable(item=visibility, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/assets",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.AssetSignature,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        asset_id: str,
        site_id: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Asset:
        """
        PUT /sites/{site_id}/assets/{asset_id}

        Args:
            asset_id: str
            site_id: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Updated

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.assets.update(
            asset_id="string", site_id="string", state="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "state",
            to_encodable(item=state, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/assets/{asset_id}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.Asset,
            request_options=request_options or default_request_options(),
        )
