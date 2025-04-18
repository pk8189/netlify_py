import pydantic
import typing


class UserOnboardingProgress(pydantic.BaseModel):
    """
    UserOnboardingProgress
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    slides: typing.Optional[str] = pydantic.Field(alias="slides", default=None)
