import pydantic
import typing
import typing_extensions

from .env_var_user import EnvVarUser
from .env_var_value import EnvVarValue


class EnvVar(pydantic.BaseModel):
    """
    Environment variable model definition
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_secret: typing.Optional[bool] = pydantic.Field(alias="is_secret", default=None)
    """
    Secret values are only readable by code running on Netlify's systems. With secrets, only the local development context values are readable from the UI, API, and CLI. By default, environment variable values are not secret.
    """
    key: typing.Optional[str] = pydantic.Field(alias="key", default=None)
    """
    The environment variable key, like ALGOLIA_ID (case-sensitive)
    """
    scopes: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "builds", "functions", "post-processing", "runtime"
            ]
        ]
    ] = pydantic.Field(alias="scopes", default=None)
    """
    The scopes that this environment variable is set to
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    The timestamp of when the value was last updated
    """
    updated_by: typing.Optional[EnvVarUser] = pydantic.Field(
        alias="updated_by", default=None
    )
    values: typing.Optional[typing.List[EnvVarValue]] = pydantic.Field(
        alias="values", default=None
    )
    """
    An array of Value objects containing values and metadata
    """
