import pydantic
import typing

from .asset import Asset
from .asset_form import AssetForm


class AssetSignature(pydantic.BaseModel):
    """
    AssetSignature
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset: typing.Optional[Asset] = pydantic.Field(alias="asset", default=None)
    form: typing.Optional[AssetForm] = pydantic.Field(alias="form", default=None)
