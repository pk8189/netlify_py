import pydantic
import typing
import typing_extensions


class AccountsEnvSetBody(typing_extensions.TypedDict):
    """
    AccountsEnvSetBody
    """

    context: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "all", "branch", "branch-deploy", "deploy-preview", "dev", "production"
        ]
    ]
    """
    The deploy context in which this value will be used. `dev` refers to local development when running `netlify dev`. `branch` must be provided with a value in `context_parameter`.
    """

    context_parameter: typing_extensions.NotRequired[str]
    """
    An additional parameter for custom branches. Currently, this is used for providing a branch name when `context=branch`.
    """

    value: typing_extensions.NotRequired[str]
    """
    The environment variable's unencrypted value
    """


class _SerializerAccountsEnvSetBody(pydantic.BaseModel):
    """
    Serializer for AccountsEnvSetBody handling case conversions
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
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
