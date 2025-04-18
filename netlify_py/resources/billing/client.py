from netlify_py.core import AsyncBaseClient, SyncBaseClient
from netlify_py.resources.billing.payment_methods import (
    AsyncPaymentMethodsClient,
    PaymentMethodsClient,
)


class BillingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.payment_methods = PaymentMethodsClient(base_client=self._base_client)


class AsyncBillingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.payment_methods = AsyncPaymentMethodsClient(base_client=self._base_client)
