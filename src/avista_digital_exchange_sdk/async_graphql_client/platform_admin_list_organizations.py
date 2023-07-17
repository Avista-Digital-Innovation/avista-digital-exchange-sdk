# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PlatformAdminListOrganizations(BaseModel):
    platform_admin_list_organizations: Optional[
        List[Optional["PlatformAdminListOrganizationsPlatformAdminListOrganizations"]]
    ] = Field(alias="platformAdmin_listOrganizations")


class PlatformAdminListOrganizationsPlatformAdminListOrganizations(BaseModel):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminListOrganizations.update_forward_refs()
PlatformAdminListOrganizationsPlatformAdminListOrganizations.update_forward_refs()