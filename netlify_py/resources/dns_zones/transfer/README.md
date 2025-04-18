
### update <a name="update"></a>
PUT /dns_zones/{zone_id}/transfer



**API Endpoint**: `PUT /dns_zones/{zone_id}/transfer`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.transfer.update(
    account_id="string",
    transfer_account_id="string",
    transfer_user_id="string",
    zone_id="string",
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.transfer.update(
    account_id="string",
    transfer_account_id="string",
    transfer_user_id="string",
    zone_id="string",
)
```
