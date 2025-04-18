
### list <a name="list"></a>
GET /sites/{site_id}/dns



**API Endpoint**: `GET /sites/{site_id}/dns`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dns.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dns.list(site_id="string")
```

### update <a name="update"></a>
PUT /sites/{site_id}/dns



**API Endpoint**: `PUT /sites/{site_id}/dns`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dns.update(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dns.update(site_id="string")
```
