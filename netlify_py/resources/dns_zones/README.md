
### delete <a name="delete"></a>
DELETE /dns_zones/{zone_id}



**API Endpoint**: `DELETE /dns_zones/{zone_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.delete(zone_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.delete(zone_id="string")
```

### list <a name="list"></a>
GET /dns_zones



**API Endpoint**: `GET /dns_zones`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.list()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.list()
```

### get <a name="get"></a>
GET /dns_zones/{zone_id}



**API Endpoint**: `GET /dns_zones/{zone_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.get(zone_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.get(zone_id="string")
```

### create <a name="create"></a>
POST /dns_zones



**API Endpoint**: `POST /dns_zones`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.create()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.create()
```
