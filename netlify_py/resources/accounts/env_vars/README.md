
### delete <a name="delete"></a>
DELETE /accounts/{account_id}/env/{key}

Deletes an environment variable

**API Endpoint**: `DELETE /accounts/{account_id}/env/{key}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.env_vars.delete(account_id="string", key="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.env_vars.delete(account_id="string", key="string")
```

### delete_value <a name="delete_value"></a>
DELETE /accounts/{account_id}/env/{key}/value/{id}

Deletes a specific environment variable value.

**API Endpoint**: `DELETE /accounts/{account_id}/env/{key}/value/{id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.env_vars.delete_value(
    account_id="string", id="string", key="string"
)
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.env_vars.delete_value(
    account_id="string", id="string", key="string"
)
```

### list <a name="list"></a>
GET /accounts/{account_id}/env

Returns all environment variables for an account or site. An account corresponds to a team in the Netlify UI.

**API Endpoint**: `GET /accounts/{account_id}/env`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.env_vars.list(account_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.env_vars.list(account_id="string")
```

### get <a name="get"></a>
GET /accounts/{account_id}/env/{key}

Returns an individual environment variable.

**API Endpoint**: `GET /accounts/{account_id}/env/{key}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.env_vars.get(account_id="string", key="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.env_vars.get(account_id="string", key="string")
```

### set <a name="set"></a>
PATCH /accounts/{account_id}/env/{key}

Updates or creates a new value for an existing environment variable.

**API Endpoint**: `PATCH /accounts/{account_id}/env/{key}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.env_vars.set(account_id="string", key="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.env_vars.set(account_id="string", key="string")
```

### create <a name="create"></a>
POST /accounts/{account_id}/env

Creates new environment variables. Granular scopes are available on Pro plans and above.

**API Endpoint**: `POST /accounts/{account_id}/env`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.env_vars.create(account_id="string", data=[{}])
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.env_vars.create(account_id="string", data=[{}])
```

### update <a name="update"></a>
PUT /accounts/{account_id}/env/{key}

Updates an existing environment variable and all of its values. Existing values will be replaced by values provided.

**API Endpoint**: `PUT /accounts/{account_id}/env/{key}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.accounts.env_vars.update(account_id="string", key_path="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.accounts.env_vars.update(account_id="string", key_path="string")
```
