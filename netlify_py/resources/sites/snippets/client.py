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


class SnippetsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        site_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/snippets/{snippet_id}

        Args:
            site_id: str
            snippet_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.snippets.delete(site_id="string", snippet_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/snippets/{snippet_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Snippet]:
        """
        GET /sites/{site_id}/snippets

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
        client.sites.snippets.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/snippets",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Snippet],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        site_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Snippet:
        """
        GET /sites/{site_id}/snippets/{snippet_id}

        Args:
            site_id: str
            snippet_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.snippets.get(site_id="string", snippet_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/snippets/{snippet_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Snippet,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id_path: str,
        general: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        general_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Snippet:
        """
        POST /sites/{site_id}/snippets

        Args:
            general: str
            general_position: str
            goal: str
            goal_position: str
            id: int
            site_id: str
            title: str
            site_id_path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.snippets.create(site_id_path="string")
        ```
        """
        _json = to_encodable(
            item={
                "general": general,
                "general_position": general_position,
                "goal": goal,
                "goal_position": goal_position,
                "id": id,
                "site_id": site_id,
                "title": title,
            },
            dump_with=params._SerializerSnippet,
        )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id_path}/snippets",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Snippet,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        site_id_path: str,
        snippet_id: str,
        general: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        general_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/snippets/{snippet_id}

        Args:
            general: str
            general_position: str
            goal: str
            goal_position: str
            id: int
            site_id: str
            title: str
            site_id_path: str
            snippet_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.snippets.update(site_id_path="string", snippet_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "general": general,
                "general_position": general_position,
                "goal": goal,
                "goal_position": goal_position,
                "id": id,
                "site_id": site_id,
                "title": title,
            },
            dump_with=params._SerializerSnippet,
        )
        self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id_path}/snippets/{snippet_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncSnippetsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        site_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/snippets/{snippet_id}

        Args:
            site_id: str
            snippet_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.snippets.delete(site_id="string", snippet_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/snippets/{snippet_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Snippet]:
        """
        GET /sites/{site_id}/snippets

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
        await client.sites.snippets.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/snippets",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Snippet],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        site_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Snippet:
        """
        GET /sites/{site_id}/snippets/{snippet_id}

        Args:
            site_id: str
            snippet_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.snippets.get(site_id="string", snippet_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/snippets/{snippet_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Snippet,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id_path: str,
        general: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        general_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Snippet:
        """
        POST /sites/{site_id}/snippets

        Args:
            general: str
            general_position: str
            goal: str
            goal_position: str
            id: int
            site_id: str
            title: str
            site_id_path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.snippets.create(site_id_path="string")
        ```
        """
        _json = to_encodable(
            item={
                "general": general,
                "general_position": general_position,
                "goal": goal,
                "goal_position": goal_position,
                "id": id,
                "site_id": site_id,
                "title": title,
            },
            dump_with=params._SerializerSnippet,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id_path}/snippets",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Snippet,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        site_id_path: str,
        snippet_id: str,
        general: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        general_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        goal_position: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        site_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/snippets/{snippet_id}

        Args:
            general: str
            general_position: str
            goal: str
            goal_position: str
            id: int
            site_id: str
            title: str
            site_id_path: str
            snippet_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.snippets.update(site_id_path="string", snippet_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "general": general,
                "general_position": general_position,
                "goal": goal,
                "goal_position": goal_position,
                "id": id,
                "site_id": site_id,
                "title": title,
            },
            dump_with=params._SerializerSnippet,
        )
        await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id_path}/snippets/{snippet_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
