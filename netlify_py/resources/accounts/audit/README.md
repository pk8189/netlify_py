
### list <a name="list"></a>
GET /accounts/{account_id}/audit



**API Endpoint**: `GET /accounts/{account_id}/audit`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.audit.list(account_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.audit.list(account_id="string")
```
