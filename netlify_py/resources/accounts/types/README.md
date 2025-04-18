
### list <a name="list"></a>
GET /accounts/types



**API Endpoint**: `GET /accounts/types`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.types.list()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.types.list()
```
