import pydantic
import typing

from .payment_method_data import PaymentMethodData


class PaymentMethod(pydantic.BaseModel):
    """
    PaymentMethod
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    data: typing.Optional[PaymentMethodData] = pydantic.Field(
        alias="data", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    method_name: typing.Optional[str] = pydantic.Field(
        alias="method_name", default=None
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
