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


class FunctionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        site_id: str,
        filter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.SiteFunction]:
        """
        GET /sites/{site_id}/functions

        Args:
            filter: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.functions.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(item=filter, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/functions",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.SiteFunction],
            request_options=request_options or default_request_options(),
        )


class AsyncFunctionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        site_id: str,
        filter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.SiteFunction]:
        """
        GET /sites/{site_id}/functions

        Args:
            filter: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.functions.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(item=filter, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/functions",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.SiteFunction],
            request_options=request_options or default_request_options(),
        )
