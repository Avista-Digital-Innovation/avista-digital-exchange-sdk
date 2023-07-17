# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class PlatformAdminDeleteOrganization(BaseModel):
    platform_admin_delete_organization: Optional[
        "PlatformAdminDeleteOrganizationPlatformAdminDeleteOrganization"
    ] = Field(alias="platformAdmin_deleteOrganization")


class PlatformAdminDeleteOrganizationPlatformAdminDeleteOrganization(BaseModel):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminDeleteOrganization.update_forward_refs()
PlatformAdminDeleteOrganizationPlatformAdminDeleteOrganization.update_forward_refs()