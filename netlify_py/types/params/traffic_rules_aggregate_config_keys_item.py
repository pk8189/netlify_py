import pydantic
import typing
import typing_extensions


class TrafficRulesAggregateConfigKeysItem(typing_extensions.TypedDict):
    """
    TrafficRulesAggregateConfigKeysItem
    """

    type_: typing_extensions.NotRequired[typing_extensions.Literal["domain", "ip"]]


class _SerializerTrafficRulesAggregateConfigKeysItem(pydantic.BaseModel):
    """
    Serializer for TrafficRulesAggregateConfigKeysItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing.Optional[typing_extensions.Literal["domain", "ip"]] = pydantic.Field(
        alias="type", default=None
    )
