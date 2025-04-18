import pydantic
import typing
import typing_extensions

from .site_setup_processing_settings_html import (
    SiteSetupProcessingSettingsHtml,
    _SerializerSiteSetupProcessingSettingsHtml,
)


class SiteSetupProcessingSettings(typing_extensions.TypedDict):
    """
    SiteSetupProcessingSettings
    """

    html: typing_extensions.NotRequired[SiteSetupProcessingSettingsHtml]


class _SerializerSiteSetupProcessingSettings(pydantic.BaseModel):
    """
    Serializer for SiteSetupProcessingSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    html: typing.Optional[_SerializerSiteSetupProcessingSettingsHtml] = pydantic.Field(
        alias="html", default=None
    )
