import pydantic
import typing


class Asset(pydantic.BaseModel):
    """
    Asset
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    content_type: typing.Optional[str] = pydantic.Field(
        alias="content_type", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    creator_id: typing.Optional[str] = pydantic.Field(alias="creator_id", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    key: typing.Optional[str] = pydantic.Field(alias="key", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    visibility: typing.Optional[str] = pydantic.Field(alias="visibility", default=None)
