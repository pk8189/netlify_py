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


class MembersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        account_slug: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /{account_slug}/members/{member_id}

        Args:
            account_slug: str
            member_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Not Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.members.delete(account_slug="string", member_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/{account_slug}/members/{member_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        account_slug: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Member]:
        """
        GET /{account_slug}/members

        Args:
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.members.list(account_slug="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/{account_slug}/members",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Member],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account_slug: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Member:
        """
        GET /{account_slug}/members/{member_id}

        Args:
            account_slug: str
            member_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.members.get(account_slug="string", member_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/{account_slug}/members/{member_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Member,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account_slug: str,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        role: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "Billing Admin", "Developer", "Owner", "Reviewer"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Member]:
        """
        POST /{account_slug}/members

        Args:
            email: str
            role: typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.members.create(account_slug="string")
        ```
        """
        _json = to_encodable(
            item={"email": email, "role": role},
            dump_with=params._SerializerAccountAddMemberSetup,
        )
        return self._base_client.request(
            method="POST",
            path=f"/{account_slug}/members",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=typing.List[models.Member],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        account_slug: str,
        member_id: str,
        role: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "Billing Admin", "Developer", "Owner", "Reviewer"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_access: typing.Union[
            typing.Optional[typing_extensions.Literal["all", "none", "selected"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Member:
        """
        PUT /{account_slug}/members/{member_id}

        Args:
            role: typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
            site_access: typing_extensions.Literal["all", "none", "selected"]
            site_ids: typing.List[str]
            account_slug: str
            member_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.members.update(account_slug="string", member_id="string")
        ```
        """
        _json = to_encodable(
            item={"role": role, "site_access": site_access, "site_ids": site_ids},
            dump_with=params._SerializerAccountUpdateMemberSetup,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/{account_slug}/members/{member_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Member,
            request_options=request_options or default_request_options(),
        )


class AsyncMembersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        account_slug: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /{account_slug}/members/{member_id}

        Args:
            account_slug: str
            member_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Not Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.members.delete(account_slug="string", member_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/{account_slug}/members/{member_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        account_slug: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Member]:
        """
        GET /{account_slug}/members

        Args:
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.members.list(account_slug="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/{account_slug}/members",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.Member],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account_slug: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Member:
        """
        GET /{account_slug}/members/{member_id}

        Args:
            account_slug: str
            member_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.members.get(account_slug="string", member_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/{account_slug}/members/{member_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Member,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account_slug: str,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        role: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "Billing Admin", "Developer", "Owner", "Reviewer"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Member]:
        """
        POST /{account_slug}/members

        Args:
            email: str
            role: typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.members.create(account_slug="string")
        ```
        """
        _json = to_encodable(
            item={"email": email, "role": role},
            dump_with=params._SerializerAccountAddMemberSetup,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/{account_slug}/members",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=typing.List[models.Member],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        account_slug: str,
        member_id: str,
        role: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "Billing Admin", "Developer", "Owner", "Reviewer"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_access: typing.Union[
            typing.Optional[typing_extensions.Literal["all", "none", "selected"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        site_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Member:
        """
        PUT /{account_slug}/members/{member_id}

        Args:
            role: typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
            site_access: typing_extensions.Literal["all", "none", "selected"]
            site_ids: typing.List[str]
            account_slug: str
            member_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.members.update(account_slug="string", member_id="string")
        ```
        """
        _json = to_encodable(
            item={"role": role, "site_access": site_access, "site_ids": site_ids},
            dump_with=params._SerializerAccountUpdateMemberSetup,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/{account_slug}/members/{member_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Member,
            request_options=request_options or default_request_options(),
        )
