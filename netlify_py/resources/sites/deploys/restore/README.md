
### create <a name="create"></a>
POST /sites/{site_id}/deploys/{deploy_id}/restore



**API Endpoint**: `POST /sites/{site_id}/deploys/{deploy_id}/restore`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.deploys.restore.create(deploy_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.deploys.restore.create(deploy_id="string", site_id="string")
```
