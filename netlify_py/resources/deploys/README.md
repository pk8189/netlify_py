
### delete <a name="delete"></a>
DELETE /deploys/{deploy_id}



**API Endpoint**: `DELETE /deploys/{deploy_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploys.delete(deploy_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploys.delete(deploy_id="string")
```

### get <a name="get"></a>
GET /deploys/{deploy_id}



**API Endpoint**: `GET /deploys/{deploy_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploys.get(deploy_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploys.get(deploy_id="string")
```

### cancel <a name="cancel"></a>
POST /deploys/{deploy_id}/cancel



**API Endpoint**: `POST /deploys/{deploy_id}/cancel`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploys.cancel(deploy_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploys.cancel(deploy_id="string")
```

### lock <a name="lock"></a>
POST /deploys/{deploy_id}/lock



**API Endpoint**: `POST /deploys/{deploy_id}/lock`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploys.lock(deploy_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploys.lock(deploy_id="string")
```

### unlock <a name="unlock"></a>
POST /deploys/{deploy_id}/unlock



**API Endpoint**: `POST /deploys/{deploy_id}/unlock`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.deploys.unlock(deploy_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.deploys.unlock(deploy_id="string")
```
