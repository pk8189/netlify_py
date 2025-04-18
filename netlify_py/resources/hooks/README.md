
### delete <a name="delete"></a>
DELETE /hooks/{hook_id}



**API Endpoint**: `DELETE /hooks/{hook_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.hooks.delete(hook_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.hooks.delete(hook_id="string")
```

### list <a name="list"></a>
GET /hooks



**API Endpoint**: `GET /hooks`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.hooks.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.hooks.list(site_id="string")
```

### get <a name="get"></a>
GET /hooks/{hook_id}



**API Endpoint**: `GET /hooks/{hook_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.hooks.get(hook_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.hooks.get(hook_id="string")
```

### create <a name="create"></a>
POST /hooks



**API Endpoint**: `POST /hooks`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.hooks.create(site_id_query="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.hooks.create(site_id_query="string")
```

### enable <a name="enable"></a>
POST /hooks/{hook_id}/enable



**API Endpoint**: `POST /hooks/{hook_id}/enable`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.hooks.enable(hook_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.hooks.enable(hook_id="string")
```

### update <a name="update"></a>
PUT /hooks/{hook_id}



**API Endpoint**: `PUT /hooks/{hook_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.hooks.update(hook_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.hooks.update(hook_id="string")
```
