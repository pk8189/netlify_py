import pydantic
import typing
import typing_extensions


class TrafficRulesRateLimitConfig(typing_extensions.TypedDict):
    """
    TrafficRulesRateLimitConfig
    """

    algorithm: typing_extensions.NotRequired[
        typing_extensions.Literal["sliding_window"]
    ]

    window_limit: typing_extensions.NotRequired[int]

    window_size: typing_extensions.NotRequired[int]


class _SerializerTrafficRulesRateLimitConfig(pydantic.BaseModel):
    """
    Serializer for TrafficRulesRateLimitConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    algorithm: typing.Optional[typing_extensions.Literal["sliding_window"]] = (
        pydantic.Field(alias="algorithm", default=None)
    )
    window_limit: typing.Optional[int] = pydantic.Field(
        alias="window_limit", default=None
    )
    window_size: typing.Optional[int] = pydantic.Field(
        alias="window_size", default=None
    )
