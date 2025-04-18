import pydantic
import typing
import typing_extensions


class DevServerHookSetup(typing_extensions.TypedDict):
    """
    DevServerHookSetup
    """

    branch: typing_extensions.NotRequired[str]

    title: typing_extensions.NotRequired[str]

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["content_refresh", "new_dev_server"]
    ]


class _SerializerDevServerHookSetup(pydantic.BaseModel):
    """
    Serializer for DevServerHookSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    type_: typing.Optional[
        typing_extensions.Literal["content_refresh", "new_dev_server"]
    ] = pydantic.Field(alias="type", default=None)
