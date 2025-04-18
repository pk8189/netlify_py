import pydantic
import typing

from .dns_record import DnsRecord


class DnsZone(pydantic.BaseModel):
    """
    DnsZone
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="account_id", default=None)
    account_name: typing.Optional[str] = pydantic.Field(
        alias="account_name", default=None
    )
    account_slug: typing.Optional[str] = pydantic.Field(
        alias="account_slug", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    dedicated: typing.Optional[bool] = pydantic.Field(alias="dedicated", default=None)
    dns_servers: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="dns_servers", default=None
    )
    domain: typing.Optional[str] = pydantic.Field(alias="domain", default=None)
    errors: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="errors", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    ipv6_enabled: typing.Optional[bool] = pydantic.Field(
        alias="ipv6_enabled", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    records: typing.Optional[typing.List[DnsRecord]] = pydantic.Field(
        alias="records", default=None
    )
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    supported_record_types: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="supported_record_types", default=None
    )
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    user_id: typing.Optional[str] = pydantic.Field(alias="user_id", default=None)
