import pydantic
import typing
import typing_extensions

from .deploy import Deploy, _SerializerDeploy
from .repo_info import RepoInfo, _SerializerRepoInfo
from .site_setup_capabilities import (
    SiteSetupCapabilities,
    _SerializerSiteSetupCapabilities,
)
from .site_setup_default_hooks_data import (
    SiteSetupDefaultHooksData,
    _SerializerSiteSetupDefaultHooksData,
)
from .site_setup_processing_settings import (
    SiteSetupProcessingSettings,
    _SerializerSiteSetupProcessingSettings,
)


class SiteSetup(typing_extensions.TypedDict):
    """
    SiteSetup
    """

    account_id: typing_extensions.NotRequired[str]

    account_name: typing_extensions.NotRequired[str]

    account_slug: typing_extensions.NotRequired[str]

    admin_url: typing_extensions.NotRequired[str]

    branch_deploy_custom_domain: typing_extensions.NotRequired[str]

    build_image: typing_extensions.NotRequired[str]

    build_settings: typing_extensions.NotRequired[RepoInfo]

    capabilities: typing_extensions.NotRequired[SiteSetupCapabilities]

    created_at: typing_extensions.NotRequired[str]

    custom_domain: typing_extensions.NotRequired[str]

    default_hooks_data: typing_extensions.NotRequired[SiteSetupDefaultHooksData]

    deploy_hook: typing_extensions.NotRequired[str]

    deploy_preview_custom_domain: typing_extensions.NotRequired[str]

    deploy_url: typing_extensions.NotRequired[str]

    domain_aliases: typing_extensions.NotRequired[typing.List[str]]

    force_ssl: typing_extensions.NotRequired[bool]

    functions_region: typing_extensions.NotRequired[str]

    git_provider: typing_extensions.NotRequired[str]

    id: typing_extensions.NotRequired[str]

    id_domain: typing_extensions.NotRequired[str]

    managed_dns: typing_extensions.NotRequired[bool]

    name: typing_extensions.NotRequired[str]

    notification_email: typing_extensions.NotRequired[str]

    password: typing_extensions.NotRequired[str]

    plan: typing_extensions.NotRequired[str]

    prerender: typing_extensions.NotRequired[str]

    processing_settings: typing_extensions.NotRequired[SiteSetupProcessingSettings]

    published_deploy: typing_extensions.NotRequired[Deploy]

    screenshot_url: typing_extensions.NotRequired[str]

    session_id: typing_extensions.NotRequired[str]

    ssl: typing_extensions.NotRequired[bool]

    ssl_url: typing_extensions.NotRequired[str]

    state: typing_extensions.NotRequired[str]

    updated_at: typing_extensions.NotRequired[str]

    url: typing_extensions.NotRequired[str]

    user_id: typing_extensions.NotRequired[str]

    repo: typing_extensions.NotRequired[RepoInfo]


class _SerializerSiteSetup(pydantic.BaseModel):
    """
    Serializer for SiteSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="account_id", default=None)
    account_name: typing.Optional[str] = pydantic.Field(
        alias="account_name", default=None
    )
    account_slug: typing.Optional[str] = pydantic.Field(
        alias="account_slug", default=None
    )
    admin_url: typing.Optional[str] = pydantic.Field(alias="admin_url", default=None)
    branch_deploy_custom_domain: typing.Optional[str] = pydantic.Field(
        alias="branch_deploy_custom_domain", default=None
    )
    build_image: typing.Optional[str] = pydantic.Field(
        alias="build_image", default=None
    )
    build_settings: typing.Optional[_SerializerRepoInfo] = pydantic.Field(
        alias="build_settings", default=None
    )
    capabilities: typing.Optional[_SerializerSiteSetupCapabilities] = pydantic.Field(
        alias="capabilities", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    custom_domain: typing.Optional[str] = pydantic.Field(
        alias="custom_domain", default=None
    )
    default_hooks_data: typing.Optional[_SerializerSiteSetupDefaultHooksData] = (
        pydantic.Field(alias="default_hooks_data", default=None)
    )
    deploy_hook: typing.Optional[str] = pydantic.Field(
        alias="deploy_hook", default=None
    )
    deploy_preview_custom_domain: typing.Optional[str] = pydantic.Field(
        alias="deploy_preview_custom_domain", default=None
    )
    deploy_url: typing.Optional[str] = pydantic.Field(alias="deploy_url", default=None)
    domain_aliases: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="domain_aliases", default=None
    )
    force_ssl: typing.Optional[bool] = pydantic.Field(alias="force_ssl", default=None)
    functions_region: typing.Optional[str] = pydantic.Field(
        alias="functions_region", default=None
    )
    git_provider: typing.Optional[str] = pydantic.Field(
        alias="git_provider", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    id_domain: typing.Optional[str] = pydantic.Field(alias="id_domain", default=None)
    managed_dns: typing.Optional[bool] = pydantic.Field(
        alias="managed_dns", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    notification_email: typing.Optional[str] = pydantic.Field(
        alias="notification_email", default=None
    )
    password: typing.Optional[str] = pydantic.Field(alias="password", default=None)
    plan: typing.Optional[str] = pydantic.Field(alias="plan", default=None)
    prerender: typing.Optional[str] = pydantic.Field(alias="prerender", default=None)
    processing_settings: typing.Optional[_SerializerSiteSetupProcessingSettings] = (
        pydantic.Field(alias="processing_settings", default=None)
    )
    published_deploy: typing.Optional[_SerializerDeploy] = pydantic.Field(
        alias="published_deploy", default=None
    )
    screenshot_url: typing.Optional[str] = pydantic.Field(
        alias="screenshot_url", default=None
    )
    session_id: typing.Optional[str] = pydantic.Field(alias="session_id", default=None)
    ssl: typing.Optional[bool] = pydantic.Field(alias="ssl", default=None)
    ssl_url: typing.Optional[str] = pydantic.Field(alias="ssl_url", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    user_id: typing.Optional[str] = pydantic.Field(alias="user_id", default=None)
    repo: typing.Optional[_SerializerRepoInfo] = pydantic.Field(
        alias="repo", default=None
    )
