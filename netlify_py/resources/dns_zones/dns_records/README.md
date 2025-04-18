
### delete <a name="delete"></a>
DELETE /dns_zones/{zone_id}/dns_records/{dns_record_id}



**API Endpoint**: `DELETE /dns_zones/{zone_id}/dns_records/{dns_record_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.dns_records.delete(dns_record_id="string", zone_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.dns_records.delete(
    dns_record_id="string", zone_id="string"
)
```

### list <a name="list"></a>
GET /dns_zones/{zone_id}/dns_records



**API Endpoint**: `GET /dns_zones/{zone_id}/dns_records`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.dns_records.list(zone_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.dns_records.list(zone_id="string")
```

### get <a name="get"></a>
GET /dns_zones/{zone_id}/dns_records/{dns_record_id}



**API Endpoint**: `GET /dns_zones/{zone_id}/dns_records/{dns_record_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.dns_records.get(dns_record_id="string", zone_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.dns_records.get(dns_record_id="string", zone_id="string")
```

### create <a name="create"></a>
POST /dns_zones/{zone_id}/dns_records



**API Endpoint**: `POST /dns_zones/{zone_id}/dns_records`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.dns_zones.dns_records.create(zone_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dns_zones.dns_records.create(zone_id="string")
```
