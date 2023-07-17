# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../input/schema.graphql

from enum import Enum


class AuthenticationTokenType(str, Enum):
    DATA_CAPTURE_READ_WRITE = "DATA_CAPTURE_READ_WRITE"
    IOT_ENDPOINT_READ_WRITE = "IOT_ENDPOINT_READ_WRITE"
    USER_FULL_ACCESS = "USER_FULL_ACCESS"


class CaptureSortBy(str, Enum):
    DATE_CREATED = "DATE_CREATED"
    NAME = "NAME"
    STATE = "STATE"
    TYPE = "TYPE"


class CollaborativeMemberOrganizationState(str, Enum):
    APPROVED = "APPROVED"
    DENIED_ACCESS = "DENIED_ACCESS"
    HOST_ORGANIZATION = "HOST_ORGANIZATION"
    PENDING_APPROVAL = "PENDING_APPROVAL"


class CollaborativeMemberPermission(str, Enum):
    READ_ONLY = "READ_ONLY"
    READ_WRITE = "READ_WRITE"


class DataCaptureAssetAttributeSchemaType(str, Enum):
    boolean = "boolean"
    double = "double"
    integer = "integer"
    string = "string"


class DataCaptureAssetAttributeType(str, Enum):
    TELEMETRY = "TELEMETRY"


class DataCaptureAttachmentError(str, Enum):
    FILE_UPLOAD_INCOMPLETE = "FILE_UPLOAD_INCOMPLETE"


class DataCaptureAttachmentType(str, Enum):
    FILE = "FILE"


class DataCaptureDataExportState(str, Enum):
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_CREATED = "NOT_CREATED"


class DataCaptureDataExportType(str, Enum):
    ACTIVE_CAPTURE_EXPORT = "ACTIVE_CAPTURE_EXPORT"
    FULL_EXPORT = "FULL_EXPORT"


class DataCaptureDataModelState(str, Enum):
    ERROR = "ERROR"
    GOOD = "GOOD"


class DataCaptureRecordError(str, Enum):
    InvalidAttributeId = "InvalidAttributeId"
    InvalidTimestamp = "InvalidTimestamp"
    RecordExists = "RecordExists"
    Unknown = "Unknown"
    ValueTypeError = "ValueTypeError"


class DataCaptureState(str, Enum):
    CAPTURING = "CAPTURING"
    COMPLETE = "COMPLETE"
    COMPLETION_ERROR = "COMPLETION_ERROR"
    CONFIGURATION_ERROR = "CONFIGURATION_ERROR"
    DELETING = "DELETING"
    FINISHING = "FINISHING"
    READY = "READY"


class DataCaptureTimeConfigType(str, Enum):
    MANUAL = "MANUAL"
    SCHEDULED = "SCHEDULED"


class DataCaptureTimeConfigurationState(str, Enum):
    ERROR = "ERROR"
    GOOD = "GOOD"


class DataCaptureType(str, Enum):
    STANDARD = "STANDARD"


class DataStoreObjectType(str, Enum):
    DIRECTORY = "DIRECTORY"
    FILE = "FILE"


class DimensionValueType(str, Enum):
    VARCHAR = "VARCHAR"


class ExportFileFormat(str, Enum):
    CSV = "CSV"


class IotDataRecordErrorType(str, Enum):
    DUPLICATE_ENTRY = "DUPLICATE_ENTRY"
    INCORRECT_VALUE_TYPE = "INCORRECT_VALUE_TYPE"
    INVALID_TIMESTAMP = "INVALID_TIMESTAMP"
    MISSING_DATA = "MISSING_DATA"
    MISSING_TIME_UNIT = "MISSING_TIME_UNIT"
    UNEXPECTED_ATTRIBUTE = "UNEXPECTED_ATTRIBUTE"
    UNKNOWN = "UNKNOWN"


class MeasureValueType(str, Enum):
    BIGINT = "BIGINT"
    BOOLEAN = "BOOLEAN"
    DOUBLE = "DOUBLE"
    MULTI = "MULTI"
    TIMESTAMP = "TIMESTAMP"
    VARCHAR = "VARCHAR"


class MeasureValueTypeMULTI(str, Enum):
    MULTI = "MULTI"


class ModelAttributeType(str, Enum):
    Property = "Property"
    Telemetry = "Telemetry"


class ModelSchemaType(str, Enum):
    boolean = "boolean"
    dateTime = "dateTime"
    double = "double"
    duration = "duration"
    integer = "integer"
    string = "string"


class ServiceType(str, Enum):
    DATA_CAPTURE = "DATA_CAPTURE"
    DATA_STORE = "DATA_STORE"
    IOT_GROUP = "IOT_GROUP"
    OCS_ADAPTER = "OCS_ADAPTER"
    TIME_SERIES_DB = "TIME_SERIES_DB"


class TimeSeriesDbQueryType(str, Enum):
    LAST_X_ROWS = "LAST_X_ROWS"
    NEXT_TOKEN = "NEXT_TOKEN"
    TIME_PERIOD = "TIME_PERIOD"


class TimeSeriesQueryOutputFileType(str, Enum):
    CSV = "CSV"
    JSON = "JSON"


class TimeUnit(str, Enum):
    MICROSECONDS = "MICROSECONDS"
    MILLISECONDS = "MILLISECONDS"
    NANOSECONDS = "NANOSECONDS"
    SECONDS = "SECONDS"


class UserAccountState(str, Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    PENDING = "PENDING"


class UserRole(str, Enum):
    DATA_COMPLIANCE = "DATA_COMPLIANCE"
    DATA_CONSUMER = "DATA_CONSUMER"
    DATA_PROVIDER = "DATA_PROVIDER"
    PLATFORM_ADMIN = "PLATFORM_ADMIN"