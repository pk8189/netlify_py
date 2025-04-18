
### delete <a name="delete"></a>
DELETE /sites/{site_id}/dev_servers



**API Endpoint**: `DELETE /sites/{site_id}/dev_servers`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_servers.delete(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_servers.delete(site_id="string")
```

### list <a name="list"></a>
GET /sites/{site_id}/dev_servers



**API Endpoint**: `GET /sites/{site_id}/dev_servers`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_servers.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_servers.list(site_id="string")
```

### get <a name="get"></a>
GET /sites/{site_id}/dev_servers/{dev_server_id}



**API Endpoint**: `GET /sites/{site_id}/dev_servers/{dev_server_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_servers.get(dev_server_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_servers.get(dev_server_id="string", site_id="string")
```

### create <a name="create"></a>
POST /sites/{site_id}/dev_servers



**API Endpoint**: `POST /sites/{site_id}/dev_servers`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_servers.create(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_servers.create(site_id="string")
```
