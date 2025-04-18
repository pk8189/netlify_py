from netlify_py.core import AsyncBaseClient, SyncBaseClient
from netlify_py.resources.sites.services.instances import (
    AsyncInstancesClient,
    InstancesClient,
)


class ServicesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.instances = InstancesClient(base_client=self._base_client)


class AsyncServicesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.instances = AsyncInstancesClient(base_client=self._base_client)
