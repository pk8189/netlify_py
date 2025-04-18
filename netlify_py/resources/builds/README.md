
### get <a name="get"></a>
GET /builds/{build_id}



**API Endpoint**: `GET /builds/{build_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.builds.get(build_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.builds.get(build_id="string")
```
