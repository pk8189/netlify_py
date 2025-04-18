import pydantic
import typing

from .account_membership_capabilities import AccountMembershipCapabilities


class AccountMembership(pydantic.BaseModel):
    """
    AccountMembership
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_details: typing.Optional[str] = pydantic.Field(
        alias="billing_details", default=None
    )
    billing_email: typing.Optional[str] = pydantic.Field(
        alias="billing_email", default=None
    )
    billing_name: typing.Optional[str] = pydantic.Field(
        alias="billing_name", default=None
    )
    billing_period: typing.Optional[str] = pydantic.Field(
        alias="billing_period", default=None
    )
    capabilities: typing.Optional[AccountMembershipCapabilities] = pydantic.Field(
        alias="capabilities", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    owner_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="owner_ids", default=None
    )
    payment_method_id: typing.Optional[str] = pydantic.Field(
        alias="payment_method_id", default=None
    )
    roles_allowed: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="roles_allowed", default=None
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    type_id: typing.Optional[str] = pydantic.Field(alias="type_id", default=None)
    type_name: typing.Optional[str] = pydantic.Field(alias="type_name", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
