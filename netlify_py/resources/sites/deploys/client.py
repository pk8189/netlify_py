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
from netlify_py.resources.sites.deploys.restore import AsyncRestoreClient, RestoreClient
from netlify_py.types import models, params


class DeploysClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.restore = RestoreClient(base_client=self._base_client)

    def delete(
        self,
        *,
        deploy_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/deploys/{deploy_id}

        Args:
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.deploys.delete(deploy_id="string", site_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_previews: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latest_published: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        production: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "accepted",
                    "building",
                    "enqueued",
                    "error",
                    "new",
                    "pending_review",
                    "prepared",
                    "preparing",
                    "processed",
                    "processing",
                    "ready",
                    "rejected",
                    "retrying",
                    "uploaded",
                    "uploading",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Deploy]:
        """
        GET /sites/{site_id}/deploys

        Args:
            branch: str
            deploy-previews: bool
            latest-published: bool
            page: int
            per_page: int
            production: bool
            state: typing_extensions.Literal["accepted", "building", "enqueued", "error", "new", "pending_review", "prepared", "preparing", "processed", "processing", "ready", "rejected", "retrying", "uploaded", "uploading"]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.deploys.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(deploy_previews, type_utils.NotGiven):
            encode_query_param(
                _query,
                "deploy-previews",
                to_encodable(item=deploy_previews, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(latest_published, type_utils.NotGiven):
            encode_query_param(
                _query,
                "latest-published",
                to_encodable(item=latest_published, dump_with=bool),
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
        if not isinstance(production, type_utils.NotGiven):
            encode_query_param(
                _query,
                "production",
                to_encodable(item=production, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(state, type_utils.NotGiven):
            encode_query_param(
                _query,
                "state",
                to_encodable(
                    item=state,
                    dump_with=typing_extensions.Literal[
                        "accepted",
                        "building",
                        "enqueued",
                        "error",
                        "new",
                        "pending_review",
                        "prepared",
                        "preparing",
                        "processed",
                        "processing",
                        "ready",
                        "rejected",
                        "retrying",
                        "uploaded",
                        "uploading",
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/deploys",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Deploy],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        deploy_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        GET /sites/{site_id}/deploys/{deploy_id}

        Args:
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.deploys.get(deploy_id="string", site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id: str,
        async_: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_query: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_previews: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        draft: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        files: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        function_schedules: typing.Union[
            typing.Optional[typing.List[params.FunctionSchedule]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_config: typing.Union[
            typing.Optional[params.DeployFilesFunctionsConfig], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latest_published: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        production: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "accepted",
                    "building",
                    "enqueued",
                    "error",
                    "new",
                    "pending_review",
                    "prepared",
                    "preparing",
                    "processed",
                    "processing",
                    "ready",
                    "rejected",
                    "retrying",
                    "uploaded",
                    "uploading",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        POST /sites/{site_id}/deploys

        Args:
            async: bool
            branch: str
            branch_query: str
            deploy-previews: bool
            draft: bool
            files: typing.Dict[str, typing.Any]
            framework: str
            framework_version: str
            function_schedules: typing.List[FunctionSchedule]
            functions: typing.Dict[str, typing.Any]
            functions_config: DeployFilesFunctionsConfig
            latest-published: bool
            production: bool
            state: typing_extensions.Literal["accepted", "building", "enqueued", "error", "new", "pending_review", "prepared", "preparing", "processed", "processing", "ready", "rejected", "retrying", "uploaded", "uploading"]
            title: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.deploys.create(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch_query, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch_query, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(deploy_previews, type_utils.NotGiven):
            encode_query_param(
                _query,
                "deploy-previews",
                to_encodable(item=deploy_previews, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(latest_published, type_utils.NotGiven):
            encode_query_param(
                _query,
                "latest-published",
                to_encodable(item=latest_published, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(production, type_utils.NotGiven):
            encode_query_param(
                _query,
                "production",
                to_encodable(item=production, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(state, type_utils.NotGiven):
            encode_query_param(
                _query,
                "state",
                to_encodable(
                    item=state,
                    dump_with=typing_extensions.Literal[
                        "accepted",
                        "building",
                        "enqueued",
                        "error",
                        "new",
                        "pending_review",
                        "prepared",
                        "preparing",
                        "processed",
                        "processing",
                        "ready",
                        "rejected",
                        "retrying",
                        "uploaded",
                        "uploading",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(title, type_utils.NotGiven):
            encode_query_param(
                _query,
                "title",
                to_encodable(item=title, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "async_": async_,
                "branch": branch,
                "draft": draft,
                "files": files,
                "framework": framework,
                "framework_version": framework_version,
                "function_schedules": function_schedules,
                "functions": functions,
                "functions_config": functions_config,
            },
            dump_with=params._SerializerDeployFiles,
        )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/deploys",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        deploy_id: str,
        site_id: str,
        async_: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        draft: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        files: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        function_schedules: typing.Union[
            typing.Optional[typing.List[params.FunctionSchedule]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_config: typing.Union[
            typing.Optional[params.DeployFilesFunctionsConfig], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        PUT /sites/{site_id}/deploys/{deploy_id}

        Args:
            async: bool
            branch: str
            draft: bool
            files: typing.Dict[str, typing.Any]
            framework: str
            framework_version: str
            function_schedules: typing.List[FunctionSchedule]
            functions: typing.Dict[str, typing.Any]
            functions_config: DeployFilesFunctionsConfig
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.deploys.update(deploy_id="string", site_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "async_": async_,
                "branch": branch,
                "draft": draft,
                "files": files,
                "framework": framework,
                "framework_version": framework_version,
                "function_schedules": function_schedules,
                "functions": functions,
                "functions_config": functions_config,
            },
            dump_with=params._SerializerDeployFiles,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )


class AsyncDeploysClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.restore = AsyncRestoreClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        deploy_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/deploys/{deploy_id}

        Args:
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.deploys.delete(deploy_id="string", site_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_previews: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latest_published: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        production: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "accepted",
                    "building",
                    "enqueued",
                    "error",
                    "new",
                    "pending_review",
                    "prepared",
                    "preparing",
                    "processed",
                    "processing",
                    "ready",
                    "rejected",
                    "retrying",
                    "uploaded",
                    "uploading",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Deploy]:
        """
        GET /sites/{site_id}/deploys

        Args:
            branch: str
            deploy-previews: bool
            latest-published: bool
            page: int
            per_page: int
            production: bool
            state: typing_extensions.Literal["accepted", "building", "enqueued", "error", "new", "pending_review", "prepared", "preparing", "processed", "processing", "ready", "rejected", "retrying", "uploaded", "uploading"]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.deploys.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(deploy_previews, type_utils.NotGiven):
            encode_query_param(
                _query,
                "deploy-previews",
                to_encodable(item=deploy_previews, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(latest_published, type_utils.NotGiven):
            encode_query_param(
                _query,
                "latest-published",
                to_encodable(item=latest_published, dump_with=bool),
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
        if not isinstance(production, type_utils.NotGiven):
            encode_query_param(
                _query,
                "production",
                to_encodable(item=production, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(state, type_utils.NotGiven):
            encode_query_param(
                _query,
                "state",
                to_encodable(
                    item=state,
                    dump_with=typing_extensions.Literal[
                        "accepted",
                        "building",
                        "enqueued",
                        "error",
                        "new",
                        "pending_review",
                        "prepared",
                        "preparing",
                        "processed",
                        "processing",
                        "ready",
                        "rejected",
                        "retrying",
                        "uploaded",
                        "uploading",
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/deploys",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Deploy],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        deploy_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        GET /sites/{site_id}/deploys/{deploy_id}

        Args:
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.deploys.get(deploy_id="string", site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id: str,
        async_: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_query: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_previews: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        draft: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        files: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        function_schedules: typing.Union[
            typing.Optional[typing.List[params.FunctionSchedule]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_config: typing.Union[
            typing.Optional[params.DeployFilesFunctionsConfig], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latest_published: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        production: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "accepted",
                    "building",
                    "enqueued",
                    "error",
                    "new",
                    "pending_review",
                    "prepared",
                    "preparing",
                    "processed",
                    "processing",
                    "ready",
                    "rejected",
                    "retrying",
                    "uploaded",
                    "uploading",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        POST /sites/{site_id}/deploys

        Args:
            async: bool
            branch: str
            branch_query: str
            deploy-previews: bool
            draft: bool
            files: typing.Dict[str, typing.Any]
            framework: str
            framework_version: str
            function_schedules: typing.List[FunctionSchedule]
            functions: typing.Dict[str, typing.Any]
            functions_config: DeployFilesFunctionsConfig
            latest-published: bool
            production: bool
            state: typing_extensions.Literal["accepted", "building", "enqueued", "error", "new", "pending_review", "prepared", "preparing", "processed", "processing", "ready", "rejected", "retrying", "uploaded", "uploading"]
            title: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.deploys.create(site_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(branch_query, type_utils.NotGiven):
            encode_query_param(
                _query,
                "branch",
                to_encodable(item=branch_query, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(deploy_previews, type_utils.NotGiven):
            encode_query_param(
                _query,
                "deploy-previews",
                to_encodable(item=deploy_previews, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(latest_published, type_utils.NotGiven):
            encode_query_param(
                _query,
                "latest-published",
                to_encodable(item=latest_published, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(production, type_utils.NotGiven):
            encode_query_param(
                _query,
                "production",
                to_encodable(item=production, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(state, type_utils.NotGiven):
            encode_query_param(
                _query,
                "state",
                to_encodable(
                    item=state,
                    dump_with=typing_extensions.Literal[
                        "accepted",
                        "building",
                        "enqueued",
                        "error",
                        "new",
                        "pending_review",
                        "prepared",
                        "preparing",
                        "processed",
                        "processing",
                        "ready",
                        "rejected",
                        "retrying",
                        "uploaded",
                        "uploading",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(title, type_utils.NotGiven):
            encode_query_param(
                _query,
                "title",
                to_encodable(item=title, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "async_": async_,
                "branch": branch,
                "draft": draft,
                "files": files,
                "framework": framework,
                "framework_version": framework_version,
                "function_schedules": function_schedules,
                "functions": functions,
                "functions_config": functions_config,
            },
            dump_with=params._SerializerDeployFiles,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/deploys",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        deploy_id: str,
        site_id: str,
        async_: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        draft: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        files: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        framework_version: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        function_schedules: typing.Union[
            typing.Optional[typing.List[params.FunctionSchedule]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_config: typing.Union[
            typing.Optional[params.DeployFilesFunctionsConfig], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Deploy:
        """
        PUT /sites/{site_id}/deploys/{deploy_id}

        Args:
            async: bool
            branch: str
            draft: bool
            files: typing.Dict[str, typing.Any]
            framework: str
            framework_version: str
            function_schedules: typing.List[FunctionSchedule]
            functions: typing.Dict[str, typing.Any]
            functions_config: DeployFilesFunctionsConfig
            deploy_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.deploys.update(deploy_id="string", site_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "async_": async_,
                "branch": branch,
                "draft": draft,
                "files": files,
                "framework": framework,
                "framework_version": framework_version,
                "function_schedules": function_schedules,
                "functions": functions,
                "functions_config": functions_config,
            },
            dump_with=params._SerializerDeployFiles,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/deploys/{deploy_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Deploy,
            request_options=request_options or default_request_options(),
        )
