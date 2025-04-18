import httpx
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


class DevServersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        DELETE /sites/{site_id}/dev_servers

        Args:
            branch: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.dev_servers.delete(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/dev_servers",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

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
    ) -> typing.List[models.DevServer]:
        """
        GET /sites/{site_id}/dev_servers

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
        client.sites.dev_servers.list(site_id="string")
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
            path=f"/sites/{site_id}/dev_servers",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.DevServer],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        dev_server_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevServer:
        """
        GET /sites/{site_id}/dev_servers/{dev_server_id}

        Args:
            dev_server_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.dev_servers.get(dev_server_id="string", site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dev_servers/{dev_server_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DevServer,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.DevServer]:
        """
        POST /sites/{site_id}/dev_servers

        Args:
            branch: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.dev_servers.create(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/dev_servers",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.DevServer],
            request_options=request_options or default_request_options(),
        )


class AsyncDevServersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        DELETE /sites/{site_id}/dev_servers

        Args:
            branch: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.dev_servers.delete(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/dev_servers",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

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
    ) -> typing.List[models.DevServer]:
        """
        GET /sites/{site_id}/dev_servers

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
        await client.sites.dev_servers.list(site_id="string")
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
            path=f"/sites/{site_id}/dev_servers",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.DevServer],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        dev_server_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevServer:
        """
        GET /sites/{site_id}/dev_servers/{dev_server_id}

        Args:
            dev_server_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.dev_servers.get(dev_server_id="string", site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dev_servers/{dev_server_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DevServer,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.DevServer]:
        """
        POST /sites/{site_id}/dev_servers

        Args:
            branch: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.dev_servers.create(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/dev_servers",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.DevServer],
            request_options=request_options or default_request_options(),
        )
