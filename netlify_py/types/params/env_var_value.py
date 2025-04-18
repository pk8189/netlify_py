import pydantic
import typing
import typing_extensions


class EnvVarValue(typing_extensions.TypedDict):
    """
    Environment variable value model definition
    """

    context: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "all", "branch", "branch-deploy", "deploy-preview", "dev", "production"
        ]
    ]
    """
    The deploy context in which this value will be used. `dev` refers to local development when running `netlify dev`.
    """

    context_parameter: typing_extensions.NotRequired[str]
    """
    An additional parameter for custom branches. Currently, this is used for specifying a branch name when `context=branch`.
    """

    id: typing_extensions.NotRequired[str]
    """
    The environment variable value's universally unique ID
    """

    value: typing_extensions.NotRequired[str]
    """
    The environment variable's unencrypted value
    """


class _SerializerEnvVarValue(pydantic.BaseModel):
    """
    Serializer for EnvVarValue handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    context: typing.Optional[
        typing_extensions.Literal[
            "all", "branch", "branch-deploy", "deploy-preview", "dev", "production"
        ]
    ] = pydantic.Field(alias="context", default=None)
    context_parameter: typing.Optional[str] = pydantic.Field(
        alias="context_parameter", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
