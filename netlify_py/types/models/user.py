import pydantic
import typing

from .user_onboarding_progress import UserOnboardingProgress


class User(pydantic.BaseModel):
    """
    User
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    affiliate_id: typing.Optional[str] = pydantic.Field(
        alias="affiliate_id", default=None
    )
    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatar_url", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    last_login: typing.Optional[str] = pydantic.Field(alias="last_login", default=None)
    login_providers: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="login_providers", default=None
    )
    onboarding_progress: typing.Optional[UserOnboardingProgress] = pydantic.Field(
        alias="onboarding_progress", default=None
    )
    site_count: typing.Optional[int] = pydantic.Field(alias="site_count", default=None)
    uid: typing.Optional[str] = pydantic.Field(alias="uid", default=None)
