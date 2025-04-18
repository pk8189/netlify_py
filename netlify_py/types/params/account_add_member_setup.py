import pydantic
import typing
import typing_extensions


class AccountAddMemberSetup(typing_extensions.TypedDict):
    """
    AccountAddMemberSetup
    """

    email: typing_extensions.NotRequired[str]

    role: typing_extensions.NotRequired[
        typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
    ]


class _SerializerAccountAddMemberSetup(pydantic.BaseModel):
    """
    Serializer for AccountAddMemberSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    role: typing.Optional[
        typing_extensions.Literal["Billing Admin", "Developer", "Owner", "Reviewer"]
    ] = pydantic.Field(alias="role", default=None)
