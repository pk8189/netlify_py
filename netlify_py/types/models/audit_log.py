import pydantic
import typing

from .audit_log_payload import AuditLogPayload


class AuditLog(pydantic.BaseModel):
    """
    AuditLog
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="account_id", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    payload: typing.Optional[AuditLogPayload] = pydantic.Field(
        alias="payload", default=None
    )
