import pydantic
import typing
import typing_extensions


class FunctionSchedule(typing_extensions.TypedDict):
    """
    FunctionSchedule
    """

    cron: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]


class _SerializerFunctionSchedule(pydantic.BaseModel):
    """
    Serializer for FunctionSchedule handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cron: typing.Optional[str] = pydantic.Field(alias="cron", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
