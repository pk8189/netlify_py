
### get <a name="get"></a>
GET /oauth/tickets/{ticket_id}



**API Endpoint**: `GET /oauth/tickets/{ticket_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.oauth.tickets.get(ticket_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.oauth.tickets.get(ticket_id="string")
```

### create <a name="create"></a>
POST /oauth/tickets



**API Endpoint**: `POST /oauth/tickets`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.oauth.tickets.create(client_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.oauth.tickets.create(client_id="string")
```

### exchange <a name="exchange"></a>
POST /oauth/tickets/{ticket_id}/exchange



**API Endpoint**: `POST /oauth/tickets/{ticket_id}/exchange`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.oauth.tickets.exchange(ticket_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.oauth.tickets.exchange(ticket_id="string")
```
