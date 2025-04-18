
# Netlify's API documentation Python SDK

## Overview
Netlify is a hosting service for the programmable web. It understands your documents and provides an API to handle atomic deploys of websites, manage form submissions, inject JavaScript snippets, and much more. This is a REST-style API that uses JSON for serialization and OAuth 2 for authentication.

This document is an OpenAPI reference for the Netlify API that you can explore. For more detailed instructions for common uses, please visit the [online documentation](https://www.netlify.com/docs/api/). Visit our Community forum to join the conversation about [understanding and using Netlify's API](https://community.netlify.com/t/common-issue-understanding-and-using-netlifys-api/160).

Additionally, we have two API clients for your convenience:
- [Go Client](https://github.com/netlify/open-api#go-client)
- [JS Client](https://github.com/netlify/build/tree/main/packages/js-client)

### Synchronous Client

```python
from netlify_py import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
```

### Asynchronous Client

```python
from netlify_py import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
```

## Module Documentation and Snippets

### [accounts](netlify_py/resources/accounts/README.md)

* [cancel](netlify_py/resources/accounts/README.md#cancel) - DELETE /accounts/{account_id}
* [create](netlify_py/resources/accounts/README.md#create) - POST /accounts
* [get](netlify_py/resources/accounts/README.md#get) - GET /accounts/{account_id}
* [list](netlify_py/resources/accounts/README.md#list) - GET /accounts
* [update](netlify_py/resources/accounts/README.md#update) - PUT /accounts/{account_id}

### [accounts.audit](netlify_py/resources/accounts/audit/README.md)

* [list](netlify_py/resources/accounts/audit/README.md#list) - GET /accounts/{account_id}/audit

### [accounts.env](netlify_py/resources/accounts/env/README.md)

* [create](netlify_py/resources/accounts/env/README.md#create) - POST /accounts/{account_id}/env
* [delete](netlify_py/resources/accounts/env/README.md#delete) - DELETE /accounts/{account_id}/env/{key}
* [delete_value](netlify_py/resources/accounts/env/README.md#delete_value) - DELETE /accounts/{account_id}/env/{key}/value/{id}
* [get](netlify_py/resources/accounts/env/README.md#get) - GET /accounts/{account_id}/env/{key}
* [list](netlify_py/resources/accounts/env/README.md#list) - GET /accounts/{account_id}/env
* [set](netlify_py/resources/accounts/env/README.md#set) - PATCH /accounts/{account_id}/env/{key}
* [update](netlify_py/resources/accounts/env/README.md#update) - PUT /accounts/{account_id}/env/{key}

### [accounts.types](netlify_py/resources/accounts/types/README.md)

* [list](netlify_py/resources/accounts/types/README.md#list) - GET /accounts/types

### [billing.payment_methods](netlify_py/resources/billing/payment_methods/README.md)

* [list](netlify_py/resources/billing/payment_methods/README.md#list) - GET /billing/payment_methods

### [builds](netlify_py/resources/builds/README.md)

* [get](netlify_py/resources/builds/README.md#get) - GET /builds/{build_id}

### [builds.log](netlify_py/resources/builds/log/README.md)

* [create](netlify_py/resources/builds/log/README.md#create) - POST /builds/{build_id}/log

### [builds.start](netlify_py/resources/builds/start/README.md)

* [create](netlify_py/resources/builds/start/README.md#create) - POST /builds/{build_id}/start

### [builds.status](netlify_py/resources/builds/status/README.md)

* [list](netlify_py/resources/builds/status/README.md#list) - GET /{account_id}/builds/status

### [cache](netlify_py/resources/cache/README.md)

* [purge](netlify_py/resources/cache/README.md#purge) - POST /purge

### [deploy_keys](netlify_py/resources/deploy_keys/README.md)

* [create](netlify_py/resources/deploy_keys/README.md#create) - POST /deploy_keys
* [delete](netlify_py/resources/deploy_keys/README.md#delete) - DELETE /deploy_keys/{key_id}
* [get](netlify_py/resources/deploy_keys/README.md#get) - GET /deploy_keys/{key_id}
* [list](netlify_py/resources/deploy_keys/README.md#list) - GET /deploy_keys

### [deploys](netlify_py/resources/deploys/README.md)

* [cancel](netlify_py/resources/deploys/README.md#cancel) - POST /deploys/{deploy_id}/cancel
* [delete](netlify_py/resources/deploys/README.md#delete) - DELETE /deploys/{deploy_id}
* [get](netlify_py/resources/deploys/README.md#get) - GET /deploys/{deploy_id}
* [lock](netlify_py/resources/deploys/README.md#lock) - POST /deploys/{deploy_id}/lock
* [unlock](netlify_py/resources/deploys/README.md#unlock) - POST /deploys/{deploy_id}/unlock

### [deploys.files](netlify_py/resources/deploys/files/README.md)

* [upload](netlify_py/resources/deploys/files/README.md#upload) - PUT /deploys/{deploy_id}/files/{path}

### [deploys.functions](netlify_py/resources/deploys/functions/README.md)

* [upload](netlify_py/resources/deploys/functions/README.md#upload) - PUT /deploys/{deploy_id}/functions/{name}

### [dns_zones](netlify_py/resources/dns_zones/README.md)

* [create](netlify_py/resources/dns_zones/README.md#create) - POST /dns_zones
* [delete](netlify_py/resources/dns_zones/README.md#delete) - DELETE /dns_zones/{zone_id}
* [get](netlify_py/resources/dns_zones/README.md#get) - GET /dns_zones/{zone_id}
* [list](netlify_py/resources/dns_zones/README.md#list) - GET /dns_zones

### [dns_zones.dns_records](netlify_py/resources/dns_zones/dns_records/README.md)

* [create](netlify_py/resources/dns_zones/dns_records/README.md#create) - POST /dns_zones/{zone_id}/dns_records
* [delete](netlify_py/resources/dns_zones/dns_records/README.md#delete) - DELETE /dns_zones/{zone_id}/dns_records/{dns_record_id}
* [get](netlify_py/resources/dns_zones/dns_records/README.md#get) - GET /dns_zones/{zone_id}/dns_records/{dns_record_id}
* [list](netlify_py/resources/dns_zones/dns_records/README.md#list) - GET /dns_zones/{zone_id}/dns_records

### [dns_zones.transfer](netlify_py/resources/dns_zones/transfer/README.md)

* [update](netlify_py/resources/dns_zones/transfer/README.md#update) - PUT /dns_zones/{zone_id}/transfer

### [forms.submissions](netlify_py/resources/forms/submissions/README.md)

* [list](netlify_py/resources/forms/submissions/README.md#list) - GET /forms/{form_id}/submissions

### [hooks](netlify_py/resources/hooks/README.md)

* [create](netlify_py/resources/hooks/README.md#create) - POST /hooks
* [delete](netlify_py/resources/hooks/README.md#delete) - DELETE /hooks/{hook_id}
* [enable](netlify_py/resources/hooks/README.md#enable) - POST /hooks/{hook_id}/enable
* [get](netlify_py/resources/hooks/README.md#get) - GET /hooks/{hook_id}
* [list](netlify_py/resources/hooks/README.md#list) - GET /hooks
* [update](netlify_py/resources/hooks/README.md#update) - PUT /hooks/{hook_id}

### [hooks.types](netlify_py/resources/hooks/types/README.md)

* [list](netlify_py/resources/hooks/types/README.md#list) - GET /hooks/types

### [members](netlify_py/resources/members/README.md)

* [create](netlify_py/resources/members/README.md#create) - POST /{account_slug}/members
* [delete](netlify_py/resources/members/README.md#delete) - DELETE /{account_slug}/members/{member_id}
* [get](netlify_py/resources/members/README.md#get) - GET /{account_slug}/members/{member_id}
* [list](netlify_py/resources/members/README.md#list) - GET /{account_slug}/members
* [update](netlify_py/resources/members/README.md#update) - PUT /{account_slug}/members/{member_id}

### [oauth.tickets](netlify_py/resources/oauth/tickets/README.md)

* [create](netlify_py/resources/oauth/tickets/README.md#create) - POST /oauth/tickets
* [exchange](netlify_py/resources/oauth/tickets/README.md#exchange) - POST /oauth/tickets/{ticket_id}/exchange
* [get](netlify_py/resources/oauth/tickets/README.md#get) - GET /oauth/tickets/{ticket_id}

### [services](netlify_py/resources/services/README.md)

* [get](netlify_py/resources/services/README.md#get) - GET /services/{addonName}
* [list](netlify_py/resources/services/README.md#list) - GET /services/

### [services.manifest](netlify_py/resources/services/manifest/README.md)

* [list](netlify_py/resources/services/manifest/README.md#list) - GET /services/{addonName}/manifest

### [sites](netlify_py/resources/sites/README.md)

* [create](netlify_py/resources/sites/README.md#create) - POST /sites
* [create_1](netlify_py/resources/sites/README.md#create_1) - POST /{account_slug}/sites
* [delete](netlify_py/resources/sites/README.md#delete) - DELETE /sites/{site_id}
* [get](netlify_py/resources/sites/README.md#get) - GET /sites/{site_id}
* [list](netlify_py/resources/sites/README.md#list) - GET /sites
* [list_for_account](netlify_py/resources/sites/README.md#list_for_account) - GET /{account_slug}/sites
* [patch](netlify_py/resources/sites/README.md#patch) - PATCH /sites/{site_id}

### [sites.assets](netlify_py/resources/sites/assets/README.md)

* [create](netlify_py/resources/sites/assets/README.md#create) - POST /sites/{site_id}/assets
* [delete](netlify_py/resources/sites/assets/README.md#delete) - DELETE /sites/{site_id}/assets/{asset_id}
* [get](netlify_py/resources/sites/assets/README.md#get) - GET /sites/{site_id}/assets/{asset_id}
* [get_public_signature](netlify_py/resources/sites/assets/README.md#get_public_signature) - GET /sites/{site_id}/assets/{asset_id}/public_signature
* [list](netlify_py/resources/sites/assets/README.md#list) - GET /sites/{site_id}/assets
* [update](netlify_py/resources/sites/assets/README.md#update) - PUT /sites/{site_id}/assets/{asset_id}

### [sites.build_hooks](netlify_py/resources/sites/build_hooks/README.md)

* [create](netlify_py/resources/sites/build_hooks/README.md#create) - POST /sites/{site_id}/build_hooks
* [delete](netlify_py/resources/sites/build_hooks/README.md#delete) - DELETE /sites/{site_id}/build_hooks/{id}
* [get](netlify_py/resources/sites/build_hooks/README.md#get) - GET /sites/{site_id}/build_hooks/{id}
* [list](netlify_py/resources/sites/build_hooks/README.md#list) - GET /sites/{site_id}/build_hooks
* [update](netlify_py/resources/sites/build_hooks/README.md#update) - PUT /sites/{site_id}/build_hooks/{id}

### [sites.builds](netlify_py/resources/sites/builds/README.md)

* [create](netlify_py/resources/sites/builds/README.md#create) - POST /sites/{site_id}/builds
* [list](netlify_py/resources/sites/builds/README.md#list) - GET /sites/{site_id}/builds

### [sites.deployed_branches](netlify_py/resources/sites/deployed_branches/README.md)

* [list](netlify_py/resources/sites/deployed_branches/README.md#list) - GET /sites/{site_id}/deployed-branches

### [sites.deploys](netlify_py/resources/sites/deploys/README.md)

* [create](netlify_py/resources/sites/deploys/README.md#create) - POST /sites/{site_id}/deploys
* [delete](netlify_py/resources/sites/deploys/README.md#delete) - DELETE /sites/{site_id}/deploys/{deploy_id}
* [get](netlify_py/resources/sites/deploys/README.md#get) - GET /sites/{site_id}/deploys/{deploy_id}
* [list](netlify_py/resources/sites/deploys/README.md#list) - GET /sites/{site_id}/deploys
* [update](netlify_py/resources/sites/deploys/README.md#update) - PUT /sites/{site_id}/deploys/{deploy_id}

### [sites.deploys.restore](netlify_py/resources/sites/deploys/restore/README.md)

* [create](netlify_py/resources/sites/deploys/restore/README.md#create) - POST /sites/{site_id}/deploys/{deploy_id}/restore

### [sites.dev_server_hooks](netlify_py/resources/sites/dev_server_hooks/README.md)

* [create](netlify_py/resources/sites/dev_server_hooks/README.md#create) - POST /sites/{site_id}/dev_server_hooks
* [delete](netlify_py/resources/sites/dev_server_hooks/README.md#delete) - DELETE /sites/{site_id}/dev_server_hooks/{id}
* [get](netlify_py/resources/sites/dev_server_hooks/README.md#get) - GET /sites/{site_id}/dev_server_hooks/{id}
* [list](netlify_py/resources/sites/dev_server_hooks/README.md#list) - GET /sites/{site_id}/dev_server_hooks
* [update](netlify_py/resources/sites/dev_server_hooks/README.md#update) - PUT /sites/{site_id}/dev_server_hooks/{id}

### [sites.dev_servers](netlify_py/resources/sites/dev_servers/README.md)

* [create](netlify_py/resources/sites/dev_servers/README.md#create) - POST /sites/{site_id}/dev_servers
* [delete](netlify_py/resources/sites/dev_servers/README.md#delete) - DELETE /sites/{site_id}/dev_servers
* [get](netlify_py/resources/sites/dev_servers/README.md#get) - GET /sites/{site_id}/dev_servers/{dev_server_id}
* [list](netlify_py/resources/sites/dev_servers/README.md#list) - GET /sites/{site_id}/dev_servers

### [sites.dns](netlify_py/resources/sites/dns/README.md)

* [list](netlify_py/resources/sites/dns/README.md#list) - GET /sites/{site_id}/dns
* [update](netlify_py/resources/sites/dns/README.md#update) - PUT /sites/{site_id}/dns

### [sites.env](netlify_py/resources/sites/env/README.md)

* [list](netlify_py/resources/sites/env/README.md#list) - GET /api/v1/sites/{site_id}/env

### [sites.files](netlify_py/resources/sites/files/README.md)

* [get](netlify_py/resources/sites/files/README.md#get) - GET /sites/{site_id}/files/{file_path}
* [list](netlify_py/resources/sites/files/README.md#list) - GET /sites/{site_id}/files

### [sites.forms](netlify_py/resources/sites/forms/README.md)

* [delete](netlify_py/resources/sites/forms/README.md#delete) - DELETE /sites/{site_id}/forms/{form_id}
* [list](netlify_py/resources/sites/forms/README.md#list) - GET /sites/{site_id}/forms

### [sites.functions](netlify_py/resources/sites/functions/README.md)

* [list](netlify_py/resources/sites/functions/README.md#list) - GET /sites/{site_id}/functions

### [sites.metadata](netlify_py/resources/sites/metadata/README.md)

* [list](netlify_py/resources/sites/metadata/README.md#list) - GET /sites/{site_id}/metadata
* [update](netlify_py/resources/sites/metadata/README.md#update) - PUT /sites/{site_id}/metadata

### [sites.rollback](netlify_py/resources/sites/rollback/README.md)

* [update](netlify_py/resources/sites/rollback/README.md#update) - PUT /sites/{site_id}/rollback

### [sites.service_instances](netlify_py/resources/sites/service_instances/README.md)

* [list](netlify_py/resources/sites/service_instances/README.md#list) - GET /sites/{site_id}/service-instances

### [sites.services.instances](netlify_py/resources/sites/services/instances/README.md)

* [create](netlify_py/resources/sites/services/instances/README.md#create) - POST /sites/{site_id}/services/{addon}/instances
* [delete](netlify_py/resources/sites/services/instances/README.md#delete) - DELETE /sites/{site_id}/services/{addon}/instances/{instance_id}
* [get](netlify_py/resources/sites/services/instances/README.md#get) - GET /sites/{site_id}/services/{addon}/instances/{instance_id}
* [update](netlify_py/resources/sites/services/instances/README.md#update) - PUT /sites/{site_id}/services/{addon}/instances/{instance_id}

### [sites.snippets](netlify_py/resources/sites/snippets/README.md)

* [create](netlify_py/resources/sites/snippets/README.md#create) - POST /sites/{site_id}/snippets
* [delete](netlify_py/resources/sites/snippets/README.md#delete) - DELETE /sites/{site_id}/snippets/{snippet_id}
* [get](netlify_py/resources/sites/snippets/README.md#get) - GET /sites/{site_id}/snippets/{snippet_id}
* [list](netlify_py/resources/sites/snippets/README.md#list) - GET /sites/{site_id}/snippets
* [update](netlify_py/resources/sites/snippets/README.md#update) - PUT /sites/{site_id}/snippets/{snippet_id}

### [sites.ssl](netlify_py/resources/sites/ssl/README.md)

* [create](netlify_py/resources/sites/ssl/README.md#create) - POST /sites/{site_id}/ssl
* [list](netlify_py/resources/sites/ssl/README.md#list) - GET /sites/{site_id}/ssl

### [sites.ssl.certificates](netlify_py/resources/sites/ssl/certificates/README.md)

* [list](netlify_py/resources/sites/ssl/certificates/README.md#list) - GET /sites/{site_id}/ssl/certificates

### [sites.submissions](netlify_py/resources/sites/submissions/README.md)

* [list](netlify_py/resources/sites/submissions/README.md#list) - GET /sites/{site_id}/submissions

### [sites.traffic_splits](netlify_py/resources/sites/traffic_splits/README.md)

* [create](netlify_py/resources/sites/traffic_splits/README.md#create) - POST /sites/{site_id}/traffic_splits
* [get](netlify_py/resources/sites/traffic_splits/README.md#get) - GET /sites/{site_id}/traffic_splits/{split_test_id}
* [list](netlify_py/resources/sites/traffic_splits/README.md#list) - GET /sites/{site_id}/traffic_splits
* [update](netlify_py/resources/sites/traffic_splits/README.md#update) - PUT /sites/{site_id}/traffic_splits/{split_test_id}

### [sites.traffic_splits.publish](netlify_py/resources/sites/traffic_splits/publish/README.md)

* [create](netlify_py/resources/sites/traffic_splits/publish/README.md#create) - POST /sites/{site_id}/traffic_splits/{split_test_id}/publish

### [sites.traffic_splits.unpublish](netlify_py/resources/sites/traffic_splits/unpublish/README.md)

* [create](netlify_py/resources/sites/traffic_splits/unpublish/README.md#create) - POST /sites/{site_id}/traffic_splits/{split_test_id}/unpublish

### [sites.unlink_repo](netlify_py/resources/sites/unlink_repo/README.md)

* [update](netlify_py/resources/sites/unlink_repo/README.md#update) - PUT /sites/{site_id}/unlink_repo

### [submissions](netlify_py/resources/submissions/README.md)

* [delete](netlify_py/resources/submissions/README.md#delete) - DELETE /submissions/{submission_id}
* [get](netlify_py/resources/submissions/README.md#get) - GET /submissions/{submission_id}

### [user](netlify_py/resources/user/README.md)

* [list](netlify_py/resources/user/README.md#list) - GET /user

<!-- MODULE DOCS END -->
