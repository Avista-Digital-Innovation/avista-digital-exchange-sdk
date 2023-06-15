# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ExportFileFormat


class OnNotifyIotQueryExportComplete(BaseModel):
    on_notify_iot_query_export_complete: Optional[
        "OnNotifyIotQueryExportCompleteOnNotifyIotQueryExportComplete"
    ] = Field(alias="onNotifyIotQueryExportComplete")


class OnNotifyIotQueryExportCompleteOnNotifyIotQueryExportComplete(BaseModel):
    file_format: ExportFileFormat = Field(alias="fileFormat")
    file_size_bytes: Optional[int] = Field(alias="fileSizeBytes")
    query_id: str = Field(alias="queryId")
    url: str


OnNotifyIotQueryExportComplete.update_forward_refs()
OnNotifyIotQueryExportCompleteOnNotifyIotQueryExportComplete.update_forward_refs()
