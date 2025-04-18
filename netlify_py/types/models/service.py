import pydantic
import typing


class Service(pydantic.BaseModel):
    """
    Service
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    environments: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="environments", default=None
    )
    events: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(
        alias="events", default=None
    )
    icon: typing.Optional[str] = pydantic.Field(alias="icon", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    long_description: typing.Optional[str] = pydantic.Field(
        alias="long_description", default=None
    )
    manifest_url: typing.Optional[str] = pydantic.Field(
        alias="manifest_url", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    service_path: typing.Optional[str] = pydantic.Field(
        alias="service_path", default=None
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    tags: typing.Optional[typing.List[str]] = pydantic.Field(alias="tags", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
