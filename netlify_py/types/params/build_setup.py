import pydantic
import typing
import typing_extensions


class BuildSetup(typing_extensions.TypedDict):
    """
    BuildSetup
    """

    clear_cache: typing_extensions.NotRequired[bool]

    image: typing_extensions.NotRequired[str]


class _SerializerBuildSetup(pydantic.BaseModel):
    """
    Serializer for BuildSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    clear_cache: typing.Optional[bool] = pydantic.Field(
        alias="clear_cache", default=None
    )
    image: typing.Optional[str] = pydantic.Field(alias="image", default=None)
