import pydantic
import typing

from .build_status_minutes import BuildStatusMinutes


class BuildStatus(pydantic.BaseModel):
    """
    BuildStatus
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: typing.Optional[int] = pydantic.Field(alias="active", default=None)
    build_count: typing.Optional[int] = pydantic.Field(
        alias="build_count", default=None
    )
    enqueued: typing.Optional[int] = pydantic.Field(alias="enqueued", default=None)
    minutes: typing.Optional[BuildStatusMinutes] = pydantic.Field(
        alias="minutes", default=None
    )
    pending_concurrency: typing.Optional[int] = pydantic.Field(
        alias="pending_concurrency", default=None
    )
