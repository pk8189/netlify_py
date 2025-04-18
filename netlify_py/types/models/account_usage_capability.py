import pydantic
import typing


class AccountUsageCapability(pydantic.BaseModel):
    """
    AccountUsageCapability
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    included: typing.Optional[int] = pydantic.Field(alias="included", default=None)
    used: typing.Optional[int] = pydantic.Field(alias="used", default=None)
