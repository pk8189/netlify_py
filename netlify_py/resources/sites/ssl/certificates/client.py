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


class CertificatesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        domain: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.SniCertificate]:
        """
        GET /sites/{site_id}/ssl/certificates

        Args:
            domain: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Array of SNI Certificates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.ssl.certificates.list(domain="string", site_id="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "domain",
            to_encodable(item=domain, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/ssl/certificates",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.SniCertificate],
            request_options=request_options or default_request_options(),
        )


class AsyncCertificatesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        domain: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.SniCertificate]:
        """
        GET /sites/{site_id}/ssl/certificates

        Args:
            domain: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Array of SNI Certificates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.ssl.certificates.list(domain="string", site_id="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "domain",
            to_encodable(item=domain, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/ssl/certificates",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.SniCertificate],
            request_options=request_options or default_request_options(),
        )
