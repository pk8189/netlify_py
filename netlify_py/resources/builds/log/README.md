
### create <a name="create"></a>
POST /builds/{build_id}/log



**API Endpoint**: `POST /builds/{build_id}/log`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.builds.log.create(build_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.builds.log.create(build_id="string")
```
