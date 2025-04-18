import pydantic
import typing

from .account_usage_capability import AccountUsageCapability


class AccountMembershipCapabilities(pydantic.BaseModel):
    """
    AccountMembershipCapabilities
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    collaborators: typing.Optional[AccountUsageCapability] = pydantic.Field(
        alias="collaborators", default=None
    )
    sites: typing.Optional[AccountUsageCapability] = pydantic.Field(
        alias="sites", default=None
    )
