
### update <a name="update"></a>
PUT /sites/{site_id}/unlink_repo

[Beta] Unlinks the repo from the site.

This action will also:
- Delete associated deploy keys
- Delete outgoing webhooks for the repo
- Delete the site's build hooks

**API Endpoint**: `PUT /sites/{site_id}/unlink_repo`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.unlink_repo.update(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.unlink_repo.update(site_id="string")
```
