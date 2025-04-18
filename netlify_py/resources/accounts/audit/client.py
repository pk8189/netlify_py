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


class AuditClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        account_id: str,
        log_type: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        query: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.AuditLog]:
        """
        GET /accounts/{account_id}/audit

        Args:
            log_type: str
            page: int
            per_page: int
            query: str
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.audit.list(account_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(log_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "log_type",
                to_encodable(item=log_type, dump_with=str),
                style="form",
                explode=True,
            )
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
        if not isinstance(query, type_utils.NotGiven):
            encode_query_param(
                _query,
                "query",
                to_encodable(item=query, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}/audit",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.AuditLog],
            request_options=request_options or default_request_options(),
        )


class AsyncAuditClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        account_id: str,
        log_type: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        query: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.AuditLog]:
        """
        GET /accounts/{account_id}/audit

        Args:
            log_type: str
            page: int
            per_page: int
            query: str
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.audit.list(account_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(log_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "log_type",
                to_encodable(item=log_type, dump_with=str),
                style="form",
                explode=True,
            )
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
        if not isinstance(query, type_utils.NotGiven):
            encode_query_param(
                _query,
                "query",
                to_encodable(item=query, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}/audit",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.AuditLog],
            request_options=request_options or default_request_options(),
        )
