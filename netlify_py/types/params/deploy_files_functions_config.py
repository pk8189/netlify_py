import pydantic
import typing
import typing_extensions

from .function_config import FunctionConfig, _SerializerFunctionConfig


class DeployFilesFunctionsConfig(typing_extensions.TypedDict, total=False):
    """
    DeployFilesFunctionsConfig
    """


class _SerializerDeployFilesFunctionsConfig(pydantic.BaseModel):
    """
    Serializer for DeployFilesFunctionsConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, _SerializerFunctionConfig]
