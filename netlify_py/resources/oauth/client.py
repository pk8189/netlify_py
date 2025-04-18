from netlify_py.core import AsyncBaseClient, SyncBaseClient
from netlify_py.resources.oauth.tickets import AsyncTicketsClient, TicketsClient


class OauthClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.tickets = TicketsClient(base_client=self._base_client)


class AsyncOauthClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.tickets = AsyncTicketsClient(base_client=self._base_client)
