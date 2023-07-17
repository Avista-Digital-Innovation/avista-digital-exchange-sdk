# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class DataCaptureGetPythonSDKSample(BaseModel):
    data_capture_get_python_s_d_k_sample: Optional[str] = Field(
        alias="dataCapture_getPythonSDKSample"
    )


DataCaptureGetPythonSDKSample.update_forward_refs()