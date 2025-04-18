import pydantic
import typing
import typing_extensions


class DnsZoneSetup(typing_extensions.TypedDict):
    """
    DnsZoneSetup
    """

    account_slug: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    site_id: typing_extensions.NotRequired[str]


class _SerializerDnsZoneSetup(pydantic.BaseModel):
    """
    Serializer for DnsZoneSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_slug: typing.Optional[str] = pydantic.Field(
        alias="account_slug", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
