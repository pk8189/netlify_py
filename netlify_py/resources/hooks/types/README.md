
### list <a name="list"></a>
GET /hooks/types



**API Endpoint**: `GET /hooks/types`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.hooks.types.list()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.hooks.types.list()
```
