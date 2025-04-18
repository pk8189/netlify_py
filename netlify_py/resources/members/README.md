
### delete <a name="delete"></a>
DELETE /{account_slug}/members/{member_id}



**API Endpoint**: `DELETE /{account_slug}/members/{member_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.members.delete(account_slug="string", member_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.members.delete(account_slug="string", member_id="string")
```

### list <a name="list"></a>
GET /{account_slug}/members



**API Endpoint**: `GET /{account_slug}/members`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.members.list(account_slug="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.members.list(account_slug="string")
```

### get <a name="get"></a>
GET /{account_slug}/members/{member_id}



**API Endpoint**: `GET /{account_slug}/members/{member_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.members.get(account_slug="string", member_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.members.get(account_slug="string", member_id="string")
```

### create <a name="create"></a>
POST /{account_slug}/members



**API Endpoint**: `POST /{account_slug}/members`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.members.create(account_slug="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.members.create(account_slug="string")
```

### update <a name="update"></a>
PUT /{account_slug}/members/{member_id}



**API Endpoint**: `PUT /{account_slug}/members/{member_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.members.update(account_slug="string", member_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.members.update(account_slug="string", member_id="string")
```
