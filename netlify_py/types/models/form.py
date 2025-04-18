import pydantic
import typing


class Form(pydantic.BaseModel):
    """
    Form
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    fields: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(
        alias="fields", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    paths: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="paths", default=None
    )
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    submission_count: typing.Optional[int] = pydantic.Field(
        alias="submission_count", default=None
    )
