# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import DataStoreObjectType


class StorageCreateDataStoreDirectory(BaseModel):
    storage_create_data_store_directory: Optional[
        "StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectory"
    ] = Field(alias="storage_createDataStoreDirectory")


class StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectory(BaseModel):
    contents: Optional[
        List[
            Optional[
                "StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContents"
            ]
        ]
    ]
    data_store_directory_id: str = Field(alias="dataStoreDirectoryId")
    data_store_id: Optional[str] = Field(alias="dataStoreId")
    home_directory: Optional[bool] = Field(alias="homeDirectory")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")
    parent_directory_id: Optional[str] = Field(alias="parentDirectoryId")


class StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContents(BaseModel):
    data_store_directory: Optional[
        "StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectory"
    ] = Field(alias="dataStoreDirectory")
    object_type: DataStoreObjectType = Field(alias="objectType")


class StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectory(
    BaseModel
):
    contents: Optional[
        List[
            Optional[
                "StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectoryContents"
            ]
        ]
    ]
    data_store_directory_id: str = Field(alias="dataStoreDirectoryId")
    data_store_id: Optional[str] = Field(alias="dataStoreId")
    home_directory: Optional[bool] = Field(alias="homeDirectory")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")
    parent_directory_id: Optional[str] = Field(alias="parentDirectoryId")


class StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectoryContents(
    BaseModel
):
    data_store_file: Optional[
        "StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile"
    ] = Field(alias="dataStoreFile")
    object_type: DataStoreObjectType = Field(alias="objectType")


class StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile(
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


StorageCreateDataStoreDirectory.update_forward_refs()
StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectory.update_forward_refs()
StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContents.update_forward_refs()
StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectory.update_forward_refs()
StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectoryContents.update_forward_refs()
StorageCreateDataStoreDirectoryStorageCreateDataStoreDirectoryContentsDataStoreDirectoryContentsDataStoreFile.update_forward_refs()