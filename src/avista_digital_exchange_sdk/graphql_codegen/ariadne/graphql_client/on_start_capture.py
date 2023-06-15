# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    DataCaptureAssetAttributeSchemaType,
    DataCaptureAssetAttributeType,
    DataCaptureDataModelState,
    DataCaptureState,
    DataCaptureTimeConfigType,
    DataCaptureTimeConfigurationState,
    DataCaptureType,
)


class OnStartCapture(BaseModel):
    on_start_capture: Optional["OnStartCaptureOnStartCapture"] = Field(
        alias="onStartCapture"
    )


class OnStartCaptureOnStartCapture(BaseModel):
    capture_id: str = Field(alias="captureId")
    capture_type: DataCaptureType = Field(alias="captureType")
    data_model: Optional["OnStartCaptureOnStartCaptureDataModel"] = Field(
        alias="dataModel"
    )
    date_created: str = Field(alias="dateCreated")
    date_updated: str = Field(alias="dateUpdated")
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    owner_user_id: str = Field(alias="ownerUserId")
    state: DataCaptureState
    state_history: Optional[
        List[Optional["OnStartCaptureOnStartCaptureStateHistory"]]
    ] = Field(alias="stateHistory")
    time_settings: Optional["OnStartCaptureOnStartCaptureTimeSettings"] = Field(
        alias="timeSettings"
    )


class OnStartCaptureOnStartCaptureDataModel(BaseModel):
    date_created: Optional[str] = Field(alias="dateCreated")
    date_updated: Optional[str] = Field(alias="dateUpdated")
    errors: Optional[List[Optional[str]]]
    items: List[Optional["OnStartCaptureOnStartCaptureDataModelItems"]]
    state: DataCaptureDataModelState
    version: Optional[int]


class OnStartCaptureOnStartCaptureDataModelItems(BaseModel):
    attributes: Optional[
        List[Optional["OnStartCaptureOnStartCaptureDataModelItemsAttributes"]]
    ]
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    user_defined_id: str = Field(alias="userDefinedId")


class OnStartCaptureOnStartCaptureDataModelItemsAttributes(BaseModel):
    attribute_type: DataCaptureAssetAttributeType = Field(alias="attributeType")
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    schema_type: DataCaptureAssetAttributeSchemaType = Field(alias="schemaType")
    unit: Optional[str]
    user_defined_id: str = Field(alias="userDefinedId")


class OnStartCaptureOnStartCaptureStateHistory(BaseModel):
    date_created: str = Field(alias="dateCreated")
    message: Optional[str]
    new_state: DataCaptureState = Field(alias="newState")


class OnStartCaptureOnStartCaptureTimeSettings(BaseModel):
    actual_start_time: Optional[str] = Field(alias="actualStartTime")
    actual_stop_time: Optional[str] = Field(alias="actualStopTime")
    errors: Optional[List[Optional[str]]]
    scheduled_start_time: Optional[str] = Field(alias="scheduledStartTime")
    scheduled_stop_time: Optional[str] = Field(alias="scheduledStopTime")
    start_time_type: DataCaptureTimeConfigType = Field(alias="startTimeType")
    state: Optional[DataCaptureTimeConfigurationState]
    stop_time_type: DataCaptureTimeConfigType = Field(alias="stopTimeType")


OnStartCapture.update_forward_refs()
OnStartCaptureOnStartCapture.update_forward_refs()
OnStartCaptureOnStartCaptureDataModel.update_forward_refs()
OnStartCaptureOnStartCaptureDataModelItems.update_forward_refs()
OnStartCaptureOnStartCaptureDataModelItemsAttributes.update_forward_refs()
OnStartCaptureOnStartCaptureStateHistory.update_forward_refs()
OnStartCaptureOnStartCaptureTimeSettings.update_forward_refs()
