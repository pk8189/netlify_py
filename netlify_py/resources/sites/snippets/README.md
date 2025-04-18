
### delete <a name="delete"></a>
DELETE /sites/{site_id}/snippets/{snippet_id}



**API Endpoint**: `DELETE /sites/{site_id}/snippets/{snippet_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.snippets.delete(site_id="string", snippet_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.snippets.delete(site_id="string", snippet_id="string")
```

### list <a name="list"></a>
GET /sites/{site_id}/snippets



**API Endpoint**: `GET /sites/{site_id}/snippets`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.snippets.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.snippets.list(site_id="string")
```

### get <a name="get"></a>
GET /sites/{site_id}/snippets/{snippet_id}



**API Endpoint**: `GET /sites/{site_id}/snippets/{snippet_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.snippets.get(site_id="string", snippet_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.snippets.get(site_id="string", snippet_id="string")
```

### create <a name="create"></a>
POST /sites/{site_id}/snippets



**API Endpoint**: `POST /sites/{site_id}/snippets`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.snippets.create(site_id_path="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.snippets.create(site_id_path="string")
```

### update <a name="update"></a>
PUT /sites/{site_id}/snippets/{snippet_id}



**API Endpoint**: `PUT /sites/{site_id}/snippets/{snippet_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.snippets.update(site_id_path="string", snippet_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.snippets.update(site_id_path="string", snippet_id="string")
```
