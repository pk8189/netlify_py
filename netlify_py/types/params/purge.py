import pydantic
import typing
import typing_extensions


class Purge(typing_extensions.TypedDict):
    """
    Purge
    """

    cache_tags: typing_extensions.NotRequired[typing.List[str]]

    site_id: typing_extensions.NotRequired[str]

    site_slug: typing_extensions.NotRequired[str]


class _SerializerPurge(pydantic.BaseModel):
    """
    Serializer for Purge handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cache_tags: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="cache_tags", default=None
    )
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    site_slug: typing.Optional[str] = pydantic.Field(alias="site_slug", default=None)
