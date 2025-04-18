import pydantic
import typing


class AccountType(pydantic.BaseModel):
    """
    AccountType
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    capabilities: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="capabilities", default=None
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    monthly_dollar_price: typing.Optional[int] = pydantic.Field(
        alias="monthly_dollar_price", default=None
    )
    monthly_seats_addon_dollar_price: typing.Optional[int] = pydantic.Field(
        alias="monthly_seats_addon_dollar_price", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    yearly_dollar_price: typing.Optional[int] = pydantic.Field(
        alias="yearly_dollar_price", default=None
    )
    yearly_seats_addon_dollar_price: typing.Optional[int] = pydantic.Field(
        alias="yearly_seats_addon_dollar_price", default=None
    )
