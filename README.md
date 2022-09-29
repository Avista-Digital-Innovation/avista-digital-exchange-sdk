# Avista Digital Exchange SDK

This package allows you to access the Avista Digital Exchange and perform a subset of its features programmatically. All that you need is a personal authentication token that can be generated at [energy.collaboratives.io](https://energy.collaboratives.io).

[PyPi listing](https://pypi.org/project/avista-digital-exchange-sdk/)

[GitHub Repository](https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk)

## Table of Contents

- [Avista Digital Exchange SDK](#avista-digital-exchange-sdk)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [AvistaDigitalExchange Functions](#avistadigitalexchange-functions)
    - [getUserInfo](#getuserinfo)
    - [listDataStores](#listdatastores)
    - [getDataStore](#getdatastore)
    - [getDataStoreDirectory](#getdatastoredirectory)
    - [getDataStoreFileMeta](#getdatastorefilemeta)
    - [downloadDataStoreFile](#downloaddatastorefile)
    - [uploadFileToDataStore](#uploadfiletodatastore)
    - [deleteDataStoreFile](#deletedatastorefile)
    - [listTimeSeriesDatabases](#listtimeseriesdatabases)
    - [getTimeSeriesDatabase](#gettimeseriesdatabase)
    - [listTimeSeriesAssetsAndLatestValues](#listtimeseriesassetsandlatestvalues)
    - [queryTimeSeriesDatabaseWithFilters](#querytimeseriesdatabasewithfilters)
    - [queryTimeSeriesDatabase_TimestreamFormat](#querytimeseriesdatabase_timestreamformat)
    - [createTimeSeriesMeasureValue](#createtimeseriesmeasurevalue)
    - [createTimeSeriesDimension](#createtimeseriesdimension)
    - [createTimeSeriesInputRecord](#createtimeseriesinputrecord)
    - [publishToTimeSeriesDatabase](#publishtotimeseriesdatabase)
    - [listCollaboratives](#listcollaboratives)
    - [getCollaborative](#getcollaborative)
    - [listCollaborativeServices](#listcollaborativeservices)
    - [listCollaborativesServiceSharedWith](#listcollaborativesservicesharedwith)
    - [addServiceToCollaborative](#addservicetocollaborative)
    - [removeServiceFromCollaborative](#removeservicefromcollaborative)
  - [Types](#types)
    - [User](#user)
      - [Properties](#properties)
    - [Organization](#organization)
      - [Properties](#properties-1)
    - [Service](#service)
      - [Properties](#properties-2)
    - [DataStore](#datastore)
      - [Properties](#properties-3)
    - [DataStoreDirectory](#datastoredirectory)
      - [Properties](#properties-4)
      - [Methods](#methods)
        - [printContents](#printcontents)
    - [DataStoreFile](#datastorefile)
      - [Properties](#properties-5)
    - [TimeSeriesDb](#timeseriesdb)
      - [Properties](#properties-6)
    - [QueryResult_TimestreamVariables](#queryresult_timestreamvariables)
      - [Properties](#properties-7)
    - [TimeSeriesMeasureValue](#timeseriesmeasurevalue)
      - [Properties](#properties-8)
    - [TimeSeriesDimension](#timeseriesdimension)
      - [Properties](#properties-9)
    - [TimeSeriesInputRecord](#timeseriesinputrecord)
      - [Properties](#properties-10)
    - [TimeSeriesAssetData](#timeseriesassetdata)
      - [Properties](#properties-11)
    - [TimeSeriesAssetAttribute](#timeseriesassetattribute)
      - [Properties](#properties-12)
    - [TimeSeriesAssetAttributeData](#timeseriesassetattributedata)
      - [Properties](#properties-13)
    - [Collaborative](#collaborative)
      - [Properties](#properties-14)
    - [CollaborativeMemberOrganization](#collaborativememberorganization)
      - [Properties](#properties-15)
    - [CollaborativeMemberUser](#collaborativememberuser)
      - [Properties](#properties-16)
  - [Development](#development)
  - [Deployment](#deployment)
  - [Resources](#resources)

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

### getUserInfo

Retrieves your user information.

**Parameters**

None

**Return Type**

[User](#user)

**Example**

```
user = digitalExchange.getUserInfo()
```

---

### listDataStores

Lists the data stores you own.

**Parameters**

None

**Return Type**

[[DataStore]](#datastore)

**Example**

```
dataStores = digitalExchange.listDataStores()
```

### getDataStore

Gets the metadata of the data store.

**Parameters**

```
dataStoreId :  str, required
    The id of the data store.
```

**Return Type**

[DataStore](#datastore)

**Example**

```
dataStore = digitalExchange.getDataStore("{dataStoreId}")
```

### getDataStoreDirectory

Gets the directory metadata and contents.

**Parameters**

```
dataStoreDirectoryId :  str, required
    The id of the directory.
```

**Return Type**

[DataStoreDirectory](#datastoredirectory)

**Example**

```
dir = digitalExchange.getDataStoreDirectory("{dataStoreDirectoryId}")
```

### getDataStoreFileMeta

Gets the metadata of a file.

**Parameters**

```
dataStoreFileId :  str, required
    The id of the file.
```

**Return Type**

[DataStoreFile](#datastorefile)

**Example**

```
file = digitalExchange.getDataStoreFileMeta("{dataStoreFileId}")
```

### downloadDataStoreFile

Downloads a copy of the file to the local file system.

**Parameters**

```
dataStoreFileId :  str, required
    The id of the file.
writeLocation :  str, required
    Path where the file should be written. If writeLocation is a directory, the filename will be its original name.
```

**Return Type**

[DataStoreFile](#datastorefile)

**Example**

```
file = digitalExchange.downloadDataStoreFile("{dataStoreFileId}", "{writeLocation}")
```

### uploadFileToDataStore

Uploads a local file to a data store.

**Parameters**

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

**Return Type**

[DataStoreFile](#datastorefile)

**Example**

```
file = digitalExchange.uploadFileToDataStore("{dataStoreId}", "{dataStoreDirectoryId}", "./testFile.txt")
```

### deleteDataStoreFile

Removes a file from the data store and deletes it from the Digital Exchange.

**Parameters**

```
dataStoreFileId :  str, required
    The id of the file to delete.
```

**Return Type**

[DataStoreFile](#datastorefile)

**Example**

```
file = digitalExchange.deleteDataStoreFile("{dataStoreFileId}")
```

### listTimeSeriesDatabases

Lists the databases you own.

**Parameters**

None

**Return Type**

[[TimeSeriesDb]](#timeseriesdb)

**Example**

```
databases = digitalExchange.listTimeSeriesDatabases()
```

### getTimeSeriesDatabase

Gets the metadata of the database.

**Parameters**

```
timeSeriesDbId :  str, required
    The id of the database.
```

**Return Type**

[TimeSeriesDb](#timeseriesdb)

**Example**

```
database = digitalExchange.getTimeSeriesDatabase("{timeSeriesDbId}")
```

### listTimeSeriesAssetsAndLatestValues

Queries the time series database to collect a list of all assets and their attributes in the database, as well as the latest value and timestamp for each attribute.

**Parameters**

```
timeSeriesDbId :  str, required
    The id of the database.
resultFileWriteLocation :  str, optional
    If you would like the results stored in a file, include a name or path here. 
    Results will be in JSON format.
```

**Return Type**

[[TimeSeriesAssetData](#timeseriesassetdata)]

**Example**

```
result = digitalExchange.listTimeSeriesAssetsAndLatestValues(
     "<timeSeriesDbId>", None)

# Example iteration through assets and attributes in the result
for asset in result:
    assetId = asset.assetId
    for attribute in asset.attributes:
        name = attribute.name
        latestValue = attribute.lastValue
        timestamp = attribute.lastValueTime
```

### queryTimeSeriesDatabaseWithFilters

Queries the time series data using asset, attribute and time filters, and writes the results to a file.

You must provide a time range and the assets (and their attributes) that you wish to query. The method automatically 
iterates over all pagination tokens so the result will be compiled upon completion. When the compiled result is available, it will be written to the local file system.

**Parameters**

```
timeSeriesDbId :  str, required
    The id of the database.
startTime :  ISO8601 str, required
    The beginning of the time interval to query.
    Example: "2022-09-27T10:22:45.000Z"
endTime: ISO8601 str, required
    The end of the time interval to query.
    Example: "2022-09-27T10:22:45.000Z"
assetAndAttributesFilter: [{"assetId": <str>, "attributeNamesFilter": [<str>]}], required
resultFileWriteLocation: str, required
    The location to store the result file on the local file system. If a directory is provided but not a file name, the file will be saved as "result.csv" or "result.json" in the specified directory.
exportFileFormat: str, optional
    The file format in which to compile the query result. If JSON is used, the data will be stored as an array of TimeSeriesAssetData objects (see Data Types section below).
    Valid values: "CSV" | "JSON"
    Defaults to "CSV"
```

**Return Type**

Bool

**Example**

```
result = digitalExchange.queryTimeSeriesDatabaseWithFilters(
     "<timeSeriesDbId>", [
         {"assetId": "<assetId>",
             "attributeNamesFilter": ["SOC", "V", "V - Setpoint"]},
         {"assetId": "<assetId>",
             "attributeNamesFilter": ["A kW", "B Amps", "B PF"]},
         {"assetId": "<assetId>", 
             "attributeNamesFilter": ["A kVAR", "A kW", "B Amps"]}], 
    "2022-09-25T20:13:04.465Z", 
    "2022-09-26T20:58:04.465Z", 
    "./", 
    "JSON")
```

### queryTimeSeriesDatabase_TimestreamFormat

Queries the time series data using [SQL and AWS Timestream features](https://docs.aws.amazon.com/timestream/latest/developerguide/reference.html).

The result will be paginated if large enough. For the first request, omit the nextToken and clientToken parameters or set them to None. If a nextToken is present in the query result, there is more data to retrieve. In subsequent requests use the original queryString and maxRows parameters, and the nextToken and clientToken from the previous query result.

This SDK uses lowercase first letter variable names and AWS Timestream documented variables are capitalized.

**Parameters**

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

**Return Type**

[QueryResult_TimestreamVariables](#queryresult_timestreamvariables)

**Example**

```
db = digitalExchange.getTimeSeriesDatabase("{timeSeriesDbId}")
databaseName = db.databaseName
tableName = db.tableName

queryString = 'SELECT.....FROM "{databaseName}"."{tableName}" WHERE.....'

result = digitalExchange.queryTimeSeriesDatabase_TimestreamFormat("{timeSeriesDbId}", "{queryString}", 100, "{nextToken}", "{clientToken}")
clientToken = result.clientToken
nextToken = result.nextToken
```

### createTimeSeriesMeasureValue

Creates a measureValue object to be used as an entry for a time series record.

Reference [AWS Timestream MeasureValue](https://docs.aws.amazon.com/timestream/latest/developerguide/API_MeasureValue.html)

**Parameters**

```
type :  str, required
    The type of the the measure value. Valid values: "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP"
name :  str, required
    The name of the measure.
value :  str, required
    The measure value as a string.
```

**Return Type**

[TimeSeriesMeasureValue](#timeseriesmeasurevalue)

**Example**

```
measure = digitalExchange.createTimeSeriesMeasureValue("{type}", "{name}", "{value}")
```

### createTimeSeriesDimension

Creates a Dimension object to be used in a record. Each Dimension is essentially a metadata attribute for a record.

Reference [AWS Timestream Dimension](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Dimension.html)

**Parameters**

```
dimensionValueType :  str, required
    The type of the attribute. Valid values: "VARCHAR"
name :  str, required
    The name of the attribute.
value :  str, required
    The attribute value.
```

**Return Type**

[TimeSeriesDimension](#timeseriesdimension)

**Example**

```
dimension = digitalExchange.createTimeSeriesDimension("VARCHAR", "{name}", "{value}")
```

### createTimeSeriesInputRecord

Creates a time series data point record.

Reference (AWS Timestream Record)(https://docs.aws.amazon.com/timestream/latest/developerguide/API_Record.html)

**Parameters**

```
time :  str, required
    The timestamp for the record.
timeUnit :  str, required
    The unit of the Time timestamp. Valid values: "MILLISECONDS", "SECONDS", "MICROSECONDS", "NANOSECONDS"
measureName :  str, required
    The name of the measure.
measureValueType :  str, required
    The type of the measure. Valid values: "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP", "MULTI". "MULTI" is used to include an array of measureValues for the single time point. If type is "MULTI" include an array of measureValues for the measureValues parameter. Otherwise, pass a single value for measureValue.
measureValue :  str, optional
    The measure value as a string.
measureValues : [TimeSeriesMeasureValue], optional
    An array of measureValues.
dimensions : [TimeSeriesDimension], optional
    The dimensions, or metadata, of the record. Include a Dimension with name "name" and a value of the asset's name so it can be viewed on the Avista Digital Exchange web platform.
version : int, optional
    The version of the record. Record data can be updated by publishing it again with an incremented version number. Defaults to 1.
```

**Return Type**

[TimeSeriesInputRecord](#timeseriesinputrecord)

**Example**

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

### publishToTimeSeriesDatabase

Publishes data records to the database.

You may only publish records for 1 asset per request. To support viewing on data on the web, include a dimension entry with dimensionName 'name' and dimensionValue containing the name of the asset.

**Parameters**

```
timeSeriesDbId :  str, required
    The id of the database you are publishing to.
assetId :  str, required
    The id of the asset you are publishing data for.
records : [TimeSeriesInputRecord], required
    An array of data records to write to the database.
```

**Return Type**

[[TimeSeriesAssetData]](#timeseriesassetdata)

**Example**

```
# Initialize dimensions
dimensions = []
dimensions.append(digitalExchange.createTimeSeriesDimension('VARCHAR', 'name', 'Asset 1 Name'))
dimensions.append(digitalExchange.createTimeSeriesDimension('VARCHAR', 'Dimension2Name', 'Dimension2Value'))

# Initialize measureValues
measureValues = []
measureValues.append(digitalExchange.createTimeSeriesMeasureValue('VARCHAR', 'Measure 1', 'a string...' ))
measureValues.append(digitalExchange.createTimeSeriesMeasureValue('BIGINT', 'Measure 2', '321' ))

# Initialize records
records = []
records.append(digitalExchange.createTimeSeriesInputRecord('1662155081', 'SECONDS', 'multi-measure-entry-name', 'MULTI', None, measureValues, dimensions, 1))

# Use other measureValues for another record
measureValues = []
...
records.append(digitalExchange.createTimeSeriesInputRecord('1662155082', 'SECONDS', 'multi-measure-entry-name', 'MULTI', None, measureValues, dimensions, 1))

# Write the records to the database
result = digitalExchange.publishToTimeSeriesDatabase('{}', 'asset1', records)
```

### listCollaboratives

Lists the collaboratives you are a member of.

**Parameters**

None

**Return Type**

[[Collaborative]](#collaborative)

**Example**

```
collaboratives = digitalExchange.listCollaboratives()
```

### getCollaborative

Gets the metadata of the collaborative.

**Parameters**

```
collaborativeId :  str, required
    The id of the collaborative.
```

**Return Type**

[Collaborative](#collaborative)

**Example**

```
collaborative = digitalExchange.getCollaborative("{collaborativeId}")
```

### listCollaborativeServices

Lists all services (Data Stores of Time Series Databases) shared in the collaborative.

**Parameters**

```
collaborativeId :  str, required
    The id of the collaborative.
```

**Return Type**

[[Service]](#service)

**Example**

```
services = digitalExchange.listCollaborativeServices("{collaborativeId}")
```

### listCollaborativesServiceSharedWith

Gets the collaboratives that a service is shared with. You must be the owner of the service.

**Parameters**

```
serviceId :  str, required
    The id of the service (either a dataStoreId or timeSeriesDbId).
```

**Return Type**

[[Collaborative]](#collaborative)

**Example**

```
collaboratives = digitalExchange.listCollaborativesServiceSharedWith("{serviceId}")
```

### addServiceToCollaborative

Shares a service (Data Store or Time Series database) with a collaborative.

**Parameters**

```
serviceId :  str, required
    The id of the service (either dataStoreId or timeSeriesDbId).
collaborativeId :  str, required
    The id of the collaborative to share the service with.
```

**Return Type**

[Service](#service)

**Example**

```
service = digitalExchange.addServiceToCollaborative("{serviceId}", "{collaborativeId}")
```

### removeServiceFromCollaborative

Removes the service from a collaborative.

**Parameters**

```
serviceId :  str, required
    The id of the service (either dataStoreId or timeSeriesDbId).
collaborativeId :  str, required
    The id of the collaborative to remove the service from.
```

**Return Type**

[Service](#service)

**Example**

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

#### Methods

##### printContents

Lists all of the directory contents (directories and files), along with their ids.

**Parameters**

None

**Example**

```
dir = digitalExchange.getDataStoreDirectory("{dataStoreDirectoryId}")
dir.printContents()
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
nextToken: str | None
    Present if the query result is paginated.
queryId: str
queryStatus: dict
rows: dict
columnInfo: dict
```

### TimeSeriesMeasureValue

A measure and its data value. [Timestream Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_MeasureValue.html)

#### Properties

```
rype: str
name: str
value: str
```

### TimeSeriesDimension

A dimension (or a metadata entry). [Timestream Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Dimension.html)

#### Properties

```
dimensionValueType: str
name: str
value: str
```

### TimeSeriesInputRecord

A time series record. [Timestream Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Record.html)

#### Properties

```
time :  str
    The timestamp for the record.
timeUnit :  str
    The unit of the Time timestamp. Valid values: "MILLISECONDS", "SECONDS", "MICROSECONDS", "NANOSECONDS"
measureName :  str
    The name of the measure.
measureValueType :  str
    The type of the measure. Valid values: "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP", "MULTI". "MULTI" is used to include an array of measureValues for the single time point. If type is "MULTI" include an array of measureValues for the measureValues parameter. Otherwise, pass a single value for measureValue.
measureValue :  str
    The measure value. Only present if measureValueType != "MULTI"
measureValues : [TimeSeriesMeasureValue]
    An array of measureValues. Only present if measureValueType == "MULTI"
dimensions : [TimeSeriesDimension]
    The dimensions, or metadata, of the record.
version : int
    The version of the record.
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

## Development

If necessary, clone the repository with command `git clone https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk.git`.

Use VS Code with the Python extension to utilize formatting and type-ahead.

Deployment related code is in the root directory and the package code is found in `src/avista_digital_exchange_sdk`.

## Deployment

Follow the steps below to build and push the new package version to PyPi. [(Python packaging reference used)](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

**Steps**

1. Update `CHANGELOG.md` with new release notes.
2. Update `README.md` if necessary.
3. PyPi deployment
   1. Update the package version in `pyproject.toml`. Follow [this versioning method](https://py-pkgs.org/07-releasing-versioning.html#version-numbering)
   2. From the root directory of the repository:
      1. Run `python3 -m build`
      2. Run `python3 -m twine upload dist/* ` to upload the new build to PyPi.
         1. Use username `__token__`
         2. Use your [PyPi authentication token](https://pypi.org/help/#apitoken) as the password. 
   3. Test that the new version is available in pip by running `pip3 install --upgrade avista-digital-exchange-sdk`.
4. Push changes to git.
5. Merge changes to `main`.
6. Create a release branch from main with the name `release/YYYY_MM_DD_vXX.XX.XX` where XX.XX.XX is the new version number, and YYYY_MM_DD is the date the version was deployed.

## Resources

1. [Avista Digital Exchange](https://energy.collaboratives.io/)
2. [PyPi SDK project listing](https://pypi.org/project/avista-digital-exchange-sdk/)
3. [GitHub project repository](https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk)
4. [Python package deployment tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
5. [PyPi API Token](https://pypi.org/help/#apitoken)