# Generated by ariadne-codegen on 2023-06-08 15:03
# Source: ../gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class TimeSeriesDbDeleteDatabase(BaseModel):
    time_series_db_delete_database: Optional[
        "TimeSeriesDbDeleteDatabaseTimeSeriesDbDeleteDatabase"
    ] = Field(alias="timeSeriesDb_deleteDatabase")


class TimeSeriesDbDeleteDatabaseTimeSeriesDbDeleteDatabase(BaseModel):
    database_name: Optional[str] = Field(alias="databaseName")
    description: Optional[str]
    name: str
    owner_user_id: str = Field(alias="ownerUserId")
    table_name: Optional[str] = Field(alias="tableName")
    time_series_db_id: str = Field(alias="timeSeriesDbId")


TimeSeriesDbDeleteDatabase.update_forward_refs()
TimeSeriesDbDeleteDatabaseTimeSeriesDbDeleteDatabase.update_forward_refs()
