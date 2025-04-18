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
from netlify_py.types import models, params


class BuildsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        site_id: str,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Build]:
        """
        GET /sites/{site_id}/builds

        Args:
            page: int
            per_page: int
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.builds.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/builds",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Build],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id: str,
        clear_cache: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Build:
        """
        POST /sites/{site_id}/builds

        Args:
            clear_cache: bool
            image: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.builds.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"clear_cache": clear_cache, "image": image},
            dump_with=params._SerializerBuildSetup,
        )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/builds",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Build,
            request_options=request_options or default_request_options(),
        )


class AsyncBuildsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        site_id: str,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Build]:
        """
        GET /sites/{site_id}/builds

        Args:
            page: int
            per_page: int
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.builds.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/builds",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Build],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id: str,
        clear_cache: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Build:
        """
        POST /sites/{site_id}/builds

        Args:
            clear_cache: bool
            image: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.builds.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"clear_cache": clear_cache, "image": image},
            dump_with=params._SerializerBuildSetup,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/builds",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Build,
            request_options=request_options or default_request_options(),
        )
