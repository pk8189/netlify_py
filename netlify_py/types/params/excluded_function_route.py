import pydantic
import typing
import typing_extensions


class ExcludedFunctionRoute(typing_extensions.TypedDict):
    """
    ExcludedFunctionRoute
    """

    expression: typing_extensions.NotRequired[str]

    literal: typing_extensions.NotRequired[str]

    pattern: typing_extensions.NotRequired[str]


class _SerializerExcludedFunctionRoute(pydantic.BaseModel):
    """
    Serializer for ExcludedFunctionRoute handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expression: typing.Optional[str] = pydantic.Field(alias="expression", default=None)
    literal: typing.Optional[str] = pydantic.Field(alias="literal", default=None)
    pattern: typing.Optional[str] = pydantic.Field(alias="pattern", default=None)
