import pydantic
import typing


class FunctionSchedule(pydantic.BaseModel):
    """
    FunctionSchedule
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cron: typing.Optional[str] = pydantic.Field(alias="cron", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
