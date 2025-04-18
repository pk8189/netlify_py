import pydantic
import typing


class Snippet(pydantic.BaseModel):
    """
    Snippet
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
