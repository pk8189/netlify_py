import pydantic
import typing
import typing_extensions

from .traffic_rules_aggregate_config import (
    TrafficRulesAggregateConfig,
    _SerializerTrafficRulesAggregateConfig,
)
from .traffic_rules_rate_limit_config import (
    TrafficRulesRateLimitConfig,
    _SerializerTrafficRulesRateLimitConfig,
)


class TrafficRulesConfigActionConfig(typing_extensions.TypedDict):
    """
    TrafficRulesConfigActionConfig
    """

    aggregate: typing_extensions.NotRequired[TrafficRulesAggregateConfig]

    rate_limit_config: typing_extensions.NotRequired[TrafficRulesRateLimitConfig]

    to: typing_extensions.NotRequired[str]


class _SerializerTrafficRulesConfigActionConfig(pydantic.BaseModel):
    """
    Serializer for TrafficRulesConfigActionConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aggregate: typing.Optional[_SerializerTrafficRulesAggregateConfig] = pydantic.Field(
        alias="aggregate", default=None
    )
    rate_limit_config: typing.Optional[_SerializerTrafficRulesRateLimitConfig] = (
        pydantic.Field(alias="rate_limit_config", default=None)
    )
    to: typing.Optional[str] = pydantic.Field(alias="to", default=None)
