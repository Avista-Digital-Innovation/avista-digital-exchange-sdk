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


class PlatformAdminRemoveCollaborativeMember(BaseModel):
    platform_admin_remove_collaborative_member: Optional[
        "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMember"
    ] = Field(alias="platformAdmin_removeCollaborativeMember")


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMember(
    BaseModel
):
    collaborative_id: str = Field(alias="collaborativeId")
    description: Optional[str]
    host_organization_id: str = Field(alias="hostOrganizationId")
    member_organizations: Optional[
        List[
            Optional[
                "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizations"
            ]
        ]
    ] = Field(alias="memberOrganizations")
    name: str


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizations(
    BaseModel
):
    access_approved_by_user_id: Optional[str] = Field(alias="accessApprovedByUserId")
    collaborative_id: str = Field(alias="collaborativeId")
    member_state: Optional[CollaborativeMemberOrganizationState] = Field(
        alias="memberState"
    )
    organization: Optional[
        "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsOrganization"
    ]
    submitted_by_user: Optional[
        "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsSubmittedByUser"
    ] = Field(alias="submittedByUser")
    submitted_timestamp: Optional[str] = Field(alias="submittedTimestamp")
    users_in_collaborative: Optional[
        List[
            Optional[
                "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborative"
            ]
        ]
    ] = Field(alias="usersInCollaborative")


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsSubmittedByUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsSubmittedByUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsSubmittedByUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborative(
    BaseModel
):
    permission: Optional[CollaborativeMemberPermission]
    user: Optional[
        "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborativeUser"
    ]


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborativeUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborativeUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborativeUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminRemoveCollaborativeMember.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMember.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizations.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsOrganization.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsSubmittedByUser.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsSubmittedByUserOrganization.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborative.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborativeUser.update_forward_refs()
PlatformAdminRemoveCollaborativeMemberPlatformAdminRemoveCollaborativeMemberMemberOrganizationsUsersInCollaborativeUserOrganization.update_forward_refs()
