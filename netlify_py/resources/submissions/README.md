
### delete <a name="delete"></a>
DELETE /submissions/{submission_id}



**API Endpoint**: `DELETE /submissions/{submission_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.submissions.delete(submission_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.submissions.delete(submission_id="string")
```

### get <a name="get"></a>
GET /submissions/{submission_id}



**API Endpoint**: `GET /submissions/{submission_id}`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.submissions.get(submission_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.submissions.get(submission_id="string")
```
