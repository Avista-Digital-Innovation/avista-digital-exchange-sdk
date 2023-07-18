# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import UserAccountState, UserRole


class PlatformAdminCreateUser(BaseModel):
    platform_admin_create_user: Optional[
        "PlatformAdminCreateUserPlatformAdminCreateUser"
    ] = Field(alias="platformAdmin_createUser")


class PlatformAdminCreateUserPlatformAdminCreateUser(BaseModel):
    email: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    last_active: Optional[str] = Field(alias="lastActive")
    last_name: Optional[str] = Field(alias="lastName")
    mobile: Optional[str]
    organization: Optional["PlatformAdminCreateUserPlatformAdminCreateUserOrganization"]
    user_account_state: Optional[UserAccountState] = Field(alias="userAccountState")
    user_id: str = Field(alias="userId")
    user_roles: Optional[List[Optional[UserRole]]] = Field(alias="userRoles")


class PlatformAdminCreateUserPlatformAdminCreateUserOrganization(BaseModel):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminCreateUser.update_forward_refs()
PlatformAdminCreateUserPlatformAdminCreateUser.update_forward_refs()
PlatformAdminCreateUserPlatformAdminCreateUserOrganization.update_forward_refs()
