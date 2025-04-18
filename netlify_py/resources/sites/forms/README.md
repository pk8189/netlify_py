
### delete <a name="delete"></a>
DELETE /sites/{site_id}/forms/{form_id}



**API Endpoint**: `DELETE /sites/{site_id}/forms/{form_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.forms.delete(form_id="string", site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.forms.delete(form_id="string", site_id="string")
```

### list <a name="list"></a>
GET /sites/{site_id}/forms



**API Endpoint**: `GET /sites/{site_id}/forms`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.forms.list(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.forms.list(site_id="string")
```
