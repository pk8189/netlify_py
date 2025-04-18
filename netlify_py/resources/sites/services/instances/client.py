import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from netlify_py.types import models


class InstancesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        addon: str,
        instance_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/services/{addon}/instances/{instance_id}

        Args:
            addon: str
            instance_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.services.instances.delete(
            addon="string", instance_id="string", site_id="string"
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/services/{addon}/instances/{instance_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        addon: str,
        instance_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ServiceInstance:
        """
        GET /sites/{site_id}/services/{addon}/instances/{instance_id}

        Args:
            addon: str
            instance_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.services.instances.get(
            addon="string", instance_id="string", site_id="string"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/services/{addon}/instances/{instance_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.ServiceInstance,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        addon: str,
        data: typing.Dict[str, typing.Any],
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ServiceInstance:
        """
        POST /sites/{site_id}/services/{addon}/instances

        Args:
            addon: str
            data: typing.Dict[str, typing.Any]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.services.instances.create(
            addon="string", data={}, site_id="string"
        )
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/services/{addon}/instances",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.ServiceInstance,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        addon: str,
        data: typing.Dict[str, typing.Any],
        instance_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/services/{addon}/instances/{instance_id}

        Args:
            addon: str
            data: typing.Dict[str, typing.Any]
            instance_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.services.instances.update(
            addon="string", data={}, instance_id="string", site_id="string"
        )
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/services/{addon}/instances/{instance_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncInstancesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        addon: str,
        instance_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /sites/{site_id}/services/{addon}/instances/{instance_id}

        Args:
            addon: str
            instance_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.services.instances.delete(
            addon="string", instance_id="string", site_id="string"
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}/services/{addon}/instances/{instance_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        addon: str,
        instance_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ServiceInstance:
        """
        GET /sites/{site_id}/services/{addon}/instances/{instance_id}

        Args:
            addon: str
            instance_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.services.instances.get(
            addon="string", instance_id="string", site_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/services/{addon}/instances/{instance_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.ServiceInstance,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        addon: str,
        data: typing.Dict[str, typing.Any],
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ServiceInstance:
        """
        POST /sites/{site_id}/services/{addon}/instances

        Args:
            addon: str
            data: typing.Dict[str, typing.Any]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.services.instances.create(
            addon="string", data={}, site_id="string"
        )
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/services/{addon}/instances",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.ServiceInstance,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        addon: str,
        data: typing.Dict[str, typing.Any],
        instance_id: str,
        site_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        PUT /sites/{site_id}/services/{addon}/instances/{instance_id}

        Args:
            addon: str
            data: typing.Dict[str, typing.Any]
            instance_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.services.instances.update(
            addon="string", data={}, instance_id="string", site_id="string"
        )
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/services/{addon}/instances/{instance_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
