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


class DataCaptureNotifyCaptureComplete(BaseModel):
    data_capture_notify_capture_complete: Optional[
        "DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureComplete"
    ] = Field(alias="dataCapture_notifyCaptureComplete")


class DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureComplete(BaseModel):
    capture_id: str = Field(alias="captureId")
    capture_type: DataCaptureType = Field(alias="captureType")
    data_model: Optional[
        "DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModel"
    ] = Field(alias="dataModel")
    date_created: str = Field(alias="dateCreated")
    date_updated: str = Field(alias="dateUpdated")
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    owner_user_id: str = Field(alias="ownerUserId")
    state: DataCaptureState
    state_history: Optional[
        List[
            Optional[
                "DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteStateHistory"
            ]
        ]
    ] = Field(alias="stateHistory")
    time_settings: Optional[
        "DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteTimeSettings"
    ] = Field(alias="timeSettings")


class DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModel(
    BaseModel
):
    date_created: Optional[str] = Field(alias="dateCreated")
    date_updated: Optional[str] = Field(alias="dateUpdated")
    errors: Optional[List[Optional[str]]]
    items: List[
        Optional[
            "DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModelItems"
        ]
    ]
    state: DataCaptureDataModelState
    version: Optional[int]


class DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModelItems(
    BaseModel
):
    attributes: Optional[
        List[
            Optional[
                "DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModelItemsAttributes"
            ]
        ]
    ]
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    user_defined_id: str = Field(alias="userDefinedId")


class DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModelItemsAttributes(
    BaseModel
):
    attribute_type: DataCaptureAssetAttributeType = Field(alias="attributeType")
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    schema_type: DataCaptureAssetAttributeSchemaType = Field(alias="schemaType")
    unit: Optional[str]
    user_defined_id: str = Field(alias="userDefinedId")


class DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteStateHistory(
    BaseModel
):
    date_created: str = Field(alias="dateCreated")
    message: Optional[str]
    new_state: DataCaptureState = Field(alias="newState")


class DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteTimeSettings(
    BaseModel
):
    actual_start_time: Optional[str] = Field(alias="actualStartTime")
    actual_stop_time: Optional[str] = Field(alias="actualStopTime")
    errors: Optional[List[Optional[str]]]
    scheduled_start_time: Optional[str] = Field(alias="scheduledStartTime")
    scheduled_stop_time: Optional[str] = Field(alias="scheduledStopTime")
    start_time_type: DataCaptureTimeConfigType = Field(alias="startTimeType")
    state: Optional[DataCaptureTimeConfigurationState]
    stop_time_type: DataCaptureTimeConfigType = Field(alias="stopTimeType")


DataCaptureNotifyCaptureComplete.update_forward_refs()
DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureComplete.update_forward_refs()
DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModel.update_forward_refs()
DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModelItems.update_forward_refs()
DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteDataModelItemsAttributes.update_forward_refs()
DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteStateHistory.update_forward_refs()
DataCaptureNotifyCaptureCompleteDataCaptureNotifyCaptureCompleteTimeSettings.update_forward_refs()
