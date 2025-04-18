
### delete <a name="delete"></a>
DELETE /deploy_keys/{key_id}



**API Endpoint**: `DELETE /deploy_keys/{key_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploy_keys.delete(key_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploy_keys.delete(key_id="string")
```

### list <a name="list"></a>
GET /deploy_keys



**API Endpoint**: `GET /deploy_keys`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploy_keys.list()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploy_keys.list()
```

### get <a name="get"></a>
GET /deploy_keys/{key_id}



**API Endpoint**: `GET /deploy_keys/{key_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploy_keys.get(key_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploy_keys.get(key_id="string")
```

### create <a name="create"></a>
POST /deploy_keys



**API Endpoint**: `POST /deploy_keys`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploy_keys.create()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploy_keys.create()
```
