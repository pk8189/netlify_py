
### delete <a name="delete"></a>
DELETE /sites/{site_id}/services/{addon}/instances/{instance_id}



**API Endpoint**: `DELETE /sites/{site_id}/services/{addon}/instances/{instance_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.services.instances.delete(
    addon="string", instance_id="string", site_id="string"
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.services.instances.delete(
    addon="string", instance_id="string", site_id="string"
)
```

### get <a name="get"></a>
GET /sites/{site_id}/services/{addon}/instances/{instance_id}



**API Endpoint**: `GET /sites/{site_id}/services/{addon}/instances/{instance_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.services.instances.get(
    addon="string", instance_id="string", site_id="string"
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.services.instances.get(
    addon="string", instance_id="string", site_id="string"
)
```

### create <a name="create"></a>
POST /sites/{site_id}/services/{addon}/instances



**API Endpoint**: `POST /sites/{site_id}/services/{addon}/instances`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.services.instances.create(addon="string", data={}, site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.services.instances.create(
    addon="string", data={}, site_id="string"
)
```

### update <a name="update"></a>
PUT /sites/{site_id}/services/{addon}/instances/{instance_id}



**API Endpoint**: `PUT /sites/{site_id}/services/{addon}/instances/{instance_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.services.instances.update(
    addon="string", data={}, instance_id="string", site_id="string"
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.services.instances.update(
    addon="string", data={}, instance_id="string", site_id="string"
)
```
