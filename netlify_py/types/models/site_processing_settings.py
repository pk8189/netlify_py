import pydantic
import typing

from .site_processing_settings_html import SiteProcessingSettingsHtml


class SiteProcessingSettings(pydantic.BaseModel):
    """
    SiteProcessingSettings
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    html: typing.Optional[SiteProcessingSettingsHtml] = pydantic.Field(
        alias="html", default=None
    )
