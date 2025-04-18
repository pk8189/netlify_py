import pydantic
import typing
import typing_extensions


class SiteSetupCapabilities(typing_extensions.TypedDict, total=False):
    """
    SiteSetupCapabilities
    """


class _SerializerSiteSetupCapabilities(pydantic.BaseModel):
    """
    Serializer for SiteSetupCapabilities handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Dict[str, typing.Any]]
