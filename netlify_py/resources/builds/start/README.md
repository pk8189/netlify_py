
### create <a name="create"></a>
POST /builds/{build_id}/start



**API Endpoint**: `POST /builds/{build_id}/start`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.builds.start.create(build_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.builds.start.create(build_id="string")
```
