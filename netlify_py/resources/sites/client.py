import typing
import typing_extensions

from netlify_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from netlify_py.resources.sites.assets import AssetsClient, AsyncAssetsClient
from netlify_py.resources.sites.build_hooks import (
    AsyncBuildHooksClient,
    BuildHooksClient,
)
from netlify_py.resources.sites.builds import AsyncBuildsClient, BuildsClient
from netlify_py.resources.sites.deployed_branches import (
    AsyncDeployedBranchesClient,
    DeployedBranchesClient,
)
from netlify_py.resources.sites.deploys import AsyncDeploysClient, DeploysClient
from netlify_py.resources.sites.dev_server_hooks import (
    AsyncDevServerHooksClient,
    DevServerHooksClient,
)
from netlify_py.resources.sites.dev_servers import (
    AsyncDevServersClient,
    DevServersClient,
)
from netlify_py.resources.sites.dns import AsyncDnsClient, DnsClient
from netlify_py.resources.sites.env import AsyncEnvClient, EnvClient
from netlify_py.resources.sites.files import AsyncFilesClient, FilesClient
from netlify_py.resources.sites.forms import AsyncFormsClient, FormsClient
from netlify_py.resources.sites.functions import AsyncFunctionsClient, FunctionsClient
from netlify_py.resources.sites.metadata import AsyncMetadataClient, MetadataClient
from netlify_py.resources.sites.rollback import AsyncRollbackClient, RollbackClient
from netlify_py.resources.sites.service_instances import (
    AsyncServiceInstancesClient,
    ServiceInstancesClient,
)
from netlify_py.resources.sites.services import AsyncServicesClient, ServicesClient
from netlify_py.resources.sites.snippets import AsyncSnippetsClient, SnippetsClient
from netlify_py.resources.sites.ssl import AsyncSslClient, SslClient
from netlify_py.resources.sites.submissions import (
    AsyncSubmissionsClient,
    SubmissionsClient,
)
from netlify_py.resources.sites.traffic_splits import (
    AsyncTrafficSplitsClient,
    TrafficSplitsClient,
)
from netlify_py.resources.sites.unlink_repo import (
    AsyncUnlinkRepoClient,
    UnlinkRepoClient,
)
from netlify_py.types import models, params


class SitesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.assets = AssetsClient(base_client=self._base_client)
        self.build_hooks = BuildHooksClient(base_client=self._base_client)
        self.deploys = DeploysClient(base_client=self._base_client)
        self.dev_server_hooks = DevServerHooksClient(base_client=self._base_client)
        self.dev_servers = DevServersClient(base_client=self._base_client)
        self.forms = FormsClient(base_client=self._base_client)
        self.services = ServicesClient(base_client=self._base_client)
        self.snippets = SnippetsClient(base_client=self._base_client)
        self.env = EnvClient(base_client=self._base_client)
        self.builds = BuildsClient(base_client=self._base_client)
        self.deployed_branches = DeployedBranchesClient(base_client=self._base_client)
        self.dns = DnsClient(base_client=self._base_client)
        self.files = FilesClient(base_client=self._base_client)
        self.functions = FunctionsClient(base_client=self._base_client)
        self.metadata = MetadataClient(base_client=self._base_client)
        self.service_instances = ServiceInstancesClient(base_client=self._base_client)
        self.ssl = SslClient(base_client=self._base_client)
        self.submissions = SubmissionsClient(base_client=self._base_client)
        self.traffic_splits = TrafficSplitsClient(base_client=self._base_client)
        self.rollback = RollbackClient(base_client=self._base_client)
        self.unlink_repo = UnlinkRepoClient(base_client=self._base_client)

    def delete(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /sites/{site_id}

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.delete(site_id="string")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        filter: typing.Union[
            typing.Optional[typing_extensions.Literal["all", "guest", "owner"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Site]:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

        GET /sites

        Args:
            filter: typing_extensions.Literal["all", "guest", "owner"]
            name: str
            page: int
            per_page: int
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter,
                    dump_with=typing_extensions.Literal["all", "guest", "owner"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Site],
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

        GET /sites/{site_id}

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.get(site_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )

    def list_for_account(
        self,
        *,
        account_slug: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Site]:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

        GET /{account_slug}/sites

        Args:
            name: str
            page: int
            per_page: int
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.list_for_account(account_slug="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/{account_slug}/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Site],
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        site_id: str,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        admin_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_deploy_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_settings: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capabilities: typing.Union[
            typing.Optional[params.SiteSetupCapabilities], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_hooks_data: typing.Union[
            typing.Optional[params.SiteSetupDefaultHooksData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_hook: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_preview_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        domain_aliases: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        force_ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_region: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        git_provider: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        managed_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notification_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        plan: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        prerender: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        processing_settings: typing.Union[
            typing.Optional[params.SiteSetupProcessingSettings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        published_deploy: typing.Union[
            typing.Optional[params.Deploy], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        repo: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        screenshot_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        session_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [updateEnvVar](#tag/environmentVariables/operation/updateEnvVar) to update a site's environment variables.

        PATCH /sites/{site_id}

        Args:
            account_id: str
            account_name: str
            account_slug: str
            admin_url: str
            branch_deploy_custom_domain: str
            build_image: str
            build_settings: RepoInfo
            capabilities: SiteSetupCapabilities
            created_at: str
            custom_domain: str
            default_hooks_data: SiteSetupDefaultHooksData
            deploy_hook: str
            deploy_preview_custom_domain: str
            deploy_url: str
            domain_aliases: typing.List[str]
            force_ssl: bool
            functions_region: str
            git_provider: str
            id: str
            id_domain: str
            managed_dns: bool
            name: str
            notification_email: str
            password: str
            plan: str
            prerender: str
            processing_settings: SiteSetupProcessingSettings
            published_deploy: Deploy
            repo: RepoInfo
            screenshot_url: str
            session_id: str
            ssl: bool
            ssl_url: str
            state: str
            updated_at: str
            url: str
            user_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.patch(site_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "account_id": account_id,
                "account_name": account_name,
                "account_slug": account_slug,
                "admin_url": admin_url,
                "branch_deploy_custom_domain": branch_deploy_custom_domain,
                "build_image": build_image,
                "build_settings": build_settings,
                "capabilities": capabilities,
                "created_at": created_at,
                "custom_domain": custom_domain,
                "default_hooks_data": default_hooks_data,
                "deploy_hook": deploy_hook,
                "deploy_preview_custom_domain": deploy_preview_custom_domain,
                "deploy_url": deploy_url,
                "domain_aliases": domain_aliases,
                "force_ssl": force_ssl,
                "functions_region": functions_region,
                "git_provider": git_provider,
                "id": id,
                "id_domain": id_domain,
                "managed_dns": managed_dns,
                "name": name,
                "notification_email": notification_email,
                "password": password,
                "plan": plan,
                "prerender": prerender,
                "processing_settings": processing_settings,
                "published_deploy": published_deploy,
                "repo": repo,
                "screenshot_url": screenshot_url,
                "session_id": session_id,
                "ssl": ssl,
                "ssl_url": ssl_url,
                "state": state,
                "updated_at": updated_at,
                "url": url,
                "user_id": user_id,
            },
            dump_with=params._SerializerSiteSetup,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/sites/{site_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        admin_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_deploy_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_settings: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capabilities: typing.Union[
            typing.Optional[params.SiteSetupCapabilities], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        configure_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_hooks_data: typing.Union[
            typing.Optional[params.SiteSetupDefaultHooksData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_hook: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_preview_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        domain_aliases: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        force_ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_region: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        git_provider: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        managed_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notification_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        plan: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        prerender: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        processing_settings: typing.Union[
            typing.Optional[params.SiteSetupProcessingSettings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        published_deploy: typing.Union[
            typing.Optional[params.Deploy], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        repo: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        screenshot_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        session_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

        POST /sites

        Args:
            account_id: str
            account_name: str
            account_slug: str
            admin_url: str
            branch_deploy_custom_domain: str
            build_image: str
            build_settings: RepoInfo
            capabilities: SiteSetupCapabilities
            configure_dns: bool
            created_at: str
            custom_domain: str
            default_hooks_data: SiteSetupDefaultHooksData
            deploy_hook: str
            deploy_preview_custom_domain: str
            deploy_url: str
            domain_aliases: typing.List[str]
            force_ssl: bool
            functions_region: str
            git_provider: str
            id: str
            id_domain: str
            managed_dns: bool
            name: str
            notification_email: str
            password: str
            plan: str
            prerender: str
            processing_settings: SiteSetupProcessingSettings
            published_deploy: Deploy
            repo: RepoInfo
            screenshot_url: str
            session_id: str
            ssl: bool
            ssl_url: str
            state: str
            updated_at: str
            url: str
            user_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.create()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(configure_dns, type_utils.NotGiven):
            encode_query_param(
                _query,
                "configure_dns",
                to_encodable(item=configure_dns, dump_with=bool),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "account_id": account_id,
                "account_name": account_name,
                "account_slug": account_slug,
                "admin_url": admin_url,
                "branch_deploy_custom_domain": branch_deploy_custom_domain,
                "build_image": build_image,
                "build_settings": build_settings,
                "capabilities": capabilities,
                "created_at": created_at,
                "custom_domain": custom_domain,
                "default_hooks_data": default_hooks_data,
                "deploy_hook": deploy_hook,
                "deploy_preview_custom_domain": deploy_preview_custom_domain,
                "deploy_url": deploy_url,
                "domain_aliases": domain_aliases,
                "force_ssl": force_ssl,
                "functions_region": functions_region,
                "git_provider": git_provider,
                "id": id,
                "id_domain": id_domain,
                "managed_dns": managed_dns,
                "name": name,
                "notification_email": notification_email,
                "password": password,
                "plan": plan,
                "prerender": prerender,
                "processing_settings": processing_settings,
                "published_deploy": published_deploy,
                "repo": repo,
                "screenshot_url": screenshot_url,
                "session_id": session_id,
                "ssl": ssl,
                "ssl_url": ssl_url,
                "state": state,
                "updated_at": updated_at,
                "url": url,
                "user_id": user_id,
            },
            dump_with=params._SerializerSiteSetup,
        )
        return self._base_client.request(
            method="POST",
            path="/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )

    def create_1(
        self,
        *,
        account_slug_path: str,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        admin_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_deploy_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_settings: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capabilities: typing.Union[
            typing.Optional[params.SiteSetupCapabilities], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        configure_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_hooks_data: typing.Union[
            typing.Optional[params.SiteSetupDefaultHooksData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_hook: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_preview_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        domain_aliases: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        force_ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_region: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        git_provider: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        managed_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notification_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        plan: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        prerender: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        processing_settings: typing.Union[
            typing.Optional[params.SiteSetupProcessingSettings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        published_deploy: typing.Union[
            typing.Optional[params.Deploy], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        repo: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        screenshot_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        session_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

        POST /{account_slug}/sites

        Args:
            account_id: str
            account_name: str
            account_slug: str
            admin_url: str
            branch_deploy_custom_domain: str
            build_image: str
            build_settings: RepoInfo
            capabilities: SiteSetupCapabilities
            configure_dns: bool
            created_at: str
            custom_domain: str
            default_hooks_data: SiteSetupDefaultHooksData
            deploy_hook: str
            deploy_preview_custom_domain: str
            deploy_url: str
            domain_aliases: typing.List[str]
            force_ssl: bool
            functions_region: str
            git_provider: str
            id: str
            id_domain: str
            managed_dns: bool
            name: str
            notification_email: str
            password: str
            plan: str
            prerender: str
            processing_settings: SiteSetupProcessingSettings
            published_deploy: Deploy
            repo: RepoInfo
            screenshot_url: str
            session_id: str
            ssl: bool
            ssl_url: str
            state: str
            updated_at: str
            url: str
            user_id: str
            account_slug_path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sites.create_1(account_slug_path="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(configure_dns, type_utils.NotGiven):
            encode_query_param(
                _query,
                "configure_dns",
                to_encodable(item=configure_dns, dump_with=bool),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "account_id": account_id,
                "account_name": account_name,
                "account_slug": account_slug,
                "admin_url": admin_url,
                "branch_deploy_custom_domain": branch_deploy_custom_domain,
                "build_image": build_image,
                "build_settings": build_settings,
                "capabilities": capabilities,
                "created_at": created_at,
                "custom_domain": custom_domain,
                "default_hooks_data": default_hooks_data,
                "deploy_hook": deploy_hook,
                "deploy_preview_custom_domain": deploy_preview_custom_domain,
                "deploy_url": deploy_url,
                "domain_aliases": domain_aliases,
                "force_ssl": force_ssl,
                "functions_region": functions_region,
                "git_provider": git_provider,
                "id": id,
                "id_domain": id_domain,
                "managed_dns": managed_dns,
                "name": name,
                "notification_email": notification_email,
                "password": password,
                "plan": plan,
                "prerender": prerender,
                "processing_settings": processing_settings,
                "published_deploy": published_deploy,
                "repo": repo,
                "screenshot_url": screenshot_url,
                "session_id": session_id,
                "ssl": ssl,
                "ssl_url": ssl_url,
                "state": state,
                "updated_at": updated_at,
                "url": url,
                "user_id": user_id,
            },
            dump_with=params._SerializerSiteSetup,
        )
        return self._base_client.request(
            method="POST",
            path=f"/{account_slug_path}/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )


class AsyncSitesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.assets = AsyncAssetsClient(base_client=self._base_client)
        self.build_hooks = AsyncBuildHooksClient(base_client=self._base_client)
        self.deploys = AsyncDeploysClient(base_client=self._base_client)
        self.dev_server_hooks = AsyncDevServerHooksClient(base_client=self._base_client)
        self.dev_servers = AsyncDevServersClient(base_client=self._base_client)
        self.forms = AsyncFormsClient(base_client=self._base_client)
        self.services = AsyncServicesClient(base_client=self._base_client)
        self.snippets = AsyncSnippetsClient(base_client=self._base_client)
        self.env = AsyncEnvClient(base_client=self._base_client)
        self.builds = AsyncBuildsClient(base_client=self._base_client)
        self.deployed_branches = AsyncDeployedBranchesClient(
            base_client=self._base_client
        )
        self.dns = AsyncDnsClient(base_client=self._base_client)
        self.files = AsyncFilesClient(base_client=self._base_client)
        self.functions = AsyncFunctionsClient(base_client=self._base_client)
        self.metadata = AsyncMetadataClient(base_client=self._base_client)
        self.service_instances = AsyncServiceInstancesClient(
            base_client=self._base_client
        )
        self.ssl = AsyncSslClient(base_client=self._base_client)
        self.submissions = AsyncSubmissionsClient(base_client=self._base_client)
        self.traffic_splits = AsyncTrafficSplitsClient(base_client=self._base_client)
        self.rollback = AsyncRollbackClient(base_client=self._base_client)
        self.unlink_repo = AsyncUnlinkRepoClient(base_client=self._base_client)

    async def delete(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        DELETE /sites/{site_id}

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.delete(site_id="string")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/sites/{site_id}",
            auth_names=["netlifyAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        filter: typing.Union[
            typing.Optional[typing_extensions.Literal["all", "guest", "owner"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Site]:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

        GET /sites

        Args:
            filter: typing_extensions.Literal["all", "guest", "owner"]
            name: str
            page: int
            per_page: int
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter,
                    dump_with=typing_extensions.Literal["all", "guest", "owner"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Site],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, site_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

        GET /sites/{site_id}

        Args:
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.get(site_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/sites/{site_id}",
            auth_names=["netlifyAuth"],
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )

    async def list_for_account(
        self,
        *,
        account_slug: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.Site]:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

        GET /{account_slug}/sites

        Args:
            name: str
            page: int
            per_page: int
            account_slug: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.list_for_account(account_slug="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/{account_slug}/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            cast_to=typing.List[models.Site],
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        site_id: str,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        admin_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_deploy_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_settings: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capabilities: typing.Union[
            typing.Optional[params.SiteSetupCapabilities], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_hooks_data: typing.Union[
            typing.Optional[params.SiteSetupDefaultHooksData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_hook: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_preview_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        domain_aliases: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        force_ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_region: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        git_provider: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        managed_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notification_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        plan: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        prerender: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        processing_settings: typing.Union[
            typing.Optional[params.SiteSetupProcessingSettings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        published_deploy: typing.Union[
            typing.Optional[params.Deploy], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        repo: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        screenshot_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        session_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [updateEnvVar](#tag/environmentVariables/operation/updateEnvVar) to update a site's environment variables.

        PATCH /sites/{site_id}

        Args:
            account_id: str
            account_name: str
            account_slug: str
            admin_url: str
            branch_deploy_custom_domain: str
            build_image: str
            build_settings: RepoInfo
            capabilities: SiteSetupCapabilities
            created_at: str
            custom_domain: str
            default_hooks_data: SiteSetupDefaultHooksData
            deploy_hook: str
            deploy_preview_custom_domain: str
            deploy_url: str
            domain_aliases: typing.List[str]
            force_ssl: bool
            functions_region: str
            git_provider: str
            id: str
            id_domain: str
            managed_dns: bool
            name: str
            notification_email: str
            password: str
            plan: str
            prerender: str
            processing_settings: SiteSetupProcessingSettings
            published_deploy: Deploy
            repo: RepoInfo
            screenshot_url: str
            session_id: str
            ssl: bool
            ssl_url: str
            state: str
            updated_at: str
            url: str
            user_id: str
            site_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.patch(site_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "account_id": account_id,
                "account_name": account_name,
                "account_slug": account_slug,
                "admin_url": admin_url,
                "branch_deploy_custom_domain": branch_deploy_custom_domain,
                "build_image": build_image,
                "build_settings": build_settings,
                "capabilities": capabilities,
                "created_at": created_at,
                "custom_domain": custom_domain,
                "default_hooks_data": default_hooks_data,
                "deploy_hook": deploy_hook,
                "deploy_preview_custom_domain": deploy_preview_custom_domain,
                "deploy_url": deploy_url,
                "domain_aliases": domain_aliases,
                "force_ssl": force_ssl,
                "functions_region": functions_region,
                "git_provider": git_provider,
                "id": id,
                "id_domain": id_domain,
                "managed_dns": managed_dns,
                "name": name,
                "notification_email": notification_email,
                "password": password,
                "plan": plan,
                "prerender": prerender,
                "processing_settings": processing_settings,
                "published_deploy": published_deploy,
                "repo": repo,
                "screenshot_url": screenshot_url,
                "session_id": session_id,
                "ssl": ssl,
                "ssl_url": ssl_url,
                "state": state,
                "updated_at": updated_at,
                "url": url,
                "user_id": user_id,
            },
            dump_with=params._SerializerSiteSetup,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/sites/{site_id}",
            auth_names=["netlifyAuth"],
            json=_json,
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        admin_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_deploy_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_settings: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capabilities: typing.Union[
            typing.Optional[params.SiteSetupCapabilities], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        configure_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_hooks_data: typing.Union[
            typing.Optional[params.SiteSetupDefaultHooksData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_hook: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_preview_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        domain_aliases: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        force_ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_region: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        git_provider: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        managed_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notification_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        plan: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        prerender: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        processing_settings: typing.Union[
            typing.Optional[params.SiteSetupProcessingSettings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        published_deploy: typing.Union[
            typing.Optional[params.Deploy], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        repo: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        screenshot_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        session_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

        POST /sites

        Args:
            account_id: str
            account_name: str
            account_slug: str
            admin_url: str
            branch_deploy_custom_domain: str
            build_image: str
            build_settings: RepoInfo
            capabilities: SiteSetupCapabilities
            configure_dns: bool
            created_at: str
            custom_domain: str
            default_hooks_data: SiteSetupDefaultHooksData
            deploy_hook: str
            deploy_preview_custom_domain: str
            deploy_url: str
            domain_aliases: typing.List[str]
            force_ssl: bool
            functions_region: str
            git_provider: str
            id: str
            id_domain: str
            managed_dns: bool
            name: str
            notification_email: str
            password: str
            plan: str
            prerender: str
            processing_settings: SiteSetupProcessingSettings
            published_deploy: Deploy
            repo: RepoInfo
            screenshot_url: str
            session_id: str
            ssl: bool
            ssl_url: str
            state: str
            updated_at: str
            url: str
            user_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.create()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(configure_dns, type_utils.NotGiven):
            encode_query_param(
                _query,
                "configure_dns",
                to_encodable(item=configure_dns, dump_with=bool),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "account_id": account_id,
                "account_name": account_name,
                "account_slug": account_slug,
                "admin_url": admin_url,
                "branch_deploy_custom_domain": branch_deploy_custom_domain,
                "build_image": build_image,
                "build_settings": build_settings,
                "capabilities": capabilities,
                "created_at": created_at,
                "custom_domain": custom_domain,
                "default_hooks_data": default_hooks_data,
                "deploy_hook": deploy_hook,
                "deploy_preview_custom_domain": deploy_preview_custom_domain,
                "deploy_url": deploy_url,
                "domain_aliases": domain_aliases,
                "force_ssl": force_ssl,
                "functions_region": functions_region,
                "git_provider": git_provider,
                "id": id,
                "id_domain": id_domain,
                "managed_dns": managed_dns,
                "name": name,
                "notification_email": notification_email,
                "password": password,
                "plan": plan,
                "prerender": prerender,
                "processing_settings": processing_settings,
                "published_deploy": published_deploy,
                "repo": repo,
                "screenshot_url": screenshot_url,
                "session_id": session_id,
                "ssl": ssl,
                "ssl_url": ssl_url,
                "state": state,
                "updated_at": updated_at,
                "url": url,
                "user_id": user_id,
            },
            dump_with=params._SerializerSiteSetup,
        )
        return await self._base_client.request(
            method="POST",
            path="/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )

    async def create_1(
        self,
        *,
        account_slug_path: str,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        admin_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        branch_deploy_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_image: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        build_settings: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capabilities: typing.Union[
            typing.Optional[params.SiteSetupCapabilities], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        configure_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_hooks_data: typing.Union[
            typing.Optional[params.SiteSetupDefaultHooksData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_hook: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_preview_custom_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deploy_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        domain_aliases: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        force_ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        functions_region: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        git_provider: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        managed_dns: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notification_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        plan: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        prerender: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        processing_settings: typing.Union[
            typing.Optional[params.SiteSetupProcessingSettings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        published_deploy: typing.Union[
            typing.Optional[params.Deploy], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        repo: typing.Union[
            typing.Optional[params.RepoInfo], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        screenshot_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        session_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ssl_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Site:
        """
        **Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

        POST /{account_slug}/sites

        Args:
            account_id: str
            account_name: str
            account_slug: str
            admin_url: str
            branch_deploy_custom_domain: str
            build_image: str
            build_settings: RepoInfo
            capabilities: SiteSetupCapabilities
            configure_dns: bool
            created_at: str
            custom_domain: str
            default_hooks_data: SiteSetupDefaultHooksData
            deploy_hook: str
            deploy_preview_custom_domain: str
            deploy_url: str
            domain_aliases: typing.List[str]
            force_ssl: bool
            functions_region: str
            git_provider: str
            id: str
            id_domain: str
            managed_dns: bool
            name: str
            notification_email: str
            password: str
            plan: str
            prerender: str
            processing_settings: SiteSetupProcessingSettings
            published_deploy: Deploy
            repo: RepoInfo
            screenshot_url: str
            session_id: str
            ssl: bool
            ssl_url: str
            state: str
            updated_at: str
            url: str
            user_id: str
            account_slug_path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sites.create_1(account_slug_path="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(configure_dns, type_utils.NotGiven):
            encode_query_param(
                _query,
                "configure_dns",
                to_encodable(item=configure_dns, dump_with=bool),
                style="form",
                explode=True,
            )
        _json = to_encodable(
            item={
                "account_id": account_id,
                "account_name": account_name,
                "account_slug": account_slug,
                "admin_url": admin_url,
                "branch_deploy_custom_domain": branch_deploy_custom_domain,
                "build_image": build_image,
                "build_settings": build_settings,
                "capabilities": capabilities,
                "created_at": created_at,
                "custom_domain": custom_domain,
                "default_hooks_data": default_hooks_data,
                "deploy_hook": deploy_hook,
                "deploy_preview_custom_domain": deploy_preview_custom_domain,
                "deploy_url": deploy_url,
                "domain_aliases": domain_aliases,
                "force_ssl": force_ssl,
                "functions_region": functions_region,
                "git_provider": git_provider,
                "id": id,
                "id_domain": id_domain,
                "managed_dns": managed_dns,
                "name": name,
                "notification_email": notification_email,
                "password": password,
                "plan": plan,
                "prerender": prerender,
                "processing_settings": processing_settings,
                "published_deploy": published_deploy,
                "repo": repo,
                "screenshot_url": screenshot_url,
                "session_id": session_id,
                "ssl": ssl,
                "ssl_url": ssl_url,
                "state": state,
                "updated_at": updated_at,
                "url": url,
                "user_id": user_id,
            },
            dump_with=params._SerializerSiteSetup,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/{account_slug_path}/sites",
            auth_names=["netlifyAuth"],
            query_params=_query,
            json=_json,
            cast_to=models.Site,
            request_options=request_options or default_request_options(),
        )
