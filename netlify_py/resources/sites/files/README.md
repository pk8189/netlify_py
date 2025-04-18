
### list <a name="list"></a>
GET /sites/{site_id}/files



**API Endpoint**: `GET /sites/{site_id}/files`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.files.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.files.list(site_id="string")
```

### get <a name="get"></a>
GET /sites/{site_id}/files/{file_path}



**API Endpoint**: `GET /sites/{site_id}/files/{file_path}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.files.get(file_path="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.files.get(file_path="string", site_id="string")
```
