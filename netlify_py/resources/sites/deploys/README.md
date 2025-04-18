
### delete <a name="delete"></a>
DELETE /sites/{site_id}/deploys/{deploy_id}



**API Endpoint**: `DELETE /sites/{site_id}/deploys/{deploy_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.deploys.delete(deploy_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.deploys.delete(deploy_id="string", site_id="string")
```

### list <a name="list"></a>
GET /sites/{site_id}/deploys



**API Endpoint**: `GET /sites/{site_id}/deploys`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.deploys.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.deploys.list(site_id="string")
```

### get <a name="get"></a>
GET /sites/{site_id}/deploys/{deploy_id}



**API Endpoint**: `GET /sites/{site_id}/deploys/{deploy_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.deploys.get(deploy_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.deploys.get(deploy_id="string", site_id="string")
```

### create <a name="create"></a>
POST /sites/{site_id}/deploys



**API Endpoint**: `POST /sites/{site_id}/deploys`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.deploys.create(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.deploys.create(site_id="string")
```

### update <a name="update"></a>
PUT /sites/{site_id}/deploys/{deploy_id}



**API Endpoint**: `PUT /sites/{site_id}/deploys/{deploy_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.deploys.update(deploy_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.deploys.update(deploy_id="string", site_id="string")
```
