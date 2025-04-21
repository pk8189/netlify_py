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
from netlify_py.types import models, params


class EnvVarsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        account_id: str,
        key: str,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes an environment variable

        DELETE /accounts/{account_id}/env/{key}

        Args:
            site_id: If provided, delete the environment variable from this site
            account_id: Scope response to account_id
            key: The environment variable key (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content (success)

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.env_vars.delete(account_id="string", key="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        self._base_client.request(
            method="DELETE",
            path=f"/accounts/{account_id}/env/{key}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def delete_value(
        self,
        *,
        account_id: str,
        id: str,
        key: str,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific environment variable value.

        DELETE /accounts/{account_id}/env/{key}/value/{id}

        Args:
            site_id: If provided, delete the value from an environment variable on this site
            account_id: Scope response to account_id
            id: The environment variable value's ID
            key: The environment variable key name (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content (success)

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.env_vars.delete_value(
            account_id="string", id="string", key="string"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        self._base_client.request(
            method="DELETE",
            path=f"/accounts/{account_id}/env/{key}/value/{id}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        account_id: str,
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
                    "builds", "functions", "post-processing", "runtime"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.EnvVar]:
        """
        Returns all environment variables for an account or site. An account corresponds to a team in the Netlify UI.

        GET /accounts/{account_id}/env

        Args:
            context_name: Filter by deploy context
            scope: Filter by scope
            site_id: If specified, only return environment variables set on this site
            account_id: Scope response to account_id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.env_vars.list(account_id="string")
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
                        "builds", "functions", "post-processing", "runtime"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}/env",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.EnvVar],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account_id: str,
        key: str,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EnvVar:
        """
        Returns an individual environment variable.

        GET /accounts/{account_id}/env/{key}

        Args:
            site_id: If provided, return the environment variable for a specific site (no merging is performed)
            account_id: Scope response to account_id
            key: The environment variable key (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.env_vars.get(account_id="string", key="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}/env/{key}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.EnvVar,
            request_options=request_options or default_request_options(),
        )

    def set(
        self,
        *,
        account_id: str,
        key: str,
        context: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "all",
                    "branch",
                    "branch-deploy",
                    "deploy-preview",
                    "dev",
                    "production",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        context_parameter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EnvVar:
        """
        Updates or creates a new value for an existing environment variable.

        PATCH /accounts/{account_id}/env/{key}

        Args:
            context: The deploy context in which this value will be used. `dev` refers to local development when running `netlify dev`. `branch` must be provided with a value in `context_parameter`.
            context_parameter: An additional parameter for custom branches. Currently, this is used for providing a branch name when `context=branch`.
            site_id: If provided, update an environment variable set on this site
            value: The environment variable's unencrypted value
            account_id: Scope response to account_id
            key: The existing environment variable key name (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            Created (success)

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.env_vars.set(account_id="string", key="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "context": context,
                "context_parameter": context_parameter,
                "value": value,
            },
            dump_with=params._SerializerAccountsEnvVarsSetBody,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/accounts/{account_id}/env/{key}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.EnvVar,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account_id: str,
        data: typing.List[params.AccountsEnvVarsCreateBodyItem],
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.EnvVar]:
        """
        Creates new environment variables. Granular scopes are available on Pro plans and above.

        POST /accounts/{account_id}/env

        Args:
            site_id: If provided, create an environment variable on the site level, not the account level
            account_id: Scope response to account_id
            data: typing.List[AccountsEnvVarsCreateBodyItem]
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.env_vars.create(account_id="string", data=[{}])
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item=data,
            dump_with=typing.List[params._SerializerAccountsEnvVarsCreateBodyItem],
        )
        return self._base_client.request(
            method="POST",
            path=f"/accounts/{account_id}/env",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=typing.List[models.EnvVar],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        account_id: str,
        key_path: str,
        is_secret: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        scopes: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "builds", "functions", "post-processing", "runtime"
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        values: typing.Union[
            typing.Optional[typing.List[params.EnvVarValue]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EnvVar:
        """
        Updates an existing environment variable and all of its values. Existing values will be replaced by values provided.

        PUT /accounts/{account_id}/env/{key}

        Args:
            is_secret: Secret values are only readable by code running on Netlify's systems. With secrets, only the local development context values are readable from the UI, API, and CLI. By default, environment variable values are not secret.
            key: The existing or new name of the key, if you wish to rename it (case-sensitive)
            scopes: The scopes that this environment variable is set to (Pro plans and above)
            site_id: If provided, update an environment variable set on this site
            values: typing.List[EnvVarValue]
            account_id: Scope response to account_id
            key_path: The existing environment variable key name (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.env_vars.update(account_id="string", key_path="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "is_secret": is_secret,
                "key": key,
                "scopes": scopes,
                "values": values,
            },
            dump_with=params._SerializerAccountsEnvVarsUpdateBody,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/accounts/{account_id}/env/{key_path}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.EnvVar,
            request_options=request_options or default_request_options(),
        )


class AsyncEnvVarsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        account_id: str,
        key: str,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes an environment variable

        DELETE /accounts/{account_id}/env/{key}

        Args:
            site_id: If provided, delete the environment variable from this site
            account_id: Scope response to account_id
            key: The environment variable key (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content (success)

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.env_vars.delete(account_id="string", key="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        await self._base_client.request(
            method="DELETE",
            path=f"/accounts/{account_id}/env/{key}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def delete_value(
        self,
        *,
        account_id: str,
        id: str,
        key: str,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific environment variable value.

        DELETE /accounts/{account_id}/env/{key}/value/{id}

        Args:
            site_id: If provided, delete the value from an environment variable on this site
            account_id: Scope response to account_id
            id: The environment variable value's ID
            key: The environment variable key name (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content (success)

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.env_vars.delete_value(
            account_id="string", id="string", key="string"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        await self._base_client.request(
            method="DELETE",
            path=f"/accounts/{account_id}/env/{key}/value/{id}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        account_id: str,
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
                    "builds", "functions", "post-processing", "runtime"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.EnvVar]:
        """
        Returns all environment variables for an account or site. An account corresponds to a team in the Netlify UI.

        GET /accounts/{account_id}/env

        Args:
            context_name: Filter by deploy context
            scope: Filter by scope
            site_id: If specified, only return environment variables set on this site
            account_id: Scope response to account_id
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.env_vars.list(account_id="string")
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
                        "builds", "functions", "post-processing", "runtime"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}/env",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.EnvVar],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account_id: str,
        key: str,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EnvVar:
        """
        Returns an individual environment variable.

        GET /accounts/{account_id}/env/{key}

        Args:
            site_id: If provided, return the environment variable for a specific site (no merging is performed)
            account_id: Scope response to account_id
            key: The environment variable key (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.env_vars.get(account_id="string", key="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}/env/{key}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=models.EnvVar,
            request_options=request_options or default_request_options(),
        )

    async def set(
        self,
        *,
        account_id: str,
        key: str,
        context: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "all",
                    "branch",
                    "branch-deploy",
                    "deploy-preview",
                    "dev",
                    "production",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        context_parameter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EnvVar:
        """
        Updates or creates a new value for an existing environment variable.

        PATCH /accounts/{account_id}/env/{key}

        Args:
            context: The deploy context in which this value will be used. `dev` refers to local development when running `netlify dev`. `branch` must be provided with a value in `context_parameter`.
            context_parameter: An additional parameter for custom branches. Currently, this is used for providing a branch name when `context=branch`.
            site_id: If provided, update an environment variable set on this site
            value: The environment variable's unencrypted value
            account_id: Scope response to account_id
            key: The existing environment variable key name (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            Created (success)

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.env_vars.set(account_id="string", key="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "context": context,
                "context_parameter": context_parameter,
                "value": value,
            },
            dump_with=params._SerializerAccountsEnvVarsSetBody,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/accounts/{account_id}/env/{key}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.EnvVar,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account_id: str,
        data: typing.List[params.AccountsEnvVarsCreateBodyItem],
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.EnvVar]:
        """
        Creates new environment variables. Granular scopes are available on Pro plans and above.

        POST /accounts/{account_id}/env

        Args:
            site_id: If provided, create an environment variable on the site level, not the account level
            account_id: Scope response to account_id
            data: typing.List[AccountsEnvVarsCreateBodyItem]
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.env_vars.create(account_id="string", data=[{}])
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item=data,
            dump_with=typing.List[params._SerializerAccountsEnvVarsCreateBodyItem],
        )
        return await self._base_client.request(
            method="POST",
            path=f"/accounts/{account_id}/env",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=typing.List[models.EnvVar],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        account_id: str,
        key_path: str,
        is_secret: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        scopes: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "builds", "functions", "post-processing", "runtime"
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        values: typing.Union[
            typing.Optional[typing.List[params.EnvVarValue]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EnvVar:
        """
        Updates an existing environment variable and all of its values. Existing values will be replaced by values provided.

        PUT /accounts/{account_id}/env/{key}

        Args:
            is_secret: Secret values are only readable by code running on Netlify's systems. With secrets, only the local development context values are readable from the UI, API, and CLI. By default, environment variable values are not secret.
            key: The existing or new name of the key, if you wish to rename it (case-sensitive)
            scopes: The scopes that this environment variable is set to (Pro plans and above)
            site_id: If provided, update an environment variable set on this site
            values: typing.List[EnvVarValue]
            account_id: Scope response to account_id
            key_path: The existing environment variable key name (case-sensitive)
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.env_vars.update(account_id="string", key_path="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(site_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "site_id",
                to_encodable(item=site_id, dump_with=str),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "is_secret": is_secret,
                "key": key,
                "scopes": scopes,
                "values": values,
            },
            dump_with=params._SerializerAccountsEnvVarsUpdateBody,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/accounts/{account_id}/env/{key_path}",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.EnvVar,
            request_options=request_options or default_request_options(),
        )
