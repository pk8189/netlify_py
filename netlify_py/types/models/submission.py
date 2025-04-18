import pydantic
import typing


class Submission(pydantic.BaseModel):
    """
    Submission
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    body: typing.Optional[str] = pydantic.Field(alias="body", default=None)
    company: typing.Optional[str] = pydantic.Field(alias="company", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="data", default=None
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    number: typing.Optional[int] = pydantic.Field(alias="number", default=None)
    site_url: typing.Optional[str] = pydantic.Field(alias="site_url", default=None)
    summary: typing.Optional[str] = pydantic.Field(alias="summary", default=None)
