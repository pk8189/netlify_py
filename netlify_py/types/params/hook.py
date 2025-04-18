import pydantic
import typing
import typing_extensions


class Hook(typing_extensions.TypedDict):
    """
    Hook
    """

    created_at: typing_extensions.NotRequired[str]

    data: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    disabled: typing_extensions.NotRequired[bool]

    event: typing_extensions.NotRequired[str]

    id: typing_extensions.NotRequired[str]

    site_id: typing_extensions.NotRequired[str]

    type_: typing_extensions.NotRequired[str]

    updated_at: typing_extensions.NotRequired[str]


class _SerializerHook(pydantic.BaseModel):
    """
    Serializer for Hook handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="data", default=None
    )
    disabled: typing.Optional[bool] = pydantic.Field(alias="disabled", default=None)
    event: typing.Optional[str] = pydantic.Field(alias="event", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    site_id: typing.Optional[str] = pydantic.Field(alias="site_id", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
