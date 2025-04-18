import pydantic
import typing
import typing_extensions

from .traffic_rules_config_action_config import (
    TrafficRulesConfigActionConfig,
    _SerializerTrafficRulesConfigActionConfig,
)


class TrafficRulesConfigAction(typing_extensions.TypedDict):
    """
    TrafficRulesConfigAction
    """

    config: typing_extensions.NotRequired[TrafficRulesConfigActionConfig]

    type_: typing_extensions.NotRequired[str]


class _SerializerTrafficRulesConfigAction(pydantic.BaseModel):
    """
    Serializer for TrafficRulesConfigAction handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    config: typing.Optional[_SerializerTrafficRulesConfigActionConfig] = pydantic.Field(
        alias="config", default=None
    )
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
