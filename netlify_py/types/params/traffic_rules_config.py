import pydantic
import typing
import typing_extensions

from .traffic_rules_config_action import (
    TrafficRulesConfigAction,
    _SerializerTrafficRulesConfigAction,
)


class TrafficRulesConfig(typing_extensions.TypedDict):
    """
    TrafficRulesConfig
    """

    action: typing_extensions.NotRequired[TrafficRulesConfigAction]


class _SerializerTrafficRulesConfig(pydantic.BaseModel):
    """
    Serializer for TrafficRulesConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    action: typing.Optional[_SerializerTrafficRulesConfigAction] = pydantic.Field(
        alias="action", default=None
    )
