import typing

from netlify_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from netlify_py.resources.sites.traffic_splits.publish import (
    AsyncPublishClient,
    PublishClient,
)
from netlify_py.resources.sites.traffic_splits.unpublish import (
    AsyncUnpublishClient,
    UnpublishClient,
)
from netlify_py.types import models, params


class TrafficSplitsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.publish = PublishClient(base_client=self._base_client)
        self.unpublish = UnpublishClient(base_client=self._base_client)

    def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.SplitTest]:
        """
        GET /sites/{site_id}/traffic_splits

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            split_tests

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.traffic_splits.list(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/traffic_splits",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.SplitTest],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        site_id: str,
        split_test_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SplitTest:
        """
        GET /sites/{site_id}/traffic_splits/{split_test_id}

        Args:
            site_id: str
            split_test_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            split_test

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.traffic_splits.get(site_id="string", split_test_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/traffic_splits/{split_test_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.SplitTest,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        site_id: str,
        branch_tests: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SplitTest:
        """
        POST /sites/{site_id}/traffic_splits

        Args:
            branch_tests: typing.Dict[str, typing.Any]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.traffic_splits.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch_tests": branch_tests},
            dump_with=params._SerializerSplitTestSetup,
        )
        return self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/traffic_splits",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.SplitTest,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        site_id: str,
        split_test_id: str,
        branch_tests: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SplitTest:
        """
        PUT /sites/{site_id}/traffic_splits/{split_test_id}

        Args:
            branch_tests: typing.Dict[str, typing.Any]
            site_id: str
            split_test_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.traffic_splits.update(site_id="string", split_test_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch_tests": branch_tests},
            dump_with=params._SerializerSplitTestSetup,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/traffic_splits/{split_test_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.SplitTest,
            request_options=request_options or default_request_options(),
        )


class AsyncTrafficSplitsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.publish = AsyncPublishClient(base_client=self._base_client)
        self.unpublish = AsyncUnpublishClient(base_client=self._base_client)

    async def list(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.SplitTest]:
        """
        GET /sites/{site_id}/traffic_splits

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            split_tests

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.traffic_splits.list(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/traffic_splits",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.SplitTest],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        site_id: str,
        split_test_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SplitTest:
        """
        GET /sites/{site_id}/traffic_splits/{split_test_id}

        Args:
            site_id: str
            split_test_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            split_test

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.traffic_splits.get(site_id="string", split_test_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}/traffic_splits/{split_test_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.SplitTest,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        site_id: str,
        branch_tests: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SplitTest:
        """
        POST /sites/{site_id}/traffic_splits

        Args:
            branch_tests: typing.Dict[str, typing.Any]
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.traffic_splits.create(site_id="string")
        ```
        """
        _json = to_encodable(
            item={"branch_tests": branch_tests},
            dump_with=params._SerializerSplitTestSetup,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/sites/{site_id}/traffic_splits",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.SplitTest,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        site_id: str,
        split_test_id: str,
        branch_tests: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SplitTest:
        """
        PUT /sites/{site_id}/traffic_splits/{split_test_id}

        Args:
            branch_tests: typing.Dict[str, typing.Any]
            site_id: str
            split_test_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.traffic_splits.update(
            site_id="string", split_test_id="string"
        )
        ```
        """
        _json = to_encodable(
            item={"branch_tests": branch_tests},
            dump_with=params._SerializerSplitTestSetup,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/sites/{site_id}/traffic_splits/{split_test_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.SplitTest,
            request_options=request_options or default_request_options(),
        )
