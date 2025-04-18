
### list <a name="list"></a>
GET /{account_id}/builds/status



**API Endpoint**: `GET /{account_id}/builds/status`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.builds.status.list(account_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.builds.status.list(account_id="string")
```
