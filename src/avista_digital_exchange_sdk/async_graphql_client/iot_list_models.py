# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ModelAttributeType, ModelSchemaType


class IotListModels(BaseModel):
    iot_list_models: Optional[List[Optional["IotListModelsIotListModels"]]] = Field(
        alias="iot_listModels"
    )


class IotListModelsIotListModels(BaseModel):
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    dtmi: str
    model_id: str = Field(alias="modelId")
    owner_user_id: str = Field(alias="ownerUserId")
    properties: Optional[List[Optional["IotListModelsIotListModelsProperties"]]]
    telemetry: Optional[List[Optional["IotListModelsIotListModelsTelemetry"]]]


class IotListModelsIotListModelsProperties(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    writable: Optional[bool]


class IotListModelsIotListModelsTelemetry(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


IotListModels.update_forward_refs()
IotListModelsIotListModels.update_forward_refs()
IotListModelsIotListModelsProperties.update_forward_refs()
IotListModelsIotListModelsTelemetry.update_forward_refs()