
### create <a name="create"></a>
POST /sites/{site_id}/traffic_splits/{split_test_id}/publish



**API Endpoint**: `POST /sites/{site_id}/traffic_splits/{split_test_id}/publish`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.traffic_splits.publish.create(
    site_id="string", split_test_id="string"
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.traffic_splits.publish.create(
    site_id="string", split_test_id="string"
)
```
