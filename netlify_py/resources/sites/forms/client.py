import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from netlify_py.types import models


class FormsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        form_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/forms/{form_id}

        Args:
            form_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.forms.delete(form_id="string", site_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/forms/{form_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Form]:
        """
        GET /sites/{site_id}/forms

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
        client.sites.forms.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/forms",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Form],
            request_options=request_options or default_request_options(),
        )


class AsyncFormsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        form_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/forms/{form_id}

        Args:
            form_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.forms.delete(form_id="string", site_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/forms/{form_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.Form]:
        """
        GET /sites/{site_id}/forms

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
        await client.sites.forms.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/forms",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Form],
            request_options=request_options or default_request_options(),
        )
