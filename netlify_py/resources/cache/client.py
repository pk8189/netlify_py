import httpx
import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from netlify_py.types import params


class CacheClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def purge(
        self,
        *,
        cache_tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Purges cached content from Netlify's CDN. Supports purging by Cache-Tag.

        POST /purge

        Args:
            cache_tags: typing.List[str]
            site_id: str
            site_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.cache.purge()
        ```
        """
        _json = to_encodable(
            item={"cache_tags": cache_tags, "site_id": site_id, "site_slug": site_slug},
            dump_with=params._SerializerPurge,
        )
        return self._base_client.request(
            method="POST",
            path="/purge",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncCacheClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def purge(
        self,
        *,
        cache_tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Purges cached content from Netlify's CDN. Supports purging by Cache-Tag.

        POST /purge

        Args:
            cache_tags: typing.List[str]
            site_id: str
            site_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.cache.purge()
        ```
        """
        _json = to_encodable(
            item={"cache_tags": cache_tags, "site_id": site_id, "site_slug": site_slug},
            dump_with=params._SerializerPurge,
        )
        return await self._base_client.request(
            method="POST",
            path="/purge",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
