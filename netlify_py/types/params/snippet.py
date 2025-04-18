import pydantic
import typing
import typing_extensions


class Snippet(typing_extensions.TypedDict):
    """
    Snippet
    """

    general: typing_extensions.NotRequired[str]

    general_position: typing_extensions.NotRequired[str]

    goal: typing_extensions.NotRequired[str]

    goal_position: typing_extensions.NotRequired[str]

    id: typing_extensions.NotRequired[int]

    site_id: typing_extensions.NotRequired[str]

    title: typing_extensions.NotRequired[str]


class _SerializerSnippet(pydantic.BaseModel):
    """
    Serializer for Snippet handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    general: typing.Optional[str] = pydantic.Field(alias="general", default=None)
    general_position: typing.Optional[str] = pydantic.Field(
        alias="general_position", default=None
    )
    goal: typing.Optional[str] = pydantic.Field(alias="goal", default=None)
    goal_position: typing.Optional[str] = pydantic.Field(
        alias="goal_position", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
