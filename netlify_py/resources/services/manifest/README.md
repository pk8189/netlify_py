
### list <a name="list"></a>
GET /services/{addonName}/manifest



**API Endpoint**: `GET /services/{addonName}/manifest`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.services.manifest.list(addon_name="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.services.manifest.list(addon_name="string")
```
