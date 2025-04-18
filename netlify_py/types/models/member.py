import pydantic
import typing


class Member(pydantic.BaseModel):
    """
    Member
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avatar: typing.Optional[str] = pydantic.Field(alias="avatar", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    role: typing.Optional[str] = pydantic.Field(alias="role", default=None)
