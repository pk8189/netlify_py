import pydantic
import typing
import typing_extensions

from .traffic_rules_aggregate_config_keys_item import (
    TrafficRulesAggregateConfigKeysItem,
    _SerializerTrafficRulesAggregateConfigKeysItem,
)


class TrafficRulesAggregateConfig(typing_extensions.TypedDict):
    """
    TrafficRulesAggregateConfig
    """

    keys: typing_extensions.NotRequired[
        typing.List[TrafficRulesAggregateConfigKeysItem]
    ]


class _SerializerTrafficRulesAggregateConfig(pydantic.BaseModel):
    """
    Serializer for TrafficRulesAggregateConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    keys: typing.Optional[
        typing.List[_SerializerTrafficRulesAggregateConfigKeysItem]
    ] = pydantic.Field(alias="keys", default=None)
