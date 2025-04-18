import pydantic
import typing
import typing_extensions


class AccountUpdateMemberSetup(typing_extensions.TypedDict):
    """
    AccountUpdateMemberSetup
    """

    role: typing_extensions.NotRequired[
        typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
    ]

    site_access: typing_extensions.NotRequired[
        typing_extensions.Literal["all", "none", "selected"]
    ]

    site_ids: typing_extensions.NotRequired[typing.List[str]]


class _SerializerAccountUpdateMemberSetup(pydantic.BaseModel):
    """
    Serializer for AccountUpdateMemberSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    role: typing.Optional[
        typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
    ] = pydantic.Field(alias="role", default=None)
    site_access: typing.Optional[
        typing_extensions.Literal["all", "none", "selected"]
    ] = pydantic.Field(alias="site_access", default=None)
    site_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="site_ids", default=None
    )
