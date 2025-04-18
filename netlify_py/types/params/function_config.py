import pydantic
import typing
import typing_extensions

from .excluded_function_route import (
    ExcludedFunctionRoute,
    _SerializerExcludedFunctionRoute,
)
from .function_route import FunctionRoute, _SerializerFunctionRoute
from .traffic_rules_config import TrafficRulesConfig, _SerializerTrafficRulesConfig


class FunctionConfig(typing_extensions.TypedDict):
    """
    FunctionConfig
    """

    build_data: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    display_name: typing_extensions.NotRequired[str]

    excluded_routes: typing_extensions.NotRequired[typing.List[ExcludedFunctionRoute]]

    generator: typing_extensions.NotRequired[str]

    priority: typing_extensions.NotRequired[int]

    routes: typing_extensions.NotRequired[typing.List[FunctionRoute]]

    traffic_rules: typing_extensions.NotRequired[TrafficRulesConfig]


class _SerializerFunctionConfig(pydantic.BaseModel):
    """
    Serializer for FunctionConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    build_data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="build_data", default=None
    )
    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    excluded_routes: typing.Optional[typing.List[_SerializerExcludedFunctionRoute]] = (
        pydantic.Field(alias="excluded_routes", default=None)
    )
    generator: typing.Optional[str] = pydantic.Field(alias="generator", default=None)
    priority: typing.Optional[int] = pydantic.Field(alias="priority", default=None)
    routes: typing.Optional[typing.List[_SerializerFunctionRoute]] = pydantic.Field(
        alias="routes", default=None
    )
    traffic_rules: typing.Optional[_SerializerTrafficRulesConfig] = pydantic.Field(
        alias="traffic_rules", default=None
    )
