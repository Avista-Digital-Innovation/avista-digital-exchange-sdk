# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import MeasureValueType


class OnTimeSeriesDbPublish(BaseModel):
    on_time_series_db_publish: Optional[
        List[Optional["OnTimeSeriesDbPublishOnTimeSeriesDbPublish"]]
    ] = Field(alias="onTimeSeriesDbPublish")


class OnTimeSeriesDbPublishOnTimeSeriesDbPublish(BaseModel):
    asset_id: str = Field(alias="assetId")
    attributes: Optional[
        List[Optional["OnTimeSeriesDbPublishOnTimeSeriesDbPublishAttributes"]]
    ]
    name: Optional[str]


class OnTimeSeriesDbPublishOnTimeSeriesDbPublishAttributes(BaseModel):
    attribute_type: MeasureValueType = Field(alias="attributeType")
    data: Optional[
        List[Optional["OnTimeSeriesDbPublishOnTimeSeriesDbPublishAttributesData"]]
    ]
    last_value: str = Field(alias="lastValue")
    last_value_time: str = Field(alias="lastValueTime")
    name: str


class OnTimeSeriesDbPublishOnTimeSeriesDbPublishAttributesData(BaseModel):
    timestamp: str
    value: str


OnTimeSeriesDbPublish.update_forward_refs()
OnTimeSeriesDbPublishOnTimeSeriesDbPublish.update_forward_refs()
OnTimeSeriesDbPublishOnTimeSeriesDbPublishAttributes.update_forward_refs()
OnTimeSeriesDbPublishOnTimeSeriesDbPublishAttributesData.update_forward_refs()
