import httpx
import typing

from netlify_py.core import AsyncBaseClient, AuthBearer, SyncBaseClient
from netlify_py.environment import Environment
from netlify_py.resources.accounts import AccountsClient, AsyncAccountsClient
from netlify_py.resources.billing import AsyncBillingClient, BillingClient
from netlify_py.resources.builds import AsyncBuildsClient, BuildsClient
from netlify_py.resources.cache import AsyncCacheClient, CacheClient
from netlify_py.resources.deploy_keys import AsyncDeployKeysClient, DeployKeysClient
from netlify_py.resources.deploys import AsyncDeploysClient, DeploysClient
from netlify_py.resources.dns_zones import AsyncDnsZonesClient, DnsZonesClient
from netlify_py.resources.forms import AsyncFormsClient, FormsClient
from netlify_py.resources.hooks import AsyncHooksClient, HooksClient
from netlify_py.resources.members import AsyncMembersClient, MembersClient
from netlify_py.resources.oauth import AsyncOauthClient, OauthClient
from netlify_py.resources.services import AsyncServicesClient, ServicesClient
from netlify_py.resources.sites import AsyncSitesClient, SitesClient
from netlify_py.resources.submissions import AsyncSubmissionsClient, SubmissionsClient
from netlify_py.resources.user import AsyncUserClient, UserClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("netlifyAuth", AuthBearer(val=token))
        self.accounts = AccountsClient(base_client=self._base_client)
        self.deploy_keys = DeployKeysClient(base_client=self._base_client)
        self.deploys = DeploysClient(base_client=self._base_client)
        self.dns_zones = DnsZonesClient(base_client=self._base_client)
        self.hooks = HooksClient(base_client=self._base_client)
        self.sites = SitesClient(base_client=self._base_client)
        self.submissions = SubmissionsClient(base_client=self._base_client)
        self.members = MembersClient(base_client=self._base_client)
        self.billing = BillingClient(base_client=self._base_client)
        self.builds = BuildsClient(base_client=self._base_client)
        self.forms = FormsClient(base_client=self._base_client)
        self.oauth = OauthClient(base_client=self._base_client)
        self.services = ServicesClient(base_client=self._base_client)
        self.user = UserClient(base_client=self._base_client)
        self.cache = CacheClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("netlifyAuth", AuthBearer(val=token))
        self.accounts = AsyncAccountsClient(base_client=self._base_client)
        self.deploy_keys = AsyncDeployKeysClient(base_client=self._base_client)
        self.deploys = AsyncDeploysClient(base_client=self._base_client)
        self.dns_zones = AsyncDnsZonesClient(base_client=self._base_client)
        self.hooks = AsyncHooksClient(base_client=self._base_client)
        self.sites = AsyncSitesClient(base_client=self._base_client)
        self.submissions = AsyncSubmissionsClient(base_client=self._base_client)
        self.members = AsyncMembersClient(base_client=self._base_client)
        self.billing = AsyncBillingClient(base_client=self._base_client)
        self.builds = AsyncBuildsClient(base_client=self._base_client)
        self.forms = AsyncFormsClient(base_client=self._base_client)
        self.oauth = AsyncOauthClient(base_client=self._base_client)
        self.services = AsyncServicesClient(base_client=self._base_client)
        self.user = AsyncUserClient(base_client=self._base_client)
        self.cache = AsyncCacheClient(base_client=self._base_client)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
