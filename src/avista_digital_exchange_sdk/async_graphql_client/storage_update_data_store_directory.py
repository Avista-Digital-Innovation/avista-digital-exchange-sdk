# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import DataStoreObjectType


class StorageUpdateDataStoreDirectory(BaseModel):
    storage_update_data_store_directory: Optional[
        "StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectory"
    ] = Field(alias="storage_updateDataStoreDirectory")


class StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectory(BaseModel):
    contents: Optional[
        List[
            Optional[
                "StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContents"
            ]
        ]
    ]
    data_store_directory_id: str = Field(alias="dataStoreDirectoryId")
    data_store_id: Optional[str] = Field(alias="dataStoreId")
    home_directory: Optional[bool] = Field(alias="homeDirectory")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")
    parent_directory_id: Optional[str] = Field(alias="parentDirectoryId")


class StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContents(BaseModel):
    data_store_directory: Optional[
        "StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectory"
    ] = Field(alias="dataStoreDirectory")
    object_type: DataStoreObjectType = Field(alias="objectType")


class StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectory(
    BaseModel
):
    contents: Optional[
        List[
            Optional[
                "StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectoryContents"
            ]
        ]
    ]
    data_store_directory_id: str = Field(alias="dataStoreDirectoryId")
    data_store_id: Optional[str] = Field(alias="dataStoreId")
    home_directory: Optional[bool] = Field(alias="homeDirectory")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")
    parent_directory_id: Optional[str] = Field(alias="parentDirectoryId")


class StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectoryContents(
    BaseModel
):
    data_store_file: Optional[
        "StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile"
    ] = Field(alias="dataStoreFile")
    object_type: DataStoreObjectType = Field(alias="objectType")


class StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile(
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


StorageUpdateDataStoreDirectory.update_forward_refs()
StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectory.update_forward_refs()
StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContents.update_forward_refs()
StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectory.update_forward_refs()
StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectoryContents.update_forward_refs()
StorageUpdateDataStoreDirectoryStorageUpdateDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile.update_forward_refs()
