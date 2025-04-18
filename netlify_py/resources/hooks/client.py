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
from netlify_py.resources.hooks.types import AsyncTypesClient, TypesClient
from netlify_py.types import models, params


class HooksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.types = TypesClient(base_client=self._base_client)

    def delete(
        self, *, hook_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /hooks/{hook_id}

        Args:
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hooks.delete(hook_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/hooks/{hook_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Hook]:
        """
        GET /hooks

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
        client.hooks.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "site_id",
            to_encodable(item=site_id, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="GET",
            path="/hooks",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Hook],
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, hook_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Hook:
        """
        GET /hooks/{hook_id}

        Args:
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hooks.get(hook_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/hooks/{hook_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id_query: str,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        data: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Hook:
        """
        POST /hooks

        Args:
            created_at: str
            data: typing.Dict[str, typing.Any]
            disabled: bool
            event: str
            id: str
            site_id: str
            type: str
            updated_at: str
            site_id_query: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hooks.create(site_id_query="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "site_id",
            to_encodable(item=site_id_query, dump_with=str),
            style="form",
            explode=True,
        )
        _json = to_encodable(
            item={
                "created_at": created_at,
                "data": data,
                "disabled": disabled,
                "event": event,
                "id": id,
                "site_id": site_id,
                "type_": type_,
                "updated_at": updated_at,
            },
            dump_with=params._SerializerHook,
        )
        return self._base_client.request(
            method="POST",
            path="/hooks",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )

    def enable(
        self, *, hook_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Hook:
        """
        POST /hooks/{hook_id}/enable

        Args:
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hooks.enable(hook_id="string")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/hooks/{hook_id}/enable",
            auth_names=["netlifyAuth"],
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        hook_id: str,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        data: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Hook:
        """
        PUT /hooks/{hook_id}

        Args:
            created_at: str
            data: typing.Dict[str, typing.Any]
            disabled: bool
            event: str
            id: str
            site_id: str
            type: str
            updated_at: str
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.hooks.update(hook_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "created_at": created_at,
                "data": data,
                "disabled": disabled,
                "event": event,
                "id": id,
                "site_id": site_id,
                "type_": type_,
                "updated_at": updated_at,
            },
            dump_with=params._SerializerHook,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/hooks/{hook_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )


class AsyncHooksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.types = AsyncTypesClient(base_client=self._base_client)

    async def delete(
        self, *, hook_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /hooks/{hook_id}

        Args:
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hooks.delete(hook_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/hooks/{hook_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Hook]:
        """
        GET /hooks

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
        await client.hooks.list(site_id="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "site_id",
            to_encodable(item=site_id, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="GET",
            path="/hooks",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Hook],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, hook_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Hook:
        """
        GET /hooks/{hook_id}

        Args:
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hooks.get(hook_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/hooks/{hook_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id_query: str,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        data: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Hook:
        """
        POST /hooks

        Args:
            created_at: str
            data: typing.Dict[str, typing.Any]
            disabled: bool
            event: str
            id: str
            site_id: str
            type: str
            updated_at: str
            site_id_query: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hooks.create(site_id_query="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "site_id",
            to_encodable(item=site_id_query, dump_with=str),
            style="form",
            explode=True,
        )
        _json = to_encodable(
            item={
                "created_at": created_at,
                "data": data,
                "disabled": disabled,
                "event": event,
                "id": id,
                "site_id": site_id,
                "type_": type_,
                "updated_at": updated_at,
            },
            dump_with=params._SerializerHook,
        )
        return await self._base_client.request(
            method="POST",
            path="/hooks",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )

    async def enable(
        self, *, hook_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Hook:
        """
        POST /hooks/{hook_id}/enable

        Args:
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hooks.enable(hook_id="string")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/hooks/{hook_id}/enable",
            auth_names=["netlifyAuth"],
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        hook_id: str,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        data: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Hook:
        """
        PUT /hooks/{hook_id}

        Args:
            created_at: str
            data: typing.Dict[str, typing.Any]
            disabled: bool
            event: str
            id: str
            site_id: str
            type: str
            updated_at: str
            hook_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.hooks.update(hook_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "created_at": created_at,
                "data": data,
                "disabled": disabled,
                "event": event,
                "id": id,
                "site_id": site_id,
                "type_": type_,
                "updated_at": updated_at,
            },
            dump_with=params._SerializerHook,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/hooks/{hook_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Hook,
            request_options=request_options or default_request_options(),
        )
