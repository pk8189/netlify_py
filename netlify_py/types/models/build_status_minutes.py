import pydantic
import typing


class BuildStatusMinutes(pydantic.BaseModel):
    """
    BuildStatusMinutes
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current: typing.Optional[int] = pydantic.Field(alias="current", default=None)
    current_average_sec: typing.Optional[int] = pydantic.Field(
        alias="current_average_sec", default=None
    )
    included_minutes: typing.Optional[str] = pydantic.Field(
        alias="included_minutes", default=None
    )
    included_minutes_with_packs: typing.Optional[str] = pydantic.Field(
        alias="included_minutes_with_packs", default=None
    )
    last_updated_at: typing.Optional[str] = pydantic.Field(
        alias="last_updated_at", default=None
    )
    period_end_date: typing.Optional[str] = pydantic.Field(
        alias="period_end_date", default=None
    )
    period_start_date: typing.Optional[str] = pydantic.Field(
        alias="period_start_date", default=None
    )
    previous: typing.Optional[int] = pydantic.Field(alias="previous", default=None)
