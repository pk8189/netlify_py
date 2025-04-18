import pydantic
import typing


class DnsRecord(pydantic.BaseModel):
    """
    DnsRecord
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dns_zone_id: typing.Optional[str] = pydantic.Field(
        alias="dns_zone_id", default=None
    )
    flag: typing.Optional[int] = pydantic.Field(alias="flag", default=None)
    hostname: typing.Optional[str] = pydantic.Field(alias="hostname", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    managed: typing.Optional[bool] = pydantic.Field(alias="managed", default=None)
    priority: typing.Optional[int] = pydantic.Field(alias="priority", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    tag: typing.Optional[str] = pydantic.Field(alias="tag", default=None)
    ttl: typing.Optional[int] = pydantic.Field(alias="ttl", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
