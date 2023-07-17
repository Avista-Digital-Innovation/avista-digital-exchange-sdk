# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CollaborativeMemberOrganizationState,
    CollaborativeMemberPermission,
    UserAccountState,
    UserRole,
)


class PlatformAdminDeleteUsersCollaboratives(BaseModel):
    platform_admin_delete_users_collaboratives: Optional[
        List[
            Optional[
                "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaboratives"
            ]
        ]
    ] = Field(alias="platformAdmin_deleteUsersCollaboratives")


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaboratives(
    BaseModel
):
    collaborative_id: str = Field(alias="collaborativeId")
    description: Optional[str]
    host_organization_id: str = Field(alias="hostOrganizationId")
    member_organizations: Optional[
        List[
            Optional[
                "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizations"
            ]
        ]
    ] = Field(alias="memberOrganizations")
    name: str


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizations(
    BaseModel
):
    access_approved_by_user_id: Optional[str] = Field(alias="accessApprovedByUserId")
    collaborative_id: str = Field(alias="collaborativeId")
    member_state: Optional[CollaborativeMemberOrganizationState] = Field(
        alias="memberState"
    )
    organization: Optional[
        "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsOrganization"
    ]
    submitted_by_user: Optional[
        "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsSubmittedByUser"
    ] = Field(alias="submittedByUser")
    submitted_timestamp: Optional[str] = Field(alias="submittedTimestamp")
    users_in_collaborative: Optional[
        List[
            Optional[
                "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborative"
            ]
        ]
    ] = Field(alias="usersInCollaborative")


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsSubmittedByUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsSubmittedByUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsSubmittedByUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborative(
    BaseModel
):
    permission: Optional[CollaborativeMemberPermission]
    user: Optional[
        "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborativeUser"
    ]


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborativeUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborativeUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborativeUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminDeleteUsersCollaboratives.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaboratives.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizations.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsOrganization.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsSubmittedByUser.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsSubmittedByUserOrganization.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborative.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborativeUser.update_forward_refs()
PlatformAdminDeleteUsersCollaborativesPlatformAdminDeleteUsersCollaborativesMemberOrganizationsUsersInCollaborativeUserOrganization.update_forward_refs()