# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ModelAttributeType, ModelSchemaType


class IotUpdateModel(BaseModel):
    iot_update_model: Optional["IotUpdateModelIotUpdateModel"] = Field(
        alias="iot_updateModel"
    )


class IotUpdateModelIotUpdateModel(BaseModel):
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    dtmi: str
    model_id: str = Field(alias="modelId")
    owner_user_id: str = Field(alias="ownerUserId")
    properties: Optional[List[Optional["IotUpdateModelIotUpdateModelProperties"]]]
    telemetry: Optional[List[Optional["IotUpdateModelIotUpdateModelTelemetry"]]]


class IotUpdateModelIotUpdateModelProperties(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    writable: Optional[bool]


class IotUpdateModelIotUpdateModelTelemetry(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


IotUpdateModel.update_forward_refs()
IotUpdateModelIotUpdateModel.update_forward_refs()
IotUpdateModelIotUpdateModelProperties.update_forward_refs()
IotUpdateModelIotUpdateModelTelemetry.update_forward_refs()
