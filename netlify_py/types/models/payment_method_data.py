import pydantic
import typing


class PaymentMethodData(pydantic.BaseModel):
    """
    PaymentMethodData
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_type: typing.Optional[str] = pydantic.Field(alias="card_type", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
