import pydantic
import typing


class AccessToken(pydantic.BaseModel):
    """
    AccessToken
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    access_token: typing.Optional[str] = pydantic.Field(
        alias="access_token", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    user_email: typing.Optional[str] = pydantic.Field(alias="user_email", default=None)
    user_id: typing.Optional[str] = pydantic.Field(alias="user_id", default=None)
