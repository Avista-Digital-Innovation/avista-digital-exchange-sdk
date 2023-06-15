# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CollaborativeMemberOrganizationState,
    CollaborativeMemberPermission,
    UserAccountState,
    UserRole,
)


class PlatformAdminGetCollaborative(BaseModel):
    platform_admin_get_collaborative: Optional[
        "PlatformAdminGetCollaborativePlatformAdminGetCollaborative"
    ] = Field(alias="platformAdmin_getCollaborative")


class PlatformAdminGetCollaborativePlatformAdminGetCollaborative(BaseModel):
    collaborative_id: str = Field(alias="collaborativeId")
    description: Optional[str]
    host_organization_id: str = Field(alias="hostOrganizationId")
    member_organizations: Optional[
        List[
            Optional[
                "PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizations"
            ]
        ]
    ] = Field(alias="memberOrganizations")
    name: str


class PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizations(
    BaseModel
):
    access_approved_by_user_id: Optional[str] = Field(alias="accessApprovedByUserId")
    collaborative_id: str = Field(alias="collaborativeId")
    member_state: Optional[CollaborativeMemberOrganizationState] = Field(
        alias="memberState"
    )
    organization: Optional[
        "PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsOrganization"
    ]
    submitted_by_user: Optional[
        "PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsSubmittedByUser"
    ] = Field(alias="submittedByUser")
    submitted_timestamp: Optional[str] = Field(alias="submittedTimestamp")
    users_in_collaborative: Optional[
        List[
            Optional[
                "PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborative"
            ]
        ]
    ] = Field(alias="usersInCollaborative")


class PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsSubmittedByUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsSubmittedByUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsSubmittedByUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborative(
    BaseModel
):
    permission: Optional[CollaborativeMemberPermission]
    user: Optional[
        "PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborativeUser"
    ]


class PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborativeUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborativeUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborativeUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminGetCollaborative.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborative.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizations.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsOrganization.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsSubmittedByUser.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsSubmittedByUserOrganization.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborative.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborativeUser.update_forward_refs()
PlatformAdminGetCollaborativePlatformAdminGetCollaborativeMemberOrganizationsUsersInCollaborativeUserOrganization.update_forward_refs()
