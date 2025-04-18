import pydantic
import typing
import typing_extensions


class DnsRecordCreate(typing_extensions.TypedDict):
    """
    DnsRecordCreate
    """

    flag: typing_extensions.NotRequired[int]

    hostname: typing_extensions.NotRequired[str]

    port: typing_extensions.NotRequired[int]

    priority: typing_extensions.NotRequired[int]

    tag: typing_extensions.NotRequired[str]

    ttl: typing_extensions.NotRequired[int]

    type_: typing_extensions.NotRequired[str]

    value: typing_extensions.NotRequired[str]

    weight: typing_extensions.NotRequired[int]


class _SerializerDnsRecordCreate(pydantic.BaseModel):
    """
    Serializer for DnsRecordCreate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    flag: typing.Optional[int] = pydantic.Field(alias="flag", default=None)
    hostname: typing.Optional[str] = pydantic.Field(alias="hostname", default=None)
    port: typing.Optional[int] = pydantic.Field(alias="port", default=None)
    priority: typing.Optional[int] = pydantic.Field(alias="priority", default=None)
    tag: typing.Optional[str] = pydantic.Field(alias="tag", default=None)
    ttl: typing.Optional[int] = pydantic.Field(alias="ttl", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
    weight: typing.Optional[int] = pydantic.Field(alias="weight", default=None)
