
### purge <a name="purge"></a>
POST /purge

Purges cached content from Netlify's CDN. Supports purging by Cache-Tag.

**API Endpoint**: `POST /purge`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.cache.purge()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.cache.purge()
```
