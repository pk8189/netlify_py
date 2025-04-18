import pydantic
import typing
import typing_extensions


class DevServerHook(pydantic.BaseModel):
    """
    DevServerHook
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    type_: typing.Optional[
        typing_extensions.Literal["content_refresh", "new_dev_server"]
    ] = pydantic.Field(alias="type", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
