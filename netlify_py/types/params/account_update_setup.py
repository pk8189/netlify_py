import pydantic
import typing
import typing_extensions


class AccountUpdateSetup(typing_extensions.TypedDict):
    """
    AccountUpdateSetup
    """

    billing_details: typing_extensions.NotRequired[str]

    billing_email: typing_extensions.NotRequired[str]

    billing_name: typing_extensions.NotRequired[str]

    extra_seats_block: typing_extensions.NotRequired[int]

    name: typing_extensions.NotRequired[str]

    slug: typing_extensions.NotRequired[str]

    type_id: typing_extensions.NotRequired[str]


class _SerializerAccountUpdateSetup(pydantic.BaseModel):
    """
    Serializer for AccountUpdateSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    billing_details: typing.Optional[str] = pydantic.Field(
        alias="billing_details", default=None
    )
    billing_email: typing.Optional[str] = pydantic.Field(
        alias="billing_email", default=None
    )
    billing_name: typing.Optional[str] = pydantic.Field(
        alias="billing_name", default=None
    )
    extra_seats_block: typing.Optional[int] = pydantic.Field(
        alias="extra_seats_block", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    type_id: typing.Optional[str] = pydantic.Field(alias="type_id", default=None)
