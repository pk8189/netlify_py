
### cancel <a name="cancel"></a>
DELETE /accounts/{account_id}



**API Endpoint**: `DELETE /accounts/{account_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.cancel(account_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.cancel(account_id="string")
```

### list <a name="list"></a>
GET /accounts



**API Endpoint**: `GET /accounts`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.list()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.list()
```

### get <a name="get"></a>
GET /accounts/{account_id}



**API Endpoint**: `GET /accounts/{account_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.get(account_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.get(account_id="string")
```

### create <a name="create"></a>
POST /accounts



**API Endpoint**: `POST /accounts`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.create(name="string", type_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.create(name="string", type_id="string")
```

### update <a name="update"></a>
PUT /accounts/{account_id}



**API Endpoint**: `PUT /accounts/{account_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.update(account_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.update(account_id="string")
```
