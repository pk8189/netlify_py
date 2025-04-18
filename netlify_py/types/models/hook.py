import pydantic
import typing


class Hook(pydantic.BaseModel):
    """
    Hook
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="data", default=None
    )
    disabled: typing.Optional[bool] = pydantic.Field(alias="disabled", default=None)
    event: typing.Optional[str] = pydantic.Field(alias="event", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
