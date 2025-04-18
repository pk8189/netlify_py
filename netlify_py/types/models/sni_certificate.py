import pydantic
import typing


class SniCertificate(pydantic.BaseModel):
    """
    SniCertificate
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    domains: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="domains", default=None
    )
    expires_at: typing.Optional[str] = pydantic.Field(alias="expires_at", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
