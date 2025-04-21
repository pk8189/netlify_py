import typing
import typing_extensions

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


class EnvClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        site_id: str,
        context_name: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "all", "branch-deploy", "deploy-preview", "dev", "production"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        scope: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "builds", "functions", "post_processing", "runtime"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.EnvVar]:
        """
        Returns all environment variables for a site. This convenience method behaves the same as `getEnvVars` but doesn't require an `account_id` as input.

        GET /api/v1/sites/{site_id}/env

        Args:
            context_name: Filter by deploy context
            scope: Filter by scope
            site_id: Scope response to site_id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.env.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(context_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "context_name",
                to_encodable(
                    item=context_name,
                    dump_with=typing_extensions.Literal[
                        "all", "branch-deploy", "deploy-preview", "dev", "production"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(scope, type_utils.NotGiven):
            encode_query_param(
                _query,
                "scope",
                to_encodable(
                    item=scope,
                    dump_with=typing_extensions.Literal[
                        "builds", "functions", "post_processing", "runtime"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/api/v1/sites/{site_id}/env",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.EnvVar],
            request_options=request_options or default_request_options(),
        )


class AsyncEnvClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        site_id: str,
        context_name: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "all", "branch-deploy", "deploy-preview", "dev", "production"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        scope: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "builds", "functions", "post_processing", "runtime"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.EnvVar]:
        """
        Returns all environment variables for a site. This convenience method behaves the same as `getEnvVars` but doesn't require an `account_id` as input.

        GET /api/v1/sites/{site_id}/env

        Args:
            context_name: Filter by deploy context
            scope: Filter by scope
            site_id: Scope response to site_id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.env.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(context_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "context_name",
                to_encodable(
                    item=context_name,
                    dump_with=typing_extensions.Literal[
                        "all", "branch-deploy", "deploy-preview", "dev", "production"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(scope, type_utils.NotGiven):
            encode_query_param(
                _query,
                "scope",
                to_encodable(
                    item=scope,
                    dump_with=typing_extensions.Literal[
                        "builds", "functions", "post_processing", "runtime"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/api/v1/sites/{site_id}/env",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.EnvVar],
            request_options=request_options or default_request_options(),
        )
