import pydantic
import typing


class SiteFunction(pydantic.BaseModel):
    """
    SiteFunction
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    functions: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = (
        pydantic.Field(alias="functions", default=None)
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    log_type: typing.Optional[str] = pydantic.Field(alias="log_type", default=None)
    provider: typing.Optional[str] = pydantic.Field(alias="provider", default=None)
