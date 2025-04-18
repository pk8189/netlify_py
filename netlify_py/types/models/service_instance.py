import pydantic
import typing


class ServiceInstance(pydantic.BaseModel):
    """
    ServiceInstance
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    auth_url: typing.Optional[str] = pydantic.Field(alias="auth_url", default=None)
    config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="config", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    env: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="env", default=None
    )
    external_attributes: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="external_attributes", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    service_name: typing.Optional[str] = pydantic.Field(
        alias="service_name", default=None
    )
    service_path: typing.Optional[str] = pydantic.Field(
        alias="service_path", default=None
    )
    service_slug: typing.Optional[str] = pydantic.Field(
        alias="service_slug", default=None
    )
    snippets: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = (
        pydantic.Field(alias="snippets", default=None)
    )
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
