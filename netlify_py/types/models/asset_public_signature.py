import pydantic
import typing


class AssetPublicSignature(pydantic.BaseModel):
    """
    AssetPublicSignature
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
