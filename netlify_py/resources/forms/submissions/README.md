
### list <a name="list"></a>
GET /forms/{form_id}/submissions



**API Endpoint**: `GET /forms/{form_id}/submissions`

#### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.forms.submissions.list(form_id="string")
```

#### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.forms.submissions.list(form_id="string")
```
