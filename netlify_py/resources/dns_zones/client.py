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
from netlify_py.resources.dns_zones.dns_records import (
    AsyncDnsRecordsClient,
    DnsRecordsClient,
)
from netlify_py.resources.dns_zones.transfer import AsyncTransferClient, TransferClient
from netlify_py.types import models, params


class DnsZonesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.dns_records = DnsRecordsClient(base_client=self._base_client)
        self.transfer = TransferClient(base_client=self._base_client)

    def delete(
        self, *, zone_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /dns_zones/{zone_id}

        Args:
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            delete a single DNS zone

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.delete(zone_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/dns_zones/{zone_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.DnsZone]:
        """
        GET /dns_zones

        Args:
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get all DNS zones the user has access to

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(account_slug, type_utils.NotGiven):
            encode_query_param(
                _query,
                "account_slug",
                to_encodable(item=account_slug, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/dns_zones",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.DnsZone],
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, zone_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DnsZone:
        """
        GET /dns_zones/{zone_id}

        Args:
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get a single DNS zone

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.get(zone_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/dns_zones/{zone_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DnsZone,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsZone:
        """
        POST /dns_zones

        Args:
            account_slug: str
            name: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.create()
        ```
        """
        _json = to_encodable(
            item={"account_slug": account_slug, "name": name, "site_id": site_id},
            dump_with=params._SerializerDnsZoneSetup,
        )
        return self._base_client.request(
            method="POST",
            path="/dns_zones",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.DnsZone,
            request_options=request_options or default_request_options(),
        )


class AsyncDnsZonesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.dns_records = AsyncDnsRecordsClient(base_client=self._base_client)
        self.transfer = AsyncTransferClient(base_client=self._base_client)

    async def delete(
        self, *, zone_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /dns_zones/{zone_id}

        Args:
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            delete a single DNS zone

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.delete(zone_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/dns_zones/{zone_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.DnsZone]:
        """
        GET /dns_zones

        Args:
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get all DNS zones the user has access to

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(account_slug, type_utils.NotGiven):
            encode_query_param(
                _query,
                "account_slug",
                to_encodable(item=account_slug, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/dns_zones",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.DnsZone],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, zone_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DnsZone:
        """
        GET /dns_zones/{zone_id}

        Args:
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get a single DNS zone

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.get(zone_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/dns_zones/{zone_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DnsZone,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsZone:
        """
        POST /dns_zones

        Args:
            account_slug: str
            name: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.create()
        ```
        """
        _json = to_encodable(
            item={"account_slug": account_slug, "name": name, "site_id": site_id},
            dump_with=params._SerializerDnsZoneSetup,
        )
        return await self._base_client.request(
            method="POST",
            path="/dns_zones",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.DnsZone,
            request_options=request_options or default_request_options(),
        )
