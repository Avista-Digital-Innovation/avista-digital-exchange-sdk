
from enum import Enum
import json
from typing import List

from .async_graphql_client.data_capture_publish_data import DataCapturePublishDataDataCapturePublishData

from .async_graphql_client.iot_publish import IotPublishIotPublish


class TimeUnitEnum(Enum):
    MILLISECONDS = 1


class DxTypeBaseClass(object):
    def __init__(self) -> None:
        pass

    def toDict(self) -> dict:
        def handleList(listValue):
            result = []
            for item in listValue:
                if type(item) == list:
                    result.append(handleList(item))
                elif issubclass(type(item), DxTypeBaseClass):
                    result.append(item.toDict())
                else:
                    result.append(item)
            return result

        variables = vars(self)
        result = {}
        for key, value in variables.items():
            if issubclass(type(value), DxTypeBaseClass):
                result[key] = value.toDict()
            elif type(value) == list:
                result[key] = handleList(value)
            else:
                result[key] = value
        return result

    def __str__(self) -> str:
        return f'{json.dumps(self.toDict(), sort_keys=True, indent=4)}'


class CaptureDataRecordInput(DxTypeBaseClass):
    timestamp: str
    timeUnit: str
    attributeValues: dict

    def __init__(self, timestamp: str, timeUnit: str, attributeValues: dict) -> None:
        self.timestamp = timestamp
        self.timeUnit = timeUnit
        self.attributeValues = attributeValues


class PublishCaptureDataSuccessfulRecord(DxTypeBaseClass):
    timestamp: str
    timeUnit: str
    attributeId: str
    attributeValue: str

    def __init__(self,
                 timestamp: str,
                 timeUnit: str,
                 attributeId: str,
                 attributeValue: str) -> None:
        self.timestamp = timestamp
        self.timeUnit = timeUnit
        self.attributeId = attributeId
        self.attributeValue = attributeValue


class PublishCaptureDataFailedRecord(DxTypeBaseClass):
    timestamp: str
    timeUnit: str
    attributeId: str
    attributeValue: str
    message: str

    def __init__(self,
                 timestamp: str,
                 timeUnit: str,
                 attributeId: str,
                 attributeValue: str,
                 message: str) -> None:
        self.timestamp = timestamp
        self.timeUnit = timeUnit
        self.attributeId = attributeId
        self.attributeValue = attributeValue
        self.message = message


class PublishCaptureDataResult(DxTypeBaseClass):
    success: bool
    captureId: str
    recordsWritten: List[PublishCaptureDataSuccessfulRecord] | None
    recordsFailed: List[PublishCaptureDataFailedRecord] | None
    error: str | None

    def __init__(self,
                 success: bool,
                 captureId: str,
                 recordsWritten: List[PublishCaptureDataSuccessfulRecord] | None = None,
                 recordsFailed: List[str] | None = None,
                 error: str | None = None) -> None:
        self.success = success
        self.captureId = captureId
        self.recordsWritten = recordsWritten
        self.recordsFailed = recordsFailed
        self.error = error

    @staticmethod
    def fromCapturePublishResult(result: DataCapturePublishDataDataCapturePublishData):
        recordsWritten = []
        recordsFailed = []
        for record in result.data_written:
            recordsWritten.append(
                PublishCaptureDataSuccessfulRecord(
                    timestamp=record.timestamp,
                    timeUnit="MILLISECONDS",
                    attributeId=record.user_defined_id,
                    attributeValue=record.value))
        for record in result.failed_records:
            recordsFailed.append(
                PublishCaptureDataFailedRecord(
                    timestamp=record.timestamp,
                    timeUnit="MILLISECONDS",
                    attributeId=record.user_defined_id,
                    attributeValue=record.value,
                    message=""))
        return PublishCaptureDataResult(success=True, captureId=result.capture_id, recordsWritten=recordsWritten, recordsFailed=recordsFailed)


class StartCaptureResult(DxTypeBaseClass):
    success: bool
    captureId: str
    startedAt: str | None
    error: str | None

    def __init__(self, success: bool, captureId: str, startedAt: str | None = None, error: str | None = None) -> None:
        self.success = success
        self.captureId = captureId
        self.startedAt = startedAt
        self.error = error


class StopCaptureResult(DxTypeBaseClass):
    success: bool
    captureId: str
    stoppedAt: str | None
    error: str | None

    def __init__(self, success: bool, captureId: str, stoppedAt: str | None = None, error: str | None = None) -> None:
        self.success = success
        self.captureId = captureId
        self.stoppedAt = stoppedAt
        self.error = error


class IotEndpointAttributeValue(DxTypeBaseClass):
    name: str
    schemaType: str
    value: str

    def __init__(self,
                 name: str,
                 schemaType: str,
                 value: str) -> None:
        self.name = name
        self.schemaType = schemaType
        self.value = value

    def toDict(self):
        return vars(self)


class IotEndpointDataRecord(DxTypeBaseClass):
    attributes: List[IotEndpointAttributeValue]
    iotEndpointId: str
    timestamp: str
    timeUnit: str

    def __init__(self,
                 attributes: List[IotEndpointAttributeValue],
                 iotEndpointId: str,
                 timestamp: str,
                 timeUnit: str) -> None:
        self.attributes = attributes
        self.iotEndpointId = iotEndpointId
        self.timestamp = timestamp
        self.timeUnit = timeUnit

    def toDict(self):
        result = vars(self)
        result['attributes'] = list(map(lambda x: x.toDict(), self.attributes))
        return (result)


class IotEndpointDataRecordError(DxTypeBaseClass):
    errorMessage: str
    errorType: str

    def __init__(self,
                 errorMessage: str,
                 errorType: str) -> None:
        self.errorMessage = errorMessage
        self.errorType = errorType

    def toDict(self):
        result = vars(self)
        return result


class IotEndpointPublishDataFailedRecord(DxTypeBaseClass):
    record: IotEndpointDataRecord
    errors: List[IotEndpointDataRecordError]

    def __init__(self,
                 record: IotEndpointDataRecord,
                 errors: List[IotEndpointDataRecordError]) -> None:
        self.record = record
        self.errors = errors

    def toDict(self):
        result = {
            "record": self.record.toDict(),
            "errors": list(map(lambda x: x.toDict(), self.errors)),
        }
        return result


class IotEndpointPublishDataResult(DxTypeBaseClass):
    iotEndpointId: str
    recordsWritten: List[IotEndpointDataRecord] | None
    failedRecords: List[IotEndpointPublishDataFailedRecord] | None

    def __init__(self,
                 iotEndpointId: str,
                 recordsWritten: List[IotEndpointDataRecord] | None = None,
                 failedRecords: List[IotEndpointPublishDataFailedRecord] | None = None) -> None:
        self.iotEndpointId = iotEndpointId
        self.recordsWritten = recordsWritten
        self.failedRecords = failedRecords

    def toDict(self):
        result = {
            "iotEndpointId": self.iotEndpointId,
            "recordsWritten": list(map(lambda x: x.toDict(), self.recordsWritten)),
            "failedRecords": list(map(lambda x: x.toDict(), self.failedRecords)),
        }
        return result

    @staticmethod
    def fromIotEndpointPublishResult(result: IotPublishIotPublish):
        recordsWritten = []
        failedRecords = []

        # Process successful records
        for record in result.records_written:
            recordsWritten.append(
                IotEndpointDataRecord(
                    attributes=list(map(lambda entry: IotEndpointAttributeValue(
                        entry.name, entry.schema_type, entry.value), record.attributes)),
                    iotEndpointId=record.iot_endpoint_id,
                    timestamp=record.timestamp,
                    timeUnit="MILLISECONDS"))

        # Process failed records
        for record in result.failed_records:
            failedRecords.append(
                IotEndpointPublishDataFailedRecord(
                    record=IotEndpointDataRecord(
                        attributes=list(map(lambda entry: IotEndpointAttributeValue(
                            entry.name, entry.schema_type, entry.value), record.attributes)),
                        iotEndpointId=record.iot_endpoint_id,
                        timestamp=record.timestamp,
                        timeUnit="MILLISECONDS"),
                    errors=map(lambda entry: IotEndpointDataRecordError(entry), record.errors)))

        return IotEndpointPublishDataResult(
            iotEndpointId=result.iot_endpoint_id,
            recordsWritten=recordsWritten,
            failedRecords=failedRecords)
