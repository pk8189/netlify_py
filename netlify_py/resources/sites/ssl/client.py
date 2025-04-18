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
from netlify_py.resources.sites.ssl.certificates import (
    AsyncCertificatesClient,
    CertificatesClient,
)
from netlify_py.types import models


class SslClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.certificates = CertificatesClient(base_client=self._base_client)

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SniCertificate:
        """
        GET /sites/{site_id}/ssl

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
        client.sites.ssl.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/ssl",
            auth_names=["netlifyAuth"],
            cast_to=models.SniCertificate,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id: str,
        ca_certificates: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        certificate: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SniCertificate:
        """
        POST /sites/{site_id}/ssl

        Args:
            ca_certificates: str
            certificate: str
            key: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.ssl.create(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(ca_certificates, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ca_certificates",
                to_encodable(item=ca_certificates, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(certificate, type_utils.NotGiven):
            encode_query_param(
                _query,
                "certificate",
                to_encodable(item=certificate, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(key, type_utils.NotGiven):
            encode_query_param(
                _query,
                "key",
                to_encodable(item=key, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/ssl",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.SniCertificate,
            request_options=request_options or default_request_options(),
        )


class AsyncSslClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.certificates = AsyncCertificatesClient(base_client=self._base_client)

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.SniCertificate:
        """
        GET /sites/{site_id}/ssl

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
        await client.sites.ssl.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/ssl",
            auth_names=["netlifyAuth"],
            cast_to=models.SniCertificate,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id: str,
        ca_certificates: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        certificate: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SniCertificate:
        """
        POST /sites/{site_id}/ssl

        Args:
            ca_certificates: str
            certificate: str
            key: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.ssl.create(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(ca_certificates, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ca_certificates",
                to_encodable(item=ca_certificates, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(certificate, type_utils.NotGiven):
            encode_query_param(
                _query,
                "certificate",
                to_encodable(item=certificate, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(key, type_utils.NotGiven):
            encode_query_param(
                _query,
                "key",
                to_encodable(item=key, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/ssl",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.SniCertificate,
            request_options=request_options or default_request_options(),
        )
