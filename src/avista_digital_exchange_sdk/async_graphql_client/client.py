# Generated by ariadne-codegen on 2024-11-12 13:55
# Source: ../step_1_gqlg/output/queries.graphql

from typing import AsyncIterator, List

from .data_capture_publish_data import DataCapturePublishData
from .data_capture_start_capture import DataCaptureStartCapture
from .data_capture_stop_capture import DataCaptureStopCapture
from .input_types import DataCaptureDataRecordInput, IotDataRecordInput
from .iot_publish import IotPublish
from .modified_async_base_client import AsyncBaseClient
from .on_capture_publish_data import OnCapturePublishData
from .on_iot_publish import OnIotPublish


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def iot_publish(
        self, data: List[IotDataRecordInput], iot_endpoint_id: str
    ) -> IotPublish:
        query = gql(
            """
            mutation iot_publish($data: [IotDataRecordInput]!, $iotEndpointId: ID!) {
              iot_publish(data: $data, iotEndpointId: $iotEndpointId) {
                iotEndpointId
                failedRecords {
                  errors {
                    errorMessage
                    errorType
                  }
                  record {
                    attributes {
                      name
                      schemaType
                      value
                    }
                    iotEndpointId
                    timestamp
                  }
                }
                recordsWritten {
                  attributes {
                    name
                    schemaType
                    value
                  }
                  iotEndpointId
                  timestamp
                }
              }
            }
            """
        )
        variables: dict[str, object] = {
            "data": data, "iotEndpointId": iot_endpoint_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return IotPublish.parse_obj(data)

    async def data_capture_stop_capture(
        self, capture_id: str
    ) -> DataCaptureStopCapture:
        query = gql(
            """
            mutation dataCapture_stopCapture($captureId: ID!) {
              dataCapture_stopCapture(captureId: $captureId) {
                captureId
                captureType
                dataModel {
                  dateCreated
                  dateUpdated
                  errors
                  items {
                    attributes {
                      attributeType
                      description
                      displayName
                      schemaType
                      unit
                      userDefinedId
                    }
                    description
                    displayName
                    userDefinedId
                  }
                  state
                  version
                }
                dateCreated
                dateUpdated
                description
                displayName
                ownerUserId
                state
                stateHistory {
                  dateCreated
                  message
                  newState
                }
                timeSettings {
                  actualStartTime
                  actualStopTime
                  errors
                  scheduledStartTime
                  scheduledStopTime
                  startTimeType
                  state
                  stopTimeType
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"captureId": capture_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return DataCaptureStopCapture.parse_obj(data)

    async def data_capture_start_capture(
        self, capture_id: str
    ) -> DataCaptureStartCapture:
        query = gql(
            """
            mutation dataCapture_startCapture($captureId: ID!) {
              dataCapture_startCapture(captureId: $captureId) {
                captureId
                captureType
                dataModel {
                  dateCreated
                  dateUpdated
                  errors
                  items {
                    attributes {
                      attributeType
                      description
                      displayName
                      schemaType
                      unit
                      userDefinedId
                    }
                    description
                    displayName
                    userDefinedId
                  }
                  state
                  version
                }
                dateCreated
                dateUpdated
                description
                displayName
                ownerUserId
                state
                stateHistory {
                  dateCreated
                  message
                  newState
                }
                timeSettings {
                  actualStartTime
                  actualStopTime
                  errors
                  scheduledStartTime
                  scheduledStopTime
                  startTimeType
                  state
                  stopTimeType
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"captureId": capture_id}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return DataCaptureStartCapture.parse_obj(data)

    async def data_capture_publish_data(
        self, capture_id: str, data: List[DataCaptureDataRecordInput]
    ) -> DataCapturePublishData:
        query = gql(
            """
            mutation dataCapture_publishData($captureId: ID!, $data: [DataCaptureDataRecordInput]!) {
              dataCapture_publishData(captureId: $captureId, data: $data) {
                captureId
                dataWritten {
                  timestamp
                  userDefinedId
                  value
                }
                failedRecords {
                  attributeIndex
                  errorType
                  message
                  recordIndex
                }
                logs {
                  error
                  message
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"captureId": capture_id, "data": data}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return DataCapturePublishData.parse_obj(data)

    async def on_iot_publish(self, iot_endpoint_id: str) -> AsyncIterator[OnIotPublish]:
        query = gql(
            """
            subscription onIotPublish($iotEndpointId: ID!) {
              onIotPublish(iotEndpointId: $iotEndpointId) {
                iotEndpointId
                failedRecords {
                  errors {
                    errorMessage
                    errorType
                  }
                  record {
                    attributes {
                      name
                      schemaType
                      value
                    }
                    iotEndpointId
                    timestamp
                  }
                }
                recordsWritten {
                  attributes {
                    name
                    schemaType
                    value
                  }
                  iotEndpointId
                  timestamp
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"iotEndpointId": iot_endpoint_id}
        async for data in self.execute_ws(query=query, variables=variables, requestName="onIotPublish"):
            yield OnIotPublish.parse_obj(data)

    async def on_capture_publish_data(
        self, capture_id: str
    ) -> AsyncIterator[OnCapturePublishData]:
        query = gql(
            """
            subscription onCapturePublishData($captureId: ID!) {
              onCapturePublishData(captureId: $captureId) {
                captureId
                dataWritten {
                  timestamp
                  userDefinedId
                  value
                }
                failedRecords {
                  attributeIndex
                  errorType
                  message
                  recordIndex
                }
                logs {
                  error
                  message
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"captureId": capture_id}
        async for data in self.execute_ws(query=query, variables=variables, requestName="onCapturePublishData"):
            yield OnCapturePublishData.parse_obj(data)
