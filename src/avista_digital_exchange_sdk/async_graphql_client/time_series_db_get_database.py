# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class TimeSeriesDbGetDatabase(BaseModel):
    time_series_db_get_database: Optional[
        "TimeSeriesDbGetDatabaseTimeSeriesDbGetDatabase"
    ] = Field(alias="timeSeriesDb_getDatabase")


class TimeSeriesDbGetDatabaseTimeSeriesDbGetDatabase(BaseModel):
    database_name: Optional[str] = Field(alias="databaseName")
    description: Optional[str]
    name: str
    owner_user_id: str = Field(alias="ownerUserId")
    table_name: Optional[str] = Field(alias="tableName")
    time_series_db_id: str = Field(alias="timeSeriesDbId")


TimeSeriesDbGetDatabase.update_forward_refs()
TimeSeriesDbGetDatabaseTimeSeriesDbGetDatabase.update_forward_refs()