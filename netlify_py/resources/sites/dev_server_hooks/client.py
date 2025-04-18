import typing
import typing_extensions

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from netlify_py.types import models, params


class DevServerHooksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/dev_server_hooks/{id}

        Args:
            id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.dev_server_hooks.delete(id="string", site_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/dev_server_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DevServerHook]:
        """
        GET /sites/{site_id}/dev_server_hooks

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
        client.sites.dev_server_hooks.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dev_server_hooks",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DevServerHook],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevServerHook:
        """
        GET /sites/{site_id}/dev_server_hooks/{id}

        Args:
            id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.dev_server_hooks.get(id="string", site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dev_server_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DevServerHook,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal["content_refresh", "new_dev_server"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevServerHook:
        """
        POST /sites/{site_id}/dev_server_hooks

        Args:
            branch: str
            title: str
            type: typing_extensions.Literal["content_refresh", "new_dev_server"]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.dev_server_hooks.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title, "type_": type_},
            dump_with=params._SerializerDevServerHookSetup,
        )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/dev_server_hooks",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.DevServerHook,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal["content_refresh", "new_dev_server"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/dev_server_hooks/{id}

        Args:
            branch: str
            title: str
            type: typing_extensions.Literal["content_refresh", "new_dev_server"]
            id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.dev_server_hooks.update(id="string", site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title, "type_": type_},
            dump_with=params._SerializerDevServerHookSetup,
        )
        self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/dev_server_hooks/{id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncDevServerHooksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/dev_server_hooks/{id}

        Args:
            id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.dev_server_hooks.delete(id="string", site_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/dev_server_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.DevServerHook]:
        """
        GET /sites/{site_id}/dev_server_hooks

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
        await client.sites.dev_server_hooks.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dev_server_hooks",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.DevServerHook],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevServerHook:
        """
        GET /sites/{site_id}/dev_server_hooks/{id}

        Args:
            id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.dev_server_hooks.get(id="string", site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/dev_server_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=models.DevServerHook,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal["content_refresh", "new_dev_server"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevServerHook:
        """
        POST /sites/{site_id}/dev_server_hooks

        Args:
            branch: str
            title: str
            type: typing_extensions.Literal["content_refresh", "new_dev_server"]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.dev_server_hooks.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title, "type_": type_},
            dump_with=params._SerializerDevServerHookSetup,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/dev_server_hooks",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.DevServerHook,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        site_id: str,
        branch: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal["content_refresh", "new_dev_server"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/dev_server_hooks/{id}

        Args:
            branch: str
            title: str
            type: typing_extensions.Literal["content_refresh", "new_dev_server"]
            id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.dev_server_hooks.update(id="string", site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title, "type_": type_},
            dump_with=params._SerializerDevServerHookSetup,
        )
        await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/dev_server_hooks/{id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
