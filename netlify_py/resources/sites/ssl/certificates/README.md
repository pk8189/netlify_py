
### list <a name="list"></a>
GET /sites/{site_id}/ssl/certificates



**API Endpoint**: `GET /sites/{site_id}/ssl/certificates`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.ssl.certificates.list(domain="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.ssl.certificates.list(domain="string", site_id="string")
```
