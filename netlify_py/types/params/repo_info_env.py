import pydantic
import typing
import typing_extensions


class RepoInfoEnv(typing_extensions.TypedDict, total=False):
    """
    RepoInfoEnv
    """


class _SerializerRepoInfoEnv(pydantic.BaseModel):
    """
    Serializer for RepoInfoEnv handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
