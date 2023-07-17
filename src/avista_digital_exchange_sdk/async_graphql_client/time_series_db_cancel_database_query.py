# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class TimeSeriesDbCancelDatabaseQuery(BaseModel):
    time_series_db_cancel_database_query: Optional[
        "TimeSeriesDbCancelDatabaseQueryTimeSeriesDbCancelDatabaseQuery"
    ] = Field(alias="timeSeriesDb_cancelDatabaseQuery")


class TimeSeriesDbCancelDatabaseQueryTimeSeriesDbCancelDatabaseQuery(BaseModel):
    error_message: Optional[str] = Field(alias="errorMessage")
    http_status_code: Optional[int] = Field(alias="httpStatusCode")


TimeSeriesDbCancelDatabaseQuery.update_forward_refs()
TimeSeriesDbCancelDatabaseQueryTimeSeriesDbCancelDatabaseQuery.update_forward_refs()