import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from netlify_py.types import models, params


class BuildHooksClient:
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
        DELETE /sites/{site_id}/build_hooks/{id}

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
        client.sites.build_hooks.delete(id="string", site_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/build_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.BuildHook]:
        """
        GET /sites/{site_id}/build_hooks

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
        client.sites.build_hooks.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/build_hooks",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.BuildHook],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BuildHook:
        """
        GET /sites/{site_id}/build_hooks/{id}

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
        client.sites.build_hooks.get(id="string", site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/build_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=models.BuildHook,
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BuildHook:
        """
        POST /sites/{site_id}/build_hooks

        Args:
            branch: str
            title: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.build_hooks.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title},
            dump_with=params._SerializerBuildHookSetup,
        )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/build_hooks",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.BuildHook,
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/build_hooks/{id}

        Args:
            branch: str
            title: str
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
        client.sites.build_hooks.update(id="string", site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title},
            dump_with=params._SerializerBuildHookSetup,
        )
        self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/build_hooks/{id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncBuildHooksClient:
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
        DELETE /sites/{site_id}/build_hooks/{id}

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
        await client.sites.build_hooks.delete(id="string", site_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/build_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.BuildHook]:
        """
        GET /sites/{site_id}/build_hooks

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
        await client.sites.build_hooks.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/build_hooks",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.BuildHook],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BuildHook:
        """
        GET /sites/{site_id}/build_hooks/{id}

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
        await client.sites.build_hooks.get(id="string", site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/build_hooks/{id}",
            auth_names=["netlifyAuth"],
            cast_to=models.BuildHook,
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BuildHook:
        """
        POST /sites/{site_id}/build_hooks

        Args:
            branch: str
            title: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.build_hooks.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title},
            dump_with=params._SerializerBuildHookSetup,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/build_hooks",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.BuildHook,
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/build_hooks/{id}

        Args:
            branch: str
            title: str
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
        await client.sites.build_hooks.update(id="string", site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch": branch, "title": title},
            dump_with=params._SerializerBuildHookSetup,
        )
        await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/build_hooks/{id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
