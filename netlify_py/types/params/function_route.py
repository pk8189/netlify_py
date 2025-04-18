import pydantic
import typing
import typing_extensions


class FunctionRoute(typing_extensions.TypedDict):
    """
    FunctionRoute
    """

    expression: typing_extensions.NotRequired[str]

    literal: typing_extensions.NotRequired[str]

    methods: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"
            ]
        ]
    ]

    pattern: typing_extensions.NotRequired[str]

    prefer_static: typing_extensions.NotRequired[bool]


class _SerializerFunctionRoute(pydantic.BaseModel):
    """
    Serializer for FunctionRoute handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expression: typing.Optional[str] = pydantic.Field(alias="expression", default=None)
    literal: typing.Optional[str] = pydantic.Field(alias="literal", default=None)
    methods: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"
            ]
        ]
    ] = pydantic.Field(alias="methods", default=None)
    pattern: typing.Optional[str] = pydantic.Field(alias="pattern", default=None)
    prefer_static: typing.Optional[bool] = pydantic.Field(
        alias="prefer_static", default=None
    )
