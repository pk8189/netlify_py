import pydantic
import typing
import typing_extensions


class SplitTestSetup(typing_extensions.TypedDict):
    """
    SplitTestSetup
    """

    branch_tests: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]


class _SerializerSplitTestSetup(pydantic.BaseModel):
    """
    Serializer for SplitTestSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    branch_tests: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="branch_tests", default=None
    )
