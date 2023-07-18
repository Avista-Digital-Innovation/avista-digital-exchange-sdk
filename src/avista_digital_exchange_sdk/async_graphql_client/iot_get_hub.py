# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class IotGetHub(BaseModel):
    iot_get_hub: Optional["IotGetHubIotGetHub"] = Field(alias="iot_getHub")


class IotGetHubIotGetHub(BaseModel):
    description: Optional[str]
    iot_hub_id: str = Field(alias="iotHubId")
    name: str
    owner_user_id: str = Field(alias="ownerUserId")


IotGetHub.update_forward_refs()
IotGetHubIotGetHub.update_forward_refs()
