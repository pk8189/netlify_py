
### update <a name="update"></a>
PUT /sites/{site_id}/rollback



**API Endpoint**: `PUT /sites/{site_id}/rollback`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.rollback.update(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.rollback.update(site_id="string")
```
