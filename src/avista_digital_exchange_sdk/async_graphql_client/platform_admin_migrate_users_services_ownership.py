# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

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
    ModelAttributeType,
    ModelSchemaType,
    ServiceType,
)


class PlatformAdminMigrateUsersServicesOwnership(BaseModel):
    platform_admin_migrate_users_services_ownership: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnership"
            ]
        ]
    ] = Field(alias="platformAdmin_migrateUsersServicesOwnership")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnership(
    BaseModel
):
    data_capture: Optional[
        "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCapture"
    ] = Field(alias="dataCapture")
    data_store: Optional[
        "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataStore"
    ] = Field(alias="dataStore")
    iot_endpoint_group: Optional[
        "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroup"
    ] = Field(alias="iotEndpointGroup")
    ocs_adapter: Optional[
        "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipOcsAdapter"
    ] = Field(alias="ocsAdapter")
    service_id: str = Field(alias="serviceId")
    service_type: ServiceType = Field(alias="serviceType")
    time_series_db: Optional[
        "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipTimeSeriesDb"
    ] = Field(alias="timeSeriesDb")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCapture(
    BaseModel
):
    capture_id: str = Field(alias="captureId")
    capture_type: DataCaptureType = Field(alias="captureType")
    data_model: Optional[
        "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModel"
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
                "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureStateHistory"
            ]
        ]
    ] = Field(alias="stateHistory")
    time_settings: Optional[
        "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureTimeSettings"
    ] = Field(alias="timeSettings")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModel(
    BaseModel
):
    date_created: Optional[str] = Field(alias="dateCreated")
    date_updated: Optional[str] = Field(alias="dateUpdated")
    errors: Optional[List[Optional[str]]]
    items: List[
        Optional[
            "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModelItems"
        ]
    ]
    state: DataCaptureDataModelState
    version: Optional[int]


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModelItems(
    BaseModel
):
    attributes: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModelItemsAttributes"
            ]
        ]
    ]
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    user_defined_id: str = Field(alias="userDefinedId")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModelItemsAttributes(
    BaseModel
):
    attribute_type: DataCaptureAssetAttributeType = Field(alias="attributeType")
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    schema_type: DataCaptureAssetAttributeSchemaType = Field(alias="schemaType")
    unit: Optional[str]
    user_defined_id: str = Field(alias="userDefinedId")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureStateHistory(
    BaseModel
):
    date_created: str = Field(alias="dateCreated")
    message: Optional[str]
    new_state: DataCaptureState = Field(alias="newState")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureTimeSettings(
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


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataStore(
    BaseModel
):
    data_store_id: str = Field(alias="dataStoreId")
    description: Optional[str]
    home_directory_id: Optional[str] = Field(alias="homeDirectoryId")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroup(
    BaseModel
):
    description: Optional[str]
    endpoints: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpoints"
            ]
        ]
    ]
    iot_endpoint_ids: Optional[List[Optional[str]]] = Field(alias="iotEndpointIds")
    iot_group_id: str = Field(alias="iotGroupId")
    iot_hub_id: str = Field(alias="iotHubId")
    name: str
    owner_user_id: str = Field(alias="ownerUserId")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpoints(
    BaseModel
):
    description: Optional[str]
    iot_endpoint_id: str = Field(alias="iotEndpointId")
    iot_hub_id: str = Field(alias="iotHubId")
    model_id: str = Field(alias="modelId")
    name: str
    owner_user_id: str = Field(alias="ownerUserId")
    properties: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpointsProperties"
            ]
        ]
    ]
    telemetry: Optional[
        List[
            Optional[
                "PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpointsTelemetry"
            ]
        ]
    ]


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpointsProperties(
    BaseModel
):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    timestamp: Optional[str]
    value: Optional[str]
    writable: Optional[bool]


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpointsTelemetry(
    BaseModel
):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipOcsAdapter(
    BaseModel
):
    ocs_adapter_id: str = Field(alias="ocsAdapterId")


class PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipTimeSeriesDb(
    BaseModel
):
    database_name: Optional[str] = Field(alias="databaseName")
    description: Optional[str]
    name: str
    owner_user_id: str = Field(alias="ownerUserId")
    table_name: Optional[str] = Field(alias="tableName")
    time_series_db_id: str = Field(alias="timeSeriesDbId")


PlatformAdminMigrateUsersServicesOwnership.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnership.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCapture.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModel.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModelItems.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureDataModelItemsAttributes.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureStateHistory.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataCaptureTimeSettings.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipDataStore.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroup.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpoints.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpointsProperties.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipIotEndpointGroupEndpointsTelemetry.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipOcsAdapter.update_forward_refs()
PlatformAdminMigrateUsersServicesOwnershipPlatformAdminMigrateUsersServicesOwnershipTimeSeriesDb.update_forward_refs()
