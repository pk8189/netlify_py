import pydantic
import typing
import typing_extensions

from .repo_info_env import RepoInfoEnv, _SerializerRepoInfoEnv


class RepoInfo(typing_extensions.TypedDict):
    """
    RepoInfo
    """

    allowed_branches: typing_extensions.NotRequired[typing.List[str]]

    cmd: typing_extensions.NotRequired[str]

    deploy_key_id: typing_extensions.NotRequired[str]

    dir: typing_extensions.NotRequired[str]

    env: typing_extensions.NotRequired[RepoInfoEnv]

    functions_dir: typing_extensions.NotRequired[str]

    id: typing_extensions.NotRequired[int]

    installation_id: typing_extensions.NotRequired[int]

    private_logs: typing_extensions.NotRequired[bool]

    provider: typing_extensions.NotRequired[str]

    public_repo: typing_extensions.NotRequired[bool]

    repo_branch: typing_extensions.NotRequired[str]

    repo_path: typing_extensions.NotRequired[str]

    repo_url: typing_extensions.NotRequired[str]

    stop_builds: typing_extensions.NotRequired[bool]


class _SerializerRepoInfo(pydantic.BaseModel):
    """
    Serializer for RepoInfo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allowed_branches: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="allowed_branches", default=None
    )
    cmd: typing.Optional[str] = pydantic.Field(alias="cmd", default=None)
    deploy_key_id: typing.Optional[str] = pydantic.Field(
        alias="deploy_key_id", default=None
    )
    dir: typing.Optional[str] = pydantic.Field(alias="dir", default=None)
    env: typing.Optional[_SerializerRepoInfoEnv] = pydantic.Field(
        alias="env", default=None
    )
    functions_dir: typing.Optional[str] = pydantic.Field(
        alias="functions_dir", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    installation_id: typing.Optional[int] = pydantic.Field(
        alias="installation_id", default=None
    )
    private_logs: typing.Optional[bool] = pydantic.Field(
        alias="private_logs", default=None
    )
    provider: typing.Optional[str] = pydantic.Field(alias="provider", default=None)
    public_repo: typing.Optional[bool] = pydantic.Field(
        alias="public_repo", default=None
    )
    repo_branch: typing.Optional[str] = pydantic.Field(
        alias="repo_branch", default=None
    )
    repo_path: typing.Optional[str] = pydantic.Field(alias="repo_path", default=None)
    repo_url: typing.Optional[str] = pydantic.Field(alias="repo_url", default=None)
    stop_builds: typing.Optional[bool] = pydantic.Field(
        alias="stop_builds", default=None
    )
