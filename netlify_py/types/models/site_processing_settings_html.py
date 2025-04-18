import pydantic
import typing


class SiteProcessingSettingsHtml(pydantic.BaseModel):
    """
    SiteProcessingSettingsHtml
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    pretty_urls: typing.Optional[bool] = pydantic.Field(
        alias="pretty_urls", default=None
    )
