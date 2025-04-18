import pydantic
import typing
import typing_extensions

from .env_var_value import EnvVarValue, _SerializerEnvVarValue


class AccountsEnvCreateBodyItem(typing_extensions.TypedDict):
    """
    AccountsEnvCreateBodyItem
    """

    is_secret: typing_extensions.NotRequired[bool]
    """
    Secret values are only readable by code running on Netlify's systems. With secrets, only the local development context values are readable from the UI, API, and CLI. By default, environment variable values are not secret.
    """

    key: typing_extensions.NotRequired[str]
    """
    The existing or new name of the key, if you wish to rename it (case-sensitive)
    """

    scopes: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "builds", "functions", "post-processing", "runtime"
            ]
        ]
    ]
    """
    The scopes that this environment variable is set to (Pro plans and above)
    """

    values: typing_extensions.NotRequired[typing.List[EnvVarValue]]


class _SerializerAccountsEnvCreateBodyItem(pydantic.BaseModel):
    """
    Serializer for AccountsEnvCreateBodyItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_secret: typing.Optional[bool] = pydantic.Field(alias="is_secret", default=None)
    key: typing.Optional[str] = pydantic.Field(alias="key", default=None)
    scopes: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "builds", "functions", "post-processing", "runtime"
            ]
        ]
    ] = pydantic.Field(alias="scopes", default=None)
    values: typing.Optional[typing.List[_SerializerEnvVarValue]] = pydantic.Field(
        alias="values", default=None
    )
