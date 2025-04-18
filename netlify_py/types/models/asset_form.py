import pydantic
import typing

from .asset_form_fields import AssetFormFields


class AssetForm(pydantic.BaseModel):
    """
    AssetForm
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fields: typing.Optional[AssetFormFields] = pydantic.Field(
        alias="fields", default=None
    )
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
