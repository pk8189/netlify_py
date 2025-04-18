import pydantic
import typing
import typing_extensions


class AccountSetup(typing_extensions.TypedDict):
    """
    AccountSetup
    """

    extra_seats_block: typing_extensions.NotRequired[int]

    name: typing_extensions.Required[str]

    payment_method_id: typing_extensions.NotRequired[str]

    period: typing_extensions.NotRequired[
        typing_extensions.Literal["monthly", "yearly"]
    ]

    type_id: typing_extensions.Required[str]


class _SerializerAccountSetup(pydantic.BaseModel):
    """
    Serializer for AccountSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    extra_seats_block: typing.Optional[int] = pydantic.Field(
        alias="extra_seats_block", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    payment_method_id: typing.Optional[str] = pydantic.Field(
        alias="payment_method_id", default=None
    )
    period: typing.Optional[typing_extensions.Literal["monthly", "yearly"]] = (
        pydantic.Field(alias="period", default=None)
    )
    type_id: str = pydantic.Field(
        alias="type_id",
    )
