import typing

from netlify_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
)
from netlify_py.types import models


class TicketsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, ticket_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Ticket:
        """
        GET /oauth/tickets/{ticket_id}

        Args:
            ticket_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            ok

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth.tickets.get(ticket_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/oauth/tickets/{ticket_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Ticket,
            request_options=request_options or default_request_options(),
        )

    def create(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Ticket:
        """
        POST /oauth/tickets

        Args:
            client_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            ok

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth.tickets.create(client_id="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "client_id",
            to_encodable(item=client_id, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="POST",
            path="/oauth/tickets",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.Ticket,
            request_options=request_options or default_request_options(),
        )

    def exchange(
        self, *, ticket_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AccessToken:
        """
        POST /oauth/tickets/{ticket_id}/exchange

        Args:
            ticket_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            ok

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth.tickets.exchange(ticket_id="string")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/oauth/tickets/{ticket_id}/exchange",
            auth_names=["netlifyAuth"],
            cast_to=models.AccessToken,
            request_options=request_options or default_request_options(),
        )


class AsyncTicketsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, ticket_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Ticket:
        """
        GET /oauth/tickets/{ticket_id}

        Args:
            ticket_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            ok

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth.tickets.get(ticket_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/oauth/tickets/{ticket_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Ticket,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Ticket:
        """
        POST /oauth/tickets

        Args:
            client_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            ok

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth.tickets.create(client_id="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "client_id",
            to_encodable(item=client_id, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="POST",
            path="/oauth/tickets",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.Ticket,
            request_options=request_options or default_request_options(),
        )

    async def exchange(
        self, *, ticket_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.AccessToken:
        """
        POST /oauth/tickets/{ticket_id}/exchange

        Args:
            ticket_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            ok

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth.tickets.exchange(ticket_id="string")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/oauth/tickets/{ticket_id}/exchange",
            auth_names=["netlifyAuth"],
            cast_to=models.AccessToken,
            request_options=request_options or default_request_options(),
        )
