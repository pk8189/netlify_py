import pydantic
import typing


class File(pydantic.BaseModel):
    """
    File
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    mime_type: typing.Optional[str] = pydantic.Field(alias="mime_type", default=None)
    path: typing.Optional[str] = pydantic.Field(alias="path", default=None)
    sha: typing.Optional[str] = pydantic.Field(alias="sha", default=None)
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
