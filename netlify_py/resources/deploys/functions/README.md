
### upload <a name="upload"></a>
PUT /deploys/{deploy_id}/functions/{name}



**API Endpoint**: `PUT /deploys/{deploy_id}/functions/{name}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploys.functions.upload(
    data=open("./file.txt", "rb"), deploy_id="string", name="string"
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploys.functions.upload(
    data=open("./file.txt", "rb"), deploy_id="string", name="string"
)
```
