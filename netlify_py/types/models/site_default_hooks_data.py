import pydantic
import typing


class SiteDefaultHooksData(pydantic.BaseModel):
    """
    SiteDefaultHooksData
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    access_token: typing.Optional[str] = pydantic.Field(
        alias="access_token", default=None
    )
