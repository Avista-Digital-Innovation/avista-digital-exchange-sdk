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


class PlatformAdminListCollaboratives(BaseModel):
    platform_admin_list_collaboratives: Optional[
        List[Optional["PlatformAdminListCollaborativesPlatformAdminListCollaboratives"]]
    ] = Field(alias="platformAdmin_listCollaboratives")


class PlatformAdminListCollaborativesPlatformAdminListCollaboratives(BaseModel):
    collaborative_id: str = Field(alias="collaborativeId")
    description: Optional[str]
    host_organization_id: str = Field(alias="hostOrganizationId")
    member_organizations: Optional[
        List[
            Optional[
                "PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizations"
            ]
        ]
    ] = Field(alias="memberOrganizations")
    name: str


class PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizations(
    BaseModel
):
    access_approved_by_user_id: Optional[str] = Field(alias="accessApprovedByUserId")
    collaborative_id: str = Field(alias="collaborativeId")
    member_state: Optional[CollaborativeMemberOrganizationState] = Field(
        alias="memberState"
    )
    organization: Optional[
        "PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsOrganization"
    ]
    submitted_by_user: Optional[
        "PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsSubmittedByUser"
    ] = Field(alias="submittedByUser")
    submitted_timestamp: Optional[str] = Field(alias="submittedTimestamp")
    users_in_collaborative: Optional[
        List[
            Optional[
                "PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborative"
            ]
        ]
    ] = Field(alias="usersInCollaborative")


class PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsSubmittedByUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsSubmittedByUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsSubmittedByUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


class PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborative(
    BaseModel
):
    permission: Optional[CollaborativeMemberPermission]
    user: Optional[
        "PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborativeUser"
    ]


class PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborativeUser(
    BaseModel
):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional[
        "PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborativeUserOrganization"
    ]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborativeUserOrganization(
    BaseModel
):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminListCollaboratives.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaboratives.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizations.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsOrganization.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsSubmittedByUser.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsSubmittedByUserOrganization.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborative.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborativeUser.update_forward_refs()
PlatformAdminListCollaborativesPlatformAdminListCollaborativesMemberOrganizationsUsersInCollaborativeUserOrganization.update_forward_refs()
