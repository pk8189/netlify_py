import pydantic
import typing


class Function(pydantic.BaseModel):
    """
    Function
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    sha: typing.Optional[str] = pydantic.Field(alias="sha", default=None)
