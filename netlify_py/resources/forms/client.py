from netlify_py.core import AsyncBaseClient, SyncBaseClient
from netlify_py.resources.forms.submissions import (
    AsyncSubmissionsClient,
    SubmissionsClient,
)


class FormsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.submissions = SubmissionsClient(base_client=self._base_client)


class AsyncFormsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.submissions = AsyncSubmissionsClient(base_client=self._base_client)
