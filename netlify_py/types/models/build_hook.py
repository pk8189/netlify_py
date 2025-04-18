import pydantic
import typing


class BuildHook(pydantic.BaseModel):
    """
    BuildHook
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
