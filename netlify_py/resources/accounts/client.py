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
from netlify_py.resources.accounts.account_types import (
    AccountTypesClient,
    AsyncAccountTypesClient,
)
from netlify_py.resources.accounts.audit import AsyncAuditClient, AuditClient
from netlify_py.resources.accounts.env_vars import AsyncEnvVarsClient, EnvVarsClient
from netlify_py.types import models, params


class AccountsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.env_vars = EnvVarsClient(base_client=self._base_client)
        self.account_types = AccountTypesClient(base_client=self._base_client)
        self.audit = AuditClient(base_client=self._base_client)

    def cancel(
        self,
        *,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /accounts/{account_id}

        Args:
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Not Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.cancel(account_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/accounts/{account_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.AccountMembership]:
        """
        GET /accounts

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/accounts",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.AccountMembership],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.AccountMembership]:
        """
        GET /accounts/{account_id}

        Args:
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.get(account_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.AccountMembership],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        type_id: str,
        extra_seats_block: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        period: typing.Union[
            typing.Optional[typing_extensions.Literal["monthly", "yearly"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountMembership:
        """
        POST /accounts

        Args:
            extra_seats_block: int
            payment_method_id: str
            period: typing_extensions.Literal["monthly", "yearly"]
            name: str
            type_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.create(name="string", type_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "extra_seats_block": extra_seats_block,
                "payment_method_id": payment_method_id,
                "period": period,
                "name": name,
                "type_id": type_id,
            },
            dump_with=params._SerializerAccountSetup,
        )
        return self._base_client.request(
            method="POST",
            path="/accounts",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.AccountMembership,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        account_id: str,
        billing_details: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        extra_seats_block: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountMembership:
        """
        PUT /accounts/{account_id}

        Args:
            billing_details: str
            billing_email: str
            billing_name: str
            extra_seats_block: int
            name: str
            slug: str
            type_id: str
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.update(account_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "billing_details": billing_details,
                "billing_email": billing_email,
                "billing_name": billing_name,
                "extra_seats_block": extra_seats_block,
                "name": name,
                "slug": slug,
                "type_id": type_id,
            },
            dump_with=params._SerializerAccountUpdateSetup,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/accounts/{account_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.AccountMembership,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.env_vars = AsyncEnvVarsClient(base_client=self._base_client)
        self.account_types = AsyncAccountTypesClient(base_client=self._base_client)
        self.audit = AsyncAuditClient(base_client=self._base_client)

    async def cancel(
        self,
        *,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        DELETE /accounts/{account_id}

        Args:
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Not Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.cancel(account_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/accounts/{account_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[models.AccountMembership]:
        """
        GET /accounts

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/accounts",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.AccountMembership],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.AccountMembership]:
        """
        GET /accounts/{account_id}

        Args:
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.get(account_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/accounts/{account_id}",
            auth_names=["netlifyAuth"],
            cast_to=typing.List[models.AccountMembership],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        type_id: str,
        extra_seats_block: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        period: typing.Union[
            typing.Optional[typing_extensions.Literal["monthly", "yearly"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountMembership:
        """
        POST /accounts

        Args:
            extra_seats_block: int
            payment_method_id: str
            period: typing_extensions.Literal["monthly", "yearly"]
            name: str
            type_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.create(name="string", type_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "extra_seats_block": extra_seats_block,
                "payment_method_id": payment_method_id,
                "period": period,
                "name": name,
                "type_id": type_id,
            },
            dump_with=params._SerializerAccountSetup,
        )
        return await self._base_client.request(
            method="POST",
            path="/accounts",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.AccountMembership,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        account_id: str,
        billing_details: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        extra_seats_block: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountMembership:
        """
        PUT /accounts/{account_id}

        Args:
            billing_details: str
            billing_email: str
            billing_name: str
            extra_seats_block: int
            name: str
            slug: str
            type_id: str
            account_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.update(account_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "billing_details": billing_details,
                "billing_email": billing_email,
                "billing_name": billing_name,
                "extra_seats_block": extra_seats_block,
                "name": name,
                "slug": slug,
                "type_id": type_id,
            },
            dump_with=params._SerializerAccountUpdateSetup,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/accounts/{account_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.AccountMembership,
            request_options=request_options or default_request_options(),
        )
