import pydantic
import typing
import typing_extensions


class BuildHookSetup(typing_extensions.TypedDict):
    """
    BuildHookSetup
    """

    branch: typing_extensions.NotRequired[str]

    title: typing_extensions.NotRequired[str]


class _SerializerBuildHookSetup(pydantic.BaseModel):
    """
    Serializer for BuildHookSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
