import pydantic
import typing


class DeployedBranch(pydantic.BaseModel):
    """
    DeployedBranch
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deploy_id: typing.Optional[str] = pydantic.Field(alias="deploy_id", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    ssl_url: typing.Optional[str] = pydantic.Field(alias="ssl_url", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
