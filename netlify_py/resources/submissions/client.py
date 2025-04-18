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


class SubmissionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        submission_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /submissions/{submission_id}

        Args:
            submission_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.submissions.delete(submission_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/submissions/{submission_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        submission_id: str,
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
    ) -> typing.List[models.Submission]:
        """
        GET /submissions/{submission_id}

        Args:
            page: int
            per_page: int
            query: str
            submission_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.submissions.get(submission_id="string")
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
            path=f"/submissions/{submission_id}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Submission],
            request_options=request_options or default_request_options(),
        )


class AsyncSubmissionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        submission_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /submissions/{submission_id}

        Args:
            submission_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.submissions.delete(submission_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/submissions/{submission_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        submission_id: str,
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
    ) -> typing.List[models.Submission]:
        """
        GET /submissions/{submission_id}

        Args:
            page: int
            per_page: int
            query: str
            submission_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.submissions.get(submission_id="string")
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
            path=f"/submissions/{submission_id}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Submission],
            request_options=request_options or default_request_options(),
        )
