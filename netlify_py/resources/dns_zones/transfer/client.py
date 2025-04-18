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


class TransferClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def update(
        self,
        *,
        account_id: str,
        transfer_account_id: str,
        transfer_user_id: str,
        zone_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsZone:
        """
        PUT /dns_zones/{zone_id}/transfer

        Args:
            account_id: the account of the dns zone
            transfer_account_id: the account you want to transfer the dns zone to
            transfer_user_id: the user you want to transfer the dns zone to
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            transfer a DNS zone to another account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.transfer.update(
            account_id="string",
            transfer_account_id="string",
            transfer_user_id="string",
            zone_id="string",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "account_id",
            to_encodable(item=account_id, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "transfer_account_id",
            to_encodable(item=transfer_account_id, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "transfer_user_id",
            to_encodable(item=transfer_user_id, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/dns_zones/{zone_id}/transfer",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.DnsZone,
            request_options=request_options or default_request_options(),
        )


class AsyncTransferClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def update(
        self,
        *,
        account_id: str,
        transfer_account_id: str,
        transfer_user_id: str,
        zone_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsZone:
        """
        PUT /dns_zones/{zone_id}/transfer

        Args:
            account_id: the account of the dns zone
            transfer_account_id: the account you want to transfer the dns zone to
            transfer_user_id: the user you want to transfer the dns zone to
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            transfer a DNS zone to another account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.transfer.update(
            account_id="string",
            transfer_account_id="string",
            transfer_user_id="string",
            zone_id="string",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "account_id",
            to_encodable(item=account_id, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "transfer_account_id",
            to_encodable(item=transfer_account_id, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "transfer_user_id",
            to_encodable(item=transfer_user_id, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/dns_zones/{zone_id}/transfer",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.DnsZone,
            request_options=request_options or default_request_options(),
        )
