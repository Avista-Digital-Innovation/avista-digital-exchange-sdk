# Avista Digital Exchange SDK

This package allows you to access the Avista Digital Exchange and perform a subset of its features programmatically. All that you need is a personal authentication token that can be generated at [energy.collaboratives.io](energy.collaboratives.io).

## Getting Started

1. Install the python package.

```
pip3 install avista-digital-exchange-sdk
```

2. Ensure you have the latest version.

```
pip3 install --upgrade avista-digital-exchange-sdk
```

3. Import the module in your python script.
4. Initialize the module with your authentication token.

```
from avista_digital_exchange_sdk import AvistaDigitalExchange

digitalExchange = AvistaDigitalExchange("{token}")

# Alternatively, instantiate with debug mode enabled
# digitalExchange = AvistaDigitalExchange("{token}", True)
```

---

## AvistaDigitalExchange Functions

### 1. getUserInfo

Retrieves your user information.

#### Parameters:

None

#### Return Type

[User](#user)

#### Example

```
user = digitalExchange.getUserInfo()
```

### 2. listDataStores

Lists the data stores you own.

#### Parameters:

None

#### Return Type

[[DataStore]](#datastore)

#### Example

```
dataStores = digitalExchange.listDataStores()
```

### 3. getDataStore

Gets the metadata of the data store.

#### Parameters:

```
dataStoreId :  str, required
    The id of the data store.
```

#### Return Type

[DataStore](#datastore)

#### Example

```
dataStore = digitalExchange.getDataStore("{dataStoreId}")
```

### 4. getDataStoreDirectory

Gets the directory metadata and contents.

#### Parameters:

```
dataStoreDirectoryId :  str, required
    The id of the directory.
```

#### Return Type

[DataStoreDirectory](#datastoredirectory)

#### Example

```
dir = digitalExchange.getDataStoreDirectory("{dataStoreDirectoryId}")
```

### 5. getDataStoreFileMeta

Gets the metadata of a file.

#### Parameters:

```
dataStoreFileId :  str, required
    The id of the file.
```

#### Return Type

[DataStoreFile](#datastorefile)

#### Example

```
file = digitalExchange.getDataStoreFileMeta("{dataStoreFileId}")
```

### 6. downloadDataStoreFile

Downloads a copy of the file to the local file system.

#### Parameters:

```
dataStoreFileId :  str, required
    The id of the file.
writeLocation :  str, required
    Path where the file should be written. If writeLocation is a directory, the filename will be its original name.
```

#### Return Type

[DataStoreFile](#datastorefile)

#### Example

```
file = digitalExchange.downloadDataStoreFile("{dataStoreFileId}", "{writeLocation}")
```

### 7. uploadFileToDataStore

Uploads a local file to a data store.

#### Parameters:

```
dataStoreId :  str, required
    The id of the data store you are writing to.
dataStoreDirectoryId :  str, required
    The id of the directory to place the file in.
localPath :  str, required
    The path of the file to be uploaded.
name :  str, optional
    A name for the file if naming different than the local file name.
description :  str, optional
    A description of the file.
```

#### Return Type

[DataStoreFile](#datastorefile)

#### Example

```
file = digitalExchange.uploadFileToDataStore("{dataStoreId}", "{dataStoreDirectoryId}", "./testFile.txt")
```

### 8. deleteDataStoreFile

Removes a file from the data store and deletes it from the Digital Exchange.

#### Parameters:

```
dataStoreFileId :  str, required
    The id of the file to delete.
```

#### Return Type

[DataStoreFile](#datastorefile)

#### Example

```
file = digitalExchange.deleteDataStoreFile("{dataStoreFileId}")
```

### 9. listTimeSeriesDatabases

Lists the databases you own.

#### Parameters:

None

#### Return Type

[[TimeSeriesDb]](#timeseriesdb)

#### Example

```
databases = digitalExchange.listTimeSeriesDatabases()
```

### 10. getTimeSeriesDatabase

Gets the metadata of the database.

#### Parameters:

```
timeSeriesDbId :  str, required
    The id of the database.
```

#### Return Type

[TimeSeriesDb](#timeseriesdb)

#### Example

```
database = digitalExchange.getTimeSeriesDatabase("{timeSeriesDbId}")
```

### 11. queryTimeSeriesDatabase

Queries the time series data using [SQL and AWS Timestream features](https://docs.aws.amazon.com/timestream/latest/developerguide/reference.html).

The result will be paginated if large enough. For the first request, omit the nextToken and clientToken parameters or set them to None. If a NextToken is present in the query result, there is more data to retrieve. In subsequent requests use the original queryString and maxRows parameters, and the nextToken and clientToken from the previous query result.

Input variables begin with lowercase letters for Digital Exchange API consistency but result variables from AWS Timestream will have capitalized variable names.

#### Parameters:

```
timeSeriesDbId :  str, required
    The id of the database.
queryString :  str, required
    The query to be run.
    The database table must be referenced as "{databaseName}"."{tableName}" (ex. 'SELECT...FROM "{databaseName}"."{tableName}"'). The databaseName and tableName can be found in the TimeSeriesDb object.
maxRows :  str, optional
    The maximum number of data rows to include in the query result.
nextToken :  str, optional
    A token that will retrieve the next set of data in a paginated result.
clientToken :  str, optional
    A unique token for a query from this device. The token will change for each query. Omit this parameter on the first request.
```

#### Return Type

[QueryResult_TimestreamVariables](#queryresult_timestreamvariables)

#### Example

```
result = digitalExchange.queryTimeSeriesDatabase("{timeSeriesDbId}", "{queryString}", 100, "{nextToken}", "{clientToken}")
clientToken = result.clientToken
nextToken = result.NextToken
```

### 12. createTimeSeriesMeasureValue

Creates a MeasureValue object to be used as an entry for a time series record.

Reference [AWS Timestream MeasureValue](https://docs.aws.amazon.com/timestream/latest/developerguide/API_MeasureValue.html)

#### Parameters:

```
Type :  str, required
    The type of the the measure value. Valid values: "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP"
Name :  str, required
    The name of the measure.
Value :  str, required
    The measure value as a string.
```

#### Return Type

[TimeSeriesMeasureValue](#timeseriesmeasurevalue)

#### Example

```
measure = digitalExchange.createTimeSeriesMeasureValue("{type}", "{name}", "{value}")
```

### 13. createTimeSeriesDimension

Creates a Dimension object to be used in a record. Each Dimension is essentially a metadata attribute for a record.

Reference [AWS Timestream Dimension](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Dimension.html)

#### Parameters:

```
DimensionValueType :  str, required
    The type of the attribute. Valid values: "VARCHAR"
Name :  str, required
    The name of the attribute.
Value :  str, required
    The attribute value.
```

#### Return Type

[TimeSeriesDimension](#timeseriesdimension)

#### Example

```
dimension = digitalExchange.createTimeSeriesDimension("VARCHAR", "{name}", "{value}")
```

### 14. createTimeSeriesInputRecord

Creates a time series data point record.

Reference (AWS Timestream Record)(https://docs.aws.amazon.com/timestream/latest/developerguide/API_Record.html)

#### Parameters:

```
Time :  str, required
    The timestamp for the record.
TimeUnit :  str, required
    The unit of the Time timestamp. Valid values: "MILLISECONDS", "SECONDS", "MICROSECONDS", "NANOSECONDS"
MeasureName :  str, required
    The name of the measure.
MeasureValueType :  str, required
    The type of the measure. Valid values: "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP", "MULTI". "MULTI" is used to include an array of MeasureValues for the single time point. If type is "MULTI" include an array of MeasureValues for the MeasureValues parameter. Otherwise, pass a single value for MeasureValue.
MeasureValue :  str, optional
    The measure value as a string.
MeasureValues : [TimeSeriesMeasureValue], optional
    An array of MeasureValues.
Dimensions : [TimeSeriesDimension], optional
    The dimensions, or metadata, of the record. Include a Dimension with name "name" and a value of the asset's name so it can be viewed on the Avista Digital Exchange web platform.
Version : int, optional
    The version of the record. Record data can be updated by publishing it again with an incremented Version number. Defaults to 1.
```

#### Return Type

[TimeSeriesInputRecord](#timeseriesinputrecord)

#### Example

```
# Initialize Dimensions
dimensions = []
dimensions.append(digitalExchange.createTimeSeriesDimension('VARCHAR', 'name', 'Asset 1'))
dimensions.append(digitalExchange.createTimeSeriesDimension('VARCHAR', 'Dimension2Name', 'Dimension2Value'))

# Initialize MeasureValues
measureValues = []
measureValues.append(digitalExchange.createTimeSeriesMeasureValue('VARCHAR', 'Measure 1', 'a string...' ))
measureValues.append(digitalExchange.createTimeSeriesMeasureValue('BIGINT', 'Measure 2', '321' ))

# Initialize Record
record = digitalExchange.createTimeSeriesInputRecord('1662155084', 'SECONDS', 'multi-measure-entry-name', 'MULTI', None, measureValues, dimensions, 1)
```

### 15. publishToTimeSeriesDatabase

Publishes data records to the database.

You may only publish records for 1 asset per request. To support viewing on data on the web, include a Dimension entry with DimensionName 'name' and DimensionValue containing the name of the asset.

#### Parameters:

```
timeSeriesDbId :  str, required
    The id of the database you are publishing to.
assetId :  str, required
    The id of the asset you are publishing data for.
records : [TimeSeriesInputRecord], required
    An array of data records to write to the database.
```

#### Return Type

[[TimeSeriesAssetData]](#timeseriesassetdata)

#### Example

```
# Initialize Dimensions
dimensions = []
dimensions.append(digitalExchange.createTimeSeriesDimension('VARCHAR', 'name', 'Asset 1 Name'))
dimensions.append(digitalExchange.createTimeSeriesDimension('VARCHAR', 'Dimension2Name', 'Dimension2Value'))

# Initialize MeasureValues
measureValues = []
measureValues.append(digitalExchange.createTimeSeriesMeasureValue('VARCHAR', 'Measure 1', 'a string...' ))
measureValues.append(digitalExchange.createTimeSeriesMeasureValue('BIGINT', 'Measure 2', '321' ))

# Initialize Records
records = []
records.append(digitalExchange.createTimeSeriesInputRecord('1662155081', 'SECONDS', 'multi-measure-entry-name', 'MULTI', None, measureValues, dimensions, 1))

# Use other MeasureValues for another record
measureValues = []
...
records.append(digitalExchange.createTimeSeriesInputRecord('1662155082', 'SECONDS', 'multi-measure-entry-name', 'MULTI', None, measureValues, dimensions, 1))

# Write the records to the database
result = digitalExchange.publishToTimeSeriesDatabase('{}', 'asset1', records)
```

### 16. listCollaboratives

Lists the collaboratives you are a member of.

#### Parameters:

None

#### Return Type

[[Collaborative]](#collaborative)

#### Example

```
collaboratives = digitalExchange.listCollaboratives()
```

### 17. getCollaborative

Gets the metadata of the collaborative.

#### Parameters:

```
collaborativeId :  str, required
    The id of the collaborative.
```

#### Return Type

[Collaborative](#collaborative)

#### Example

```
collaborative = digitalExchange.getCollaborative("{collaborativeId}")
```

### 18. listCollaborativeServices

Lists all services (Data Stores of Time Series Databases) shared in the collaborative.

#### Parameters:

```
collaborativeId :  str, required
    The id of the collaborative.
```

#### Return Type

[[Service]](#service)

#### Example

```
services = digitalExchange.listCollaborativeServices("{collaborativeId}")
```

### 19. listCollaborativesServiceSharedWith

Gets the collaboratives that a service is shared with. You must be the owner of the service.

#### Parameters:

```
serviceId :  str, required
    The id of the service (either a dataStoreId or timeSeriesDbId).
```

#### Return Type

[[Collaborative]](#collaborative)

#### Example

```
collaboratives = digitalExchange.listCollaborativesServiceSharedWith("{serviceId}")
```

### 20. addServiceToCollaborative

Shares a service (Data Store or Time Series database) with a collaborative.

#### Parameters:

```
serviceId :  str, required
    The id of the service (either dataStoreId or timeSeriesDbId).
collaborativeId :  str, required
    The id of the collaborative to share the service with.
```

#### Return Type

[Service](#service)

#### Example

```
service = digitalExchange.addServiceToCollaborative("{serviceId}", "{collaborativeId}")
```

### 21. removeServiceFromCollaborative

Removes the service from a collaborative.

#### Parameters:

```
serviceId :  str, required
    The id of the service (either dataStoreId or timeSeriesDbId).
collaborativeId :  str, required
    The id of the collaborative to remove the service from.
```

#### Return Type

[Service](#service)

#### Example

```
service = digitalExchange.removeServiceFromCollaborative("{serviceId}", "{collaborativeId}")
```

---

## Types

### User

Stores basic information about a Digital Exchange user.

#### Properties

```
userId : str
    The user's unique id number.
firstName : str
lastName : str
organization : Organization
    The organization that the user is a member of.
```

### Organization

Stores basic information about a Digital Exchange member organization.

#### Properties

```
name : str
organizationId : str
```

### Service

Represents a Digital Exchange service such as Data Stores or Time Series Databases.

#### Properties

```
serviceType : str
    Valid values are "DATA_STORE", "TIME_SERIES_DB"
serviceId : str
    Either the dataStoreId or the timeSeriesDbId of the service.
dataStore : DataStore | None
    Reference to the Data Store Service object.
timeSeriesDb : TimeSeriesDb | None
    Reference to the Time Series Database Service object.
```

### DataStore

A Data Store Service object.

#### Properties

```
dataStoreId: str
name: str
description: str
ownerUserId: str
homeDirectoryId: str
    The dataStoreDirectoryId of the Data Store's home directory
```

### DataStoreDirectory

A directory in a Data Store file storage hierarchy.

#### Properties

```
dataStoreDirectoryId: str
dataStoreId: str
    The Data Store this directory belongs to.
name: str
    The name of the directory.
homeDirectory: Boolean
    Indicator of whether this directory is the home directory or a subdirectory.
parentDirectoryId: str
    The directory this directory is found within.
directories: [DataStoreDirectory]
    This directory's contents - directories.
files: [DataStoreFile]
    This directory's contents - files.
```

### DataStoreFile

A file belonging to a Data Store.

#### Properties

```
dataStoreFileId: str
dataStoreId: str
    The Data Store this file belongs to.
dataStoreDirectoryId: str
    The directory that the file belongs to.
name: str
    The filename without the file extension.
description: str
fileExtension: str
storageSizeBytes: int
lastModified: str
contentType: str
```

### TimeSeriesDb

A time series database service object.

#### Properties

```
timeSeriesDbId: str
name: str
description: str
ownerUserId: str
databaseName: str
    The name of the database the table is found in. Used in time series queries.
tableName: str
    The name of the database table. Used in time series queries.
```

### QueryResult_TimestreamVariables

A time series query result that includes the AWS Timestream result object.

#### Properties

```
timestreamResults: dict :
    The AWS Timestream query result object. [Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_Query.html). Some properties are stored within the QueryResult object for easy access.
clientToken: str
    The token generated in the cloud associating the query to the requesting user device.
NextToken: str | None
    Present if the query result is paginated.
QueryId: str
QueryStatus: dict
Rows: dict
ColumnInfo: dict
```

### TimeSeriesMeasureValue

A measure and its data value. [Timestream Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_MeasureValue.html)

#### Properties

```
Type: str
Name: str
Value: str
```

### TimeSeriesDimension

A dimension (or a metadata entry). [Timestream Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Dimension.html)

#### Properties

```
DimensionValueType: str
Name: str
Value: str
```

### TimeSeriesInputRecord

A time series record. [Timestream Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Record.html)

#### Properties

```
Time :  str
    The timestamp for the record.
TimeUnit :  str
    The unit of the Time timestamp. Valid values: "MILLISECONDS", "SECONDS", "MICROSECONDS", "NANOSECONDS"
MeasureName :  str
    The name of the measure.
MeasureValueType :  str
    The type of the measure. Valid values: "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP", "MULTI". "MULTI" is used to include an array of MeasureValues for the single time point. If type is "MULTI" include an array of MeasureValues for the MeasureValues parameter. Otherwise, pass a single value for MeasureValue.
MeasureValue :  str
    The measure value. Only present if MeasureValueType != "MULTI"
MeasureValues : [TimeSeriesMeasureValue]
    An array of MeasureValues. Only present if MeasureValueType == "MULTI"
Dimensions : [TimeSeriesDimension]
    The dimensions, or metadata, of the record.
Version : int
    The version of the record.
```

### Collaborative

A Digital Exchange data Collaborative.

#### Properties

```
collaborativeId : str
name : str
description : str
hostOrganizationId : str
    Id of the organization the collaborative belongs to.
memberOrganizations : [CollaborativeMemberOrganization]
    Members of the collaborative, organized by organization.
```

### CollaborativeMemberOrganization

An organization and its membership details for a collaborative.

#### Properties

```
organization : Organization
collaborativeId : str
memberState : str
usersInCollaborative : CollaborativeMemberUser
    The users within the organization that are members of the collaborative.
```

### CollaborativeMemberUser

A user and its membership details for a collaborative.

#### Properties

```
permission : str
    The user's permission level within the collaborative. Valid values: "READ_ONLY" or "READ_WRITE"
user : user
```

### TimeSeriesAssetData

An additional format for Time Series Database data, in a more human readable format.

#### Properties

```
assetId: str
name: str
attributes: [TimeSeriesAssetAttribute]
```

### TimeSeriesAssetAttribute

One attribute of an asset and some of its data.

#### Properties

```
attributeType: one of "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP", "MULTI"
lastValue: str
lastValueTime: str
name: str
data: [TimeSeriesAssetAttributeData]
```

### TimeSeriesAssetAttributeData

A single time/value data point for an attribute.

#### Properties

```
timestamp: str
    The time in ISO8601 format.
value: str
    The attribute value at this timestamp.
```
