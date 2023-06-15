# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class StorageGetDataStoreZipDownloadUrl(BaseModel):
    storage_get_data_store_zip_download_url: Optional[
        "StorageGetDataStoreZipDownloadUrlStorageGetDataStoreZipDownloadUrl"
    ] = Field(alias="storage_getDataStoreZipDownloadUrl")


class StorageGetDataStoreZipDownloadUrlStorageGetDataStoreZipDownloadUrl(BaseModel):
    item_id: Optional[str] = Field(alias="itemId")
    upload_id: Optional[str] = Field(alias="uploadId")
    url: Optional[str]


StorageGetDataStoreZipDownloadUrl.update_forward_refs()
StorageGetDataStoreZipDownloadUrlStorageGetDataStoreZipDownloadUrl.update_forward_refs()
