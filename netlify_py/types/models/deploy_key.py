import pydantic
import typing


class DeployKey(pydantic.BaseModel):
    """
    DeployKey
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    public_key: typing.Optional[str] = pydantic.Field(alias="public_key", default=None)
