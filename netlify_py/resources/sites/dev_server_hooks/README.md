
### delete <a name="delete"></a>
DELETE /sites/{site_id}/dev_server_hooks/{id}



**API Endpoint**: `DELETE /sites/{site_id}/dev_server_hooks/{id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_server_hooks.delete(id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_server_hooks.delete(id="string", site_id="string")
```

### list <a name="list"></a>
GET /sites/{site_id}/dev_server_hooks



**API Endpoint**: `GET /sites/{site_id}/dev_server_hooks`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_server_hooks.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_server_hooks.list(site_id="string")
```

### get <a name="get"></a>
GET /sites/{site_id}/dev_server_hooks/{id}



**API Endpoint**: `GET /sites/{site_id}/dev_server_hooks/{id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_server_hooks.get(id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_server_hooks.get(id="string", site_id="string")
```

### create <a name="create"></a>
POST /sites/{site_id}/dev_server_hooks



**API Endpoint**: `POST /sites/{site_id}/dev_server_hooks`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_server_hooks.create(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_server_hooks.create(site_id="string")
```

### update <a name="update"></a>
PUT /sites/{site_id}/dev_server_hooks/{id}



**API Endpoint**: `PUT /sites/{site_id}/dev_server_hooks/{id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.dev_server_hooks.update(id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.dev_server_hooks.update(id="string", site_id="string")
```
