# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import UserAccountState, UserRole


class PlatformAdminListUsers(BaseModel):
    platform_admin_list_users: Optional[
        List[Optional["PlatformAdminListUsersPlatformAdminListUsers"]]
    ] = Field(alias="platformAdmin_listUsers")


class PlatformAdminListUsersPlatformAdminListUsers(BaseModel):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional["PlatformAdminListUsersPlatformAdminListUsersOrganization"]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminListUsersPlatformAdminListUsersOrganization(BaseModel):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminListUsers.update_forward_refs()
PlatformAdminListUsersPlatformAdminListUsers.update_forward_refs()
PlatformAdminListUsersPlatformAdminListUsersOrganization.update_forward_refs()
