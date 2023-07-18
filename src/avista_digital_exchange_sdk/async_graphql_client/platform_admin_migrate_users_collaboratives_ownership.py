# Generated by ariadne-codegen on 2023-07-17 15:57
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


class PlatformAdminMigrateUsersCollaborativesOwnership(BaseModel):
    platform_admin_migrate_users_collaboratives_ownership: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnership"
            ]
        ]
    ] = Field(alias="platformAdmin_migrateUsersCollaborativesOwnership")


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnership(
    BaseModel
):
    collaborative_id: str = Field(alias="collaborativeId")
    description: Optional[str]
    host_organization_id: str = Field(alias="hostOrganizationId")
    member_organizations: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizations"
            ]
        ]
    ] = Field(alias="memberOrganizations")
    name: str


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizations(
    BaseModel
):
    access_approved_by_user_id: Optional[str] = Field(alias="accessApprovedByUserId")
    collaborative_id: str = Field(alias="collaborativeId")
    member_state: Optional[CollaborativeMemberOrganizationState] = Field(
        alias="memberState"
    )
    organization: Optional[
        "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsOrganization"
    ]
    submitted_by_user: Optional[
        "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsSubmittedByUser"
    ] = Field(alias="submittedByUser")
    submitted_timestamp: Optional[str] = Field(alias="submittedTimestamp")
    users_in_collaborative: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborative"
            ]
        ]
    ] = Field(alias="usersInCollaborative")


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsSubmittedByUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsSubmittedByUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsSubmittedByUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborative(
    BaseModel
):
    permission: Optional[CollaborativeMemberPermission]
    user: Optional[
        "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborativeUser"
    ]


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborativeUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborativeUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborativeUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminMigrateUsersCollaborativesOwnership.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnership.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizations.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsOrganization.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsSubmittedByUser.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsSubmittedByUserOrganization.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborative.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborativeUser.update_forward_refs()
PlatformAdminMigrateUsersCollaborativesOwnershipPlatformAdminMigrateUsersCollaborativesOwnershipMemberOrganizationsUsersInCollaborativeUserOrganization.update_forward_refs()
