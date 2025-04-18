import pydantic
import typing


class DevServer(pydantic.BaseModel):
    """
    DevServer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    done_at: typing.Optional[str] = pydantic.Field(alias="done_at", default=None)
    error_at: typing.Optional[str] = pydantic.Field(alias="error_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    live_at: typing.Optional[str] = pydantic.Field(alias="live_at", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    starting_at: typing.Optional[str] = pydantic.Field(
        alias="starting_at", default=None
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
