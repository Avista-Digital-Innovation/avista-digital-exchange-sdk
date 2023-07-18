# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import DataStoreObjectType


class StorageDeleteDataStoreDirectory(BaseModel):
    storage_delete_data_store_directory: Optional[
        "StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectory"
    ] = Field(alias="storage_deleteDataStoreDirectory")


class StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectory(BaseModel):
    contents: Optional[
        List[
            Optional[
                "StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContents"
            ]
        ]
    ]
    data_store_directory_id: str = Field(alias="dataStoreDirectoryId")
    data_store_id: Optional[str] = Field(alias="dataStoreId")
    home_directory: Optional[bool] = Field(alias="homeDirectory")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")
    parent_directory_id: Optional[str] = Field(alias="parentDirectoryId")


class StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContents(BaseModel):
    data_store_directory: Optional[
        "StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectory"
    ] = Field(alias="dataStoreDirectory")
    object_type: DataStoreObjectType = Field(alias="objectType")


class StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectory(
    BaseModel
):
    contents: Optional[
        List[
            Optional[
                "StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectoryContents"
            ]
        ]
    ]
    data_store_directory_id: str = Field(alias="dataStoreDirectoryId")
    data_store_id: Optional[str] = Field(alias="dataStoreId")
    home_directory: Optional[bool] = Field(alias="homeDirectory")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")
    parent_directory_id: Optional[str] = Field(alias="parentDirectoryId")


class StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectoryContents(
    BaseModel
):
    data_store_file: Optional[
        "StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile"
    ] = Field(alias="dataStoreFile")
    object_type: DataStoreObjectType = Field(alias="objectType")


class StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile(
    BaseModel
):
    content_type: Optional[str] = Field(alias="contentType")
    data_store_directory_id: Optional[str] = Field(alias="dataStoreDirectoryId")
    data_store_file_id: str = Field(alias="dataStoreFileId")
    data_store_id: Optional[str] = Field(alias="dataStoreId")
    data_view_ids: Optional[List[Optional[str]]] = Field(alias="dataViewIds")
    description: Optional[str]
    file_extension: Optional[str] = Field(alias="fileExtension")
    last_modified: Optional[str] = Field(alias="lastModified")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")
    s3_confirmed_upload: Optional[bool] = Field(alias="s3ConfirmedUpload")
    storage_size_bytes: Optional[int] = Field(alias="storageSizeBytes")


StorageDeleteDataStoreDirectory.update_forward_refs()
StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectory.update_forward_refs()
StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContents.update_forward_refs()
StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectory.update_forward_refs()
StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectoryContents.update_forward_refs()
StorageDeleteDataStoreDirectoryStorageDeleteDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile.update_forward_refs()
