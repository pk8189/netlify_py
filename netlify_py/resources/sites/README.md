
### delete <a name="delete"></a>
DELETE /sites/{site_id}



**API Endpoint**: `DELETE /sites/{site_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.delete(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.delete(site_id="string")
```

### list <a name="list"></a>
GET /sites

**Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

**API Endpoint**: `GET /sites`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.list()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.list()
```

### get <a name="get"></a>
GET /sites/{site_id}

**Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

**API Endpoint**: `GET /sites/{site_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.get(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.get(site_id="string")
```

### list_for_account <a name="list_for_account"></a>
GET /{account_slug}/sites

**Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

**API Endpoint**: `GET /{account_slug}/sites`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.list_for_account(account_slug="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.list_for_account(account_slug="string")
```

### patch <a name="patch"></a>
PATCH /sites/{site_id}

**Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [updateEnvVar](#tag/environmentVariables/operation/updateEnvVar) to update a site's environment variables.

**API Endpoint**: `PATCH /sites/{site_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.patch(site_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.patch(site_id="string")
```

### create <a name="create"></a>
POST /sites

**Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

**API Endpoint**: `POST /sites`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.create()
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.create()
```

### create_1 <a name="create_1"></a>
POST /{account_slug}/sites

**Note:** Environment variable keys and values have moved from `build_settings.env` and `repo.env` to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

**API Endpoint**: `POST /{account_slug}/sites`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.sites.create_1(account_slug_path="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sites.create_1(account_slug_path="string")
```
