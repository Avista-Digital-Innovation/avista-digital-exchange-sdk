# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class StorageUpdateDataStore(BaseModel):
    storage_update_data_store: Optional[
        "StorageUpdateDataStoreStorageUpdateDataStore"
    ] = Field(alias="storage_updateDataStore")


class StorageUpdateDataStoreStorageUpdateDataStore(BaseModel):
    data_store_id: str = Field(alias="dataStoreId")
    description: Optional[str]
    home_directory_id: Optional[str] = Field(alias="homeDirectoryId")
    name: str
    owner_user_id: Optional[str] = Field(alias="ownerUserId")


StorageUpdateDataStore.update_forward_refs()
StorageUpdateDataStoreStorageUpdateDataStore.update_forward_refs()