import pydantic
import typing
import typing_extensions


class SiteSetupProcessingSettingsHtml(typing_extensions.TypedDict):
    """
    SiteSetupProcessingSettingsHtml
    """

    pretty_urls: typing_extensions.NotRequired[bool]


class _SerializerSiteSetupProcessingSettingsHtml(pydantic.BaseModel):
    """
    Serializer for SiteSetupProcessingSettingsHtml handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    pretty_urls: typing.Optional[bool] = pydantic.Field(
        alias="pretty_urls", default=None
    )
