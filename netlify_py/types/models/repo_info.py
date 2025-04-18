import pydantic
import typing

from .repo_info_env import RepoInfoEnv


class RepoInfo(pydantic.BaseModel):
    """
    RepoInfo
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
    env: typing.Optional[RepoInfoEnv] = pydantic.Field(alias="env", default=None)
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
