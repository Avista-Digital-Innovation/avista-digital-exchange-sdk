# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import DataCaptureDataExportState, DataCaptureDataExportType


class DataCaptureGetActiveCaptureDataExportDownloadUrl(BaseModel):
    data_capture_get_active_capture_data_export_download_url: Optional[
        "DataCaptureGetActiveCaptureDataExportDownloadUrlDataCaptureGetActiveCaptureDataExportDownloadUrl"
    ] = Field(alias="dataCapture_getActiveCaptureDataExportDownloadUrl")


class DataCaptureGetActiveCaptureDataExportDownloadUrlDataCaptureGetActiveCaptureDataExportDownloadUrl(
    BaseModel
):
    date_completed: Optional[str] = Field(alias="dateCompleted")
    date_started: Optional[str] = Field(alias="dateStarted")
    export_type: Optional[DataCaptureDataExportType] = Field(alias="exportType")
    logs: Optional[List[Optional[str]]]
    name: Optional[str]
    state: DataCaptureDataExportState
    url: Optional[str]


DataCaptureGetActiveCaptureDataExportDownloadUrl.update_forward_refs()
DataCaptureGetActiveCaptureDataExportDownloadUrlDataCaptureGetActiveCaptureDataExportDownloadUrl.update_forward_refs()
