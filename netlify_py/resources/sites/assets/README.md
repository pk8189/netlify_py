
### delete <a name="delete"></a>
DELETE /sites/{site_id}/assets/{asset_id}



**API Endpoint**: `DELETE /sites/{site_id}/assets/{asset_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.assets.delete(asset_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.assets.delete(asset_id="string", site_id="string")
```

### list <a name="list"></a>
GET /sites/{site_id}/assets



**API Endpoint**: `GET /sites/{site_id}/assets`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.assets.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.assets.list(site_id="string")
```

### get <a name="get"></a>
GET /sites/{site_id}/assets/{asset_id}



**API Endpoint**: `GET /sites/{site_id}/assets/{asset_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.assets.get(asset_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.assets.get(asset_id="string", site_id="string")
```

### get_public_signature <a name="get_public_signature"></a>
GET /sites/{site_id}/assets/{asset_id}/public_signature



**API Endpoint**: `GET /sites/{site_id}/assets/{asset_id}/public_signature`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.assets.get_public_signature(asset_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.assets.get_public_signature(
    asset_id="string", site_id="string"
)
```

### create <a name="create"></a>
POST /sites/{site_id}/assets



**API Endpoint**: `POST /sites/{site_id}/assets`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.assets.create(
    content_type="string", name="string", site_id="string", size=123
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.assets.create(
    content_type="string", name="string", site_id="string", size=123
)
```

### update <a name="update"></a>
PUT /sites/{site_id}/assets/{asset_id}



**API Endpoint**: `PUT /sites/{site_id}/assets/{asset_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.assets.update(asset_id="string", site_id="string", state="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.assets.update(
    asset_id="string", site_id="string", state="string"
)
```
