
### list <a name="list"></a>
GET /sites/{site_id}/deployed-branches



**API Endpoint**: `GET /sites/{site_id}/deployed-branches`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.deployed_branches.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.deployed_branches.list(site_id="string")
```
