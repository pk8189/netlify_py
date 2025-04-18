import pydantic
import typing
import typing_extensions

from .deploy_files_functions_config import (
    DeployFilesFunctionsConfig,
    _SerializerDeployFilesFunctionsConfig,
)
from .function_schedule import FunctionSchedule, _SerializerFunctionSchedule


class DeployFiles(typing_extensions.TypedDict):
    """
    DeployFiles
    """

    async_: typing_extensions.NotRequired[bool]

    branch: typing_extensions.NotRequired[str]

    draft: typing_extensions.NotRequired[bool]

    files: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    framework: typing_extensions.NotRequired[str]

    framework_version: typing_extensions.NotRequired[str]

    function_schedules: typing_extensions.NotRequired[typing.List[FunctionSchedule]]

    functions: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    functions_config: typing_extensions.NotRequired[DeployFilesFunctionsConfig]


class _SerializerDeployFiles(pydantic.BaseModel):
    """
    Serializer for DeployFiles handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    async_: typing.Optional[bool] = pydantic.Field(alias="async", default=None)
    branch: typing.Optional[str] = pydantic.Field(alias="branch", default=None)
    draft: typing.Optional[bool] = pydantic.Field(alias="draft", default=None)
    files: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="files", default=None
    )
    framework: typing.Optional[str] = pydantic.Field(alias="framework", default=None)
    framework_version: typing.Optional[str] = pydantic.Field(
        alias="framework_version", default=None
    )
    function_schedules: typing.Optional[typing.List[_SerializerFunctionSchedule]] = (
        pydantic.Field(alias="function_schedules", default=None)
    )
    functions: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="functions", default=None
    )
    functions_config: typing.Optional[_SerializerDeployFilesFunctionsConfig] = (
        pydantic.Field(alias="functions_config", default=None)
    )
