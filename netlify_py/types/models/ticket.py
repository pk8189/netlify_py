import pydantic
import typing


class Ticket(pydantic.BaseModel):
    """
    Ticket
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authorized: typing.Optional[bool] = pydantic.Field(alias="authorized", default=None)
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
