# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class PlatformAdminUpdateOrganization(BaseModel):
    platform_admin_update_organization: Optional[
        "PlatformAdminUpdateOrganizationPlatformAdminUpdateOrganization"
    ] = Field(alias="platformAdmin_updateOrganization")


class PlatformAdminUpdateOrganizationPlatformAdminUpdateOrganization(BaseModel):
    host_organization: Optional[bool] = Field(alias="hostOrganization")
    name: str
    organization_id: str = Field(alias="organizationId")


PlatformAdminUpdateOrganization.update_forward_refs()
PlatformAdminUpdateOrganizationPlatformAdminUpdateOrganization.update_forward_refs()