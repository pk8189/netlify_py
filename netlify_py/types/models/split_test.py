import pydantic
import typing


class SplitTest(pydantic.BaseModel):
    """
    SplitTest
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    branches: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = (
        pydantic.Field(alias="branches", default=None)
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    path: typing.Optional[str] = pydantic.Field(alias="path", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    unpublished_at: typing.Optional[str] = pydantic.Field(
        alias="unpublished_at", default=None
    )
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
