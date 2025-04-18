
### list <a name="list"></a>
GET /sites/{site_id}/ssl



**API Endpoint**: `GET /sites/{site_id}/ssl`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.ssl.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.ssl.list(site_id="string")
```

### create <a name="create"></a>
POST /sites/{site_id}/ssl



**API Endpoint**: `POST /sites/{site_id}/ssl`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.ssl.create(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.ssl.create(site_id="string")
```
