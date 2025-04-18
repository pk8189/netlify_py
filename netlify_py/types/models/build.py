import pydantic
import typing


class Build(pydantic.BaseModel):
    """
    Build
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    deploy_id: typing.Optional[str] = pydantic.Field(alias="deploy_id", default=None)
    done: typing.Optional[bool] = pydantic.Field(alias="done", default=None)
    error: typing.Optional[str] = pydantic.Field(alias="error", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    sha: typing.Optional[str] = pydantic.Field(alias="sha", default=None)
