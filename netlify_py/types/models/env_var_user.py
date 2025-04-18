import pydantic
import typing


class EnvVarUser(pydantic.BaseModel):
    """
    EnvVarUser
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatar_url", default=None)
    """
    A URL pointing to the user's avatar
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The user's email address
    """
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    """
    The user's full name (first and last)
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    The user's unique identifier
    """
