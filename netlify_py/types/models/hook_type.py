import pydantic
import typing


class HookType(pydantic.BaseModel):
    """
    HookType
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    events: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="events", default=None
    )
    fields: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(
        alias="fields", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
