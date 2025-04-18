import pydantic
import typing
import typing_extensions


class SiteSetupDefaultHooksData(typing_extensions.TypedDict):
    """
    SiteSetupDefaultHooksData
    """

    access_token: typing_extensions.NotRequired[str]


class _SerializerSiteSetupDefaultHooksData(pydantic.BaseModel):
    """
    Serializer for SiteSetupDefaultHooksData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    access_token: typing.Optional[str] = pydantic.Field(
        alias="access_token", default=None
    )
