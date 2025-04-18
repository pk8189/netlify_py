import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from netlify_py.types import models, params


class DnsRecordsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        dns_record_id: str,
        zone_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /dns_zones/{zone_id}/dns_records/{dns_record_id}

        Args:
            dns_record_id: str
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            record deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.dns_records.delete(dns_record_id="string", zone_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/dns_zones/{zone_id}/dns_records/{dns_record_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, zone_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DnsRecord]:
        """
        GET /dns_zones/{zone_id}/dns_records

        Args:
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get all DNS records for a single DNS zone

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.dns_records.list(zone_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/dns_zones/{zone_id}/dns_records",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DnsRecord],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        dns_record_id: str,
        zone_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsRecord:
        """
        GET /dns_zones/{zone_id}/dns_records/{dns_record_id}

        Args:
            dns_record_id: str
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get a single DNS record

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.dns_records.get(dns_record_id="string", zone_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/dns_zones/{zone_id}/dns_records/{dns_record_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DnsRecord,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        zone_id: str,
        flag: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hostname: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        port: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        priority: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tag: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ttl: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        weight: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsRecord:
        """
        POST /dns_zones/{zone_id}/dns_records

        Args:
            flag: int
            hostname: str
            port: int
            priority: int
            tag: str
            ttl: int
            type: str
            value: str
            weight: int
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dns_zones.dns_records.create(zone_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "flag": flag,
                "hostname": hostname,
                "port": port,
                "priority": priority,
                "tag": tag,
                "ttl": ttl,
                "type_": type_,
                "value": value,
                "weight": weight,
            },
            dump_with=params._SerializerDnsRecordCreate,
        )
        return self._base_client.request(
            method="POST",
            path=f"/dns_zones/{zone_id}/dns_records",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.DnsRecord,
            request_options=request_options or default_request_options(),
        )


class AsyncDnsRecordsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        dns_record_id: str,
        zone_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /dns_zones/{zone_id}/dns_records/{dns_record_id}

        Args:
            dns_record_id: str
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            record deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.dns_records.delete(
            dns_record_id="string", zone_id="string"
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/dns_zones/{zone_id}/dns_records/{dns_record_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, zone_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DnsRecord]:
        """
        GET /dns_zones/{zone_id}/dns_records

        Args:
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get all DNS records for a single DNS zone

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.dns_records.list(zone_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/dns_zones/{zone_id}/dns_records",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DnsRecord],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        dns_record_id: str,
        zone_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsRecord:
        """
        GET /dns_zones/{zone_id}/dns_records/{dns_record_id}

        Args:
            dns_record_id: str
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            get a single DNS record

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.dns_records.get(dns_record_id="string", zone_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/dns_zones/{zone_id}/dns_records/{dns_record_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DnsRecord,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        zone_id: str,
        flag: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hostname: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        port: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        priority: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tag: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ttl: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        weight: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DnsRecord:
        """
        POST /dns_zones/{zone_id}/dns_records

        Args:
            flag: int
            hostname: str
            port: int
            priority: int
            tag: str
            ttl: int
            type: str
            value: str
            weight: int
            zone_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dns_zones.dns_records.create(zone_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "flag": flag,
                "hostname": hostname,
                "port": port,
                "priority": priority,
                "tag": tag,
                "ttl": ttl,
                "type_": type_,
                "value": value,
                "weight": weight,
            },
            dump_with=params._SerializerDnsRecordCreate,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/dns_zones/{zone_id}/dns_records",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.DnsRecord,
            request_options=request_options or default_request_options(),
        )
