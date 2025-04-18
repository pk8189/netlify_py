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


class StartClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        build_id: str,
        build_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        buildbot_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        POST /builds/{build_id}/start

        Args:
            build_version: str
            buildbot_version: str
            build_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.builds.start.create(build_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(build_version, type_utils.NotGiven):
            encode_query_param(
                _query,
                "build_version",
                to_encodable(item=build_version, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(buildbot_version, type_utils.NotGiven):
            encode_query_param(
                _query,
                "buildbot_version",
                to_encodable(item=buildbot_version, dump_with=str),
                style="form",
                explode=True,
            )
        self._base_client.request(
            method="POST",
            path=f"/builds/{build_id}/start",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncStartClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        build_id: str,
        build_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        buildbot_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        POST /builds/{build_id}/start

        Args:
            build_version: str
            buildbot_version: str
            build_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.builds.start.create(build_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(build_version, type_utils.NotGiven):
            encode_query_param(
                _query,
                "build_version",
                to_encodable(item=build_version, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(buildbot_version, type_utils.NotGiven):
            encode_query_param(
                _query,
                "buildbot_version",
                to_encodable(item=buildbot_version, dump_with=str),
                style="form",
                explode=True,
            )
        await self._base_client.request(
            method="POST",
            path=f"/builds/{build_id}/start",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
