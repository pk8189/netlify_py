
### list <a name="list"></a>
GET /billing/payment_methods



**API Endpoint**: `GET /billing/payment_methods`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.billing.payment_methods.list()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.billing.payment_methods.list()
```
