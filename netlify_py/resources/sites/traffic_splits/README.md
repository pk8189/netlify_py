
### list <a name="list"></a>
GET /sites/{site_id}/traffic_splits



**API Endpoint**: `GET /sites/{site_id}/traffic_splits`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.traffic_splits.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.traffic_splits.list(site_id="string")
```

### get <a name="get"></a>
GET /sites/{site_id}/traffic_splits/{split_test_id}



**API Endpoint**: `GET /sites/{site_id}/traffic_splits/{split_test_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.traffic_splits.get(site_id="string", split_test_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.traffic_splits.get(site_id="string", split_test_id="string")
```

### create <a name="create"></a>
POST /sites/{site_id}/traffic_splits



**API Endpoint**: `POST /sites/{site_id}/traffic_splits`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.traffic_splits.create(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.traffic_splits.create(site_id="string")
```

### update <a name="update"></a>
PUT /sites/{site_id}/traffic_splits/{split_test_id}



**API Endpoint**: `PUT /sites/{site_id}/traffic_splits/{split_test_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.traffic_splits.update(site_id="string", split_test_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.traffic_splits.update(site_id="string", split_test_id="string")
```
