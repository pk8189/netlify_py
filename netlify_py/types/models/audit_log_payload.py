import pydantic
import typing


class AuditLogPayload(pydantic.BaseModel):
    """
    AuditLogPayload
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Dict[str, typing.Any]]

    action: typing.Optional[str] = pydantic.Field(alias="action", default=None)
    actor_email: typing.Optional[str] = pydantic.Field(
        alias="actor_email", default=None
    )
    actor_id: typing.Optional[str] = pydantic.Field(alias="actor_id", default=None)
    actor_name: typing.Optional[str] = pydantic.Field(alias="actor_name", default=None)
    log_type: typing.Optional[str] = pydantic.Field(alias="log_type", default=None)
    timestamp: typing.Optional[str] = pydantic.Field(alias="timestamp", default=None)
