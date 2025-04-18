import pydantic
import typing
import typing_extensions

from .function_schedule import FunctionSchedule, _SerializerFunctionSchedule


class Deploy(typing_extensions.TypedDict):
    """
    Deploy
    """

    admin_url: typing_extensions.NotRequired[str]

    branch: typing_extensions.NotRequired[str]

    build_id: typing_extensions.NotRequired[str]

    commit_ref: typing_extensions.NotRequired[str]

    commit_url: typing_extensions.NotRequired[str]

    context: typing_extensions.NotRequired[str]

    created_at: typing_extensions.NotRequired[str]

    deploy_ssl_url: typing_extensions.NotRequired[str]

    deploy_url: typing_extensions.NotRequired[str]

    draft: typing_extensions.NotRequired[bool]

    error_message: typing_extensions.NotRequired[str]

    framework: typing_extensions.NotRequired[str]

    function_schedules: typing_extensions.NotRequired[typing.List[FunctionSchedule]]

    id: typing_extensions.NotRequired[str]

    locked: typing_extensions.NotRequired[bool]

    name: typing_extensions.NotRequired[str]

    published_at: typing_extensions.NotRequired[str]

    required: typing_extensions.NotRequired[typing.List[str]]

    required_functions: typing_extensions.NotRequired[typing.List[str]]

    review_id: typing_extensions.NotRequired[float]

    review_url: typing_extensions.NotRequired[str]

    screenshot_url: typing_extensions.NotRequired[str]

    site_id: typing_extensions.NotRequired[str]

    skipped: typing_extensions.NotRequired[bool]

    ssl_url: typing_extensions.NotRequired[str]

    state: typing_extensions.NotRequired[str]

    title: typing_extensions.NotRequired[str]

    updated_at: typing_extensions.NotRequired[str]

    url: typing_extensions.NotRequired[str]

    user_id: typing_extensions.NotRequired[str]


class _SerializerDeploy(pydantic.BaseModel):
    """
    Serializer for Deploy handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
    function_schedules: typing.Optional[typing.List[_SerializerFunctionSchedule]] = (
        pydantic.Field(alias="function_schedules", default=None)
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
