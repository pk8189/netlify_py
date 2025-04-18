import pydantic
import typing

from .deploy import Deploy
from .repo_info import RepoInfo
from .site_capabilities import SiteCapabilities
from .site_default_hooks_data import SiteDefaultHooksData
from .site_processing_settings import SiteProcessingSettings


class Site(pydantic.BaseModel):
    """
    Site
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
    build_settings: typing.Optional[RepoInfo] = pydantic.Field(
        alias="build_settings", default=None
    )
    capabilities: typing.Optional[SiteCapabilities] = pydantic.Field(
        alias="capabilities", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    custom_domain: typing.Optional[str] = pydantic.Field(
        alias="custom_domain", default=None
    )
    default_hooks_data: typing.Optional[SiteDefaultHooksData] = pydantic.Field(
        alias="default_hooks_data", default=None
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
    processing_settings: typing.Optional[SiteProcessingSettings] = pydantic.Field(
        alias="processing_settings", default=None
    )
    published_deploy: typing.Optional[Deploy] = pydantic.Field(
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
