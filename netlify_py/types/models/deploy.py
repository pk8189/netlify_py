import pydantic
import typing

from .function_schedule import FunctionSchedule


class Deploy(pydantic.BaseModel):
    """
    Deploy
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    admin_url: typing.Optional[str] = pydantic.Field(alias="admin_url", default=None)
    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    build_id: typing.Optional[str] = pydantic.Field(alias="build_id", default=None)
    commit_ref: typing.Optional[str] = pydantic.Field(alias="commit_ref", default=None)
    commit_url: typing.Optional[str] = pydantic.Field(alias="commit_url", default=None)
    context: typing.Optional[str] = pydantic.Field(alias="context", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    deploy_ssl_url: typing.Optional[str] = pydantic.Field(
        alias="deploy_ssl_url", default=None
    )
    deploy_url: typing.Optional[str] = pydantic.Field(alias="deploy_url", default=None)
    draft: typing.Optional[bool] = pydantic.Field(alias="draft", default=None)
    error_message: typing.Optional[str] = pydantic.Field(
        alias="error_message", default=None
    )
    framework: typing.Optional[str] = pydantic.Field(alias="framework", default=None)
    function_schedules: typing.Optional[typing.List[FunctionSchedule]] = pydantic.Field(
        alias="function_schedules", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    locked: typing.Optional[bool] = pydantic.Field(alias="locked", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    published_at: typing.Optional[str] = pydantic.Field(
        alias="published_at", default=None
    )
    required: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="required", default=None
    )
    required_functions: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="required_functions", default=None
    )
    review_id: typing.Optional[float] = pydantic.Field(alias="review_id", default=None)
    review_url: typing.Optional[str] = pydantic.Field(alias="review_url", default=None)
    screenshot_url: typing.Optional[str] = pydantic.Field(
        alias="screenshot_url", default=None
    )
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    skipped: typing.Optional[bool] = pydantic.Field(alias="skipped", default=None)
    ssl_url: typing.Optional[str] = pydantic.Field(alias="ssl_url", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    user_id: typing.Optional[str] = pydantic.Field(alias="user_id", default=None)
