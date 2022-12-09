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
    - [dataStore](#datastore)
      - [listDataStores](#listdatastores)
      - [getDataStore](#getdatastore)
      - [getDataStoreDirectory](#getdatastoredirectory)
      - [getDataStoreFileMeta](#getdatastorefilemeta)
      - [downloadDataStoreFile](#downloaddatastorefile)
      - [uploadFileToDataStore](#uploadfiletodatastore)
      - [deleteDataStoreFile](#deletedatastorefile)
    - [iot](#iot)
      - [getEndpoint](#getendpoint)
      - [listEndpointLastValues](#listendpointlastvalues)
      - [queryByTimeRange](#querybytimerange)
      - [publish](#publish)
      - [updateEndpointProperties](#updateendpointproperties)
  - [Types](#types)
    - [User](#user)
      - [Properties](#properties)
    - [Organization](#organization)
      - [Properties](#properties-1)
    - [DataStore](#datastore-1)
      - [Properties](#properties-2)
      - [Methods](#methods)
        - [cd](#cd)
        - [ls](#ls)
        - [pwd](#pwd)
        - [uploadFile](#uploadfile)
        - [downloadFile](#downloadfile)
        - [deleteFile](#deletefile)
    - [DataStoreDirectory](#datastoredirectory)
      - [Properties](#properties-3)
      - [Methods](#methods-1)
        - [printContents](#printcontents)
    - [DataStoreFile](#datastorefile)
      - [Properties](#properties-4)
    - [IotEndpoint](#iotendpoint)
      - [Properties](#properties-5)
    - [EndpointProperty](#endpointproperty)
      - [Properties](#properties-6)
    - [EndpointTelemetry](#endpointtelemetry)
      - [Properties](#properties-7)
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
4. Initialize the module with your authentication token.  The authentication token can be a user authentication token, or an iot endpoint authentication token.  If an endpoint token is used, only iot operations can be performed.

```
from avista_digital_exchange_sdk import AvistaDigitalExchange

digitalExchange = AvistaDigitalExchange("tokenvalue")

# Alternatively, instantiate with debug mode enabled
# digitalExchange = AvistaDigitalExchange("tokenvalue", True)
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

### dataStore

#### listDataStores

Lists the data stores you own.

**Parameters**

None

**Return Type**

[[DataStore]](#datastore)

**Example**

```
dataStores = digitalExchange.dataStores.listDataStores()
```

#### getDataStore

Gets a data store object. The object can be interacted with as a command line utility to navigate the data store. See [DataStore](#datastore).

**Parameters**

```
dataStoreId :  str, required
    The id of the data store.
```

**Return Type**

[DataStore](#datastore)

**Example**

```
dataStore = digitalExchange.dataStores.getDataStore("dataStoreId.1234")

dataStore.ls()
dataStore.cd("dirname1")

```

#### getDataStoreDirectory

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
dir = digitalExchange.dataStores.getDataStoreDirectory("dataStoreDirectoryId.1234")
```

#### getDataStoreFileMeta

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
file = digitalExchange.dataStores.getDataStoreFileMeta("dataStoreFileId.1234")
```

#### downloadDataStoreFile

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
file = digitalExchange.dataStores.downloadDataStoreFile("dataStoreFileId.1234", "./")
```

#### uploadFileToDataStore

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
file = digitalExchange.dataStores.uploadFileToDataStore("dataStoreId.1234", "dataStoreDirectoryId.1234", "./testFile.txt")
```

#### deleteDataStoreFile

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
file = digitalExchange.dataStores.deleteDataStoreFile("dataStoreFileId.1234")
```

---

### iot

#### getEndpoint

Gets information about the iot endpoint.  Includes the digital twin data model.

**Parameters**

```
iotEndpointId :  str, required
```

**Return Type**

[IotEndpoint](#iotendpoint)

**Example**

```
iotEndpointId = "iotEndpointId.1234"
endpoint = digitalExchange.iot.getEndpoint(
     iotEndpointId)

for property in endpoint.properties:
    print(f"Property {property.name} has type {property.schemaType}.")
for telemetry in endpoint.telemetry:
    print(f"Telemetry attribute {telemetry.name} has type {telemetry.schemaType}.")
```

#### listEndpointLastValues

Queries for the last known values of the endpoint's attributes.

**Parameters**

```
iotEndpointId :  str, required
resultFileWriteLocation :  str, optional
    If you would like the results stored in a file, include a name or path here. 
    Results will be in JSON format.
```

**Return Type**

[dict]

```
[
    {
        'attributeName': 'name'
        'lastValue': 'value',
        'timestamp': 'time'
    }
]
```

**Example**

```
iotEndpointId = "iotEndpointId.1234"
result = digitalExchange.iot.listEndpointLastValues(
     iotEndpointId)

# Example iteration through result
for entry in result:
    attributeName = entry.attributeName
    lastValue = entry.lastValue
    timestamp = entry.timestamp
```

#### queryByTimeRange

Queries the endpoint data using attribute and time filters, and writes the results to a file.

You must provide a time range and the attributeNames that you wish to query. The method automatically 
iterates over all pagination tokens so the result will be compiled upon completion. When the compiled result is available, it will be written to the local file system.

**Parameters**

```
iotEndpointId :  str, required
    The id of the endpoint.
attributeNames :  [str], required
    The attributes to include in the query result.
startTime :  ISO8601 str, required
    The beginning of the time interval.
    Example: "2022-09-27T10:22:45.000Z"
endTime: ISO8601 str, required
    The end of the time interval.
    Example: "2022-10-27T10:22:45.000Z"
resultFileWriteLocation: str, required
    The location to store the result file on the local file system. If a directory is provided but not a file name, the file will be saved as result.csv in the specified directory.
```

**Return Type**

Bool indicating success or error

**Example**

```
result = digitalExchange.iot.queryByTimeRange(
    "iotEndpointId.1234", 
    ["SOC", "V", "V - Setpoint"], 
    "2022-09-25T20:13:04.465Z", 
    "2022-09-26T20:58:04.465Z", 
    "./")
```

#### publish

Publish telemetry values for an endpoint.  One or more data records can be written at one time.

**Parameters**

```
iotEndpointId :  str, required
    The id of the endpoint.
data :  [dict], required
    Array of data records to write.  Each dict should contain the record's timestamp (defaults to current milliseconds), timeUnit ("MILLISECONDS", "SECONDS", "MICROSECONDS", "NANOSECONDS") ("MILLISECONDS" by default), and a dicitonary of attribute name, value pairs. Example shown below.
```

**Return Type**

Dictionary shown below

```
{
    'recordsWritten': [
        {
            'timestamp': '1670008999', # Epoch milliseconds
            'iotEndpointId': 'iotEndpointId.1234',
            'attributes': [
                {
                    'name': 'speed',
                    'value': '24.5'
                }
            ]
        }
    ],
    'recordsFailed': [
        {
            'record': {
                'timestamp': '1670007999', # Epoch milliseconds
                'iotEndpointId': 'iotEndpointId.1234',
                'attributes': [
                    {
                        'name': 'speed',
                        'value': '24.5'
                    }
                ]
            },
            'errors': [
                {
                    'errorType': 'DUPLICATE_RECORD',
                    'errorMessage': 'A record already exists for this endpoint at the given timestamp.'
                }
            ]
        }
    ]
}
```

**Example**

```
# Create the input data array
inputData = [
    {
        "timestamp": 1670008999,
        "timeUnit": "MILLISECONDS", # Optional - "MILLISECONDS" by default
        "attributes": {
            "speed": "40.2"
            "altitude": "2413.0"
        }
    }, {
        "timestamp": 1670009999,
        "timeUnit": "MILLISECONDS",
        "attributes": {
            "speed": "40.2"
            "altitude": "2413.0"
        }
    }
]

# Write the records
result = digitalExchange.iot.publish('iotEndpointId.1234', inputData)

recordsWritten = result.recordsWritten
failedRecords = result.failedRecords
```

#### updateEndpointProperties

Update the properties (state variables) for an endpoint.

**Parameters**

```
iotEndpointId :  str, required
    The id of the endpoint.
properties :  dict, required
    The properties to update and the new values. See example below for expected dict structure.
```

**Return Type**

[IotEndpoint](#iotendpoint)

**Example**

```

properties = {
    'moving': False
}

instance.iot.updateEndpointProperties(
     "iotEndpointId.1234",
     properties)
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

#### Methods

##### cd

Change the working directory.

**Parameters**

```
path: str, required
  The path to the desired directory.
```

**Example**
```
ds = digitalExchange.getDataStore("dataStoreId.1234")
ds.cd("docs")
```

##### ls

List the contents of the working directory.

**Parameters**

```
path: str, optional
  The path to the desired directory.
```

**Example**
```
ds = digitalExchange.getDataStore("dataStoreId.1234")
ds.ls("./")
```

##### pwd

Prints the abosulte path of the working directory.

**Parameters**

```
none
```

**Example**
```
ds = digitalExchange.getDataStore("dataStoreId.1234")
ds.pwd()
```

##### uploadFile

Upload a file to the data store in the working directory.

**Parameters**

```
localFilePath: str, required
  The location of the file on your local file system.
name: str, optional
  What the file should be named in the data store.
description: string, optional
  A brief description of the file and it's contents.
```

**Example**
```
ds = digitalExchange.getDataStore("dataStoreId.1234")
ds.uploadFile("./exampleFile.json", "remoteFileName.json", "A file containing a basic json object.")
```

##### downloadFile

Download the specified file.

**Parameters**

```
filename: str, required
  Name of the remote file in the current directory.
writeLocation: str, optional
  The location to store the downloaded file. If a filename is not given it will be saved with it's remote name.
```

**Example**
```
ds = digitalExchange.getDataStore("dataStoreId.1234")
ds.downloadFile("remoteFileName.json", "./desiredLocalFileName.json")
```

##### deleteFile

Deletes the file from the working directory.

**Parameters**

```
filename: str, required
  The name of the file to delete.
```

**Example**
```
ds = digitalExchange.getDataStore("dataStoreId.1234")
ds.deleteFile("remoteFileName.json")
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
dir = digitalExchange.getDataStoreDirectory("dataStoreDirectoryId.1234")
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

### IotEndpoint

#### Properties

```
iotEndpointId: str
iotHubId: str
    The iot hub the endpoint belongs to.
modelId: str
    The model the endpoint uses.
name: str
    The name of the endpoint.
description: str
properties: [EndpointProperty]
    The properties and their values. Properties are associated through the digital twin model used by the endpoint.
telemetry: [EndpointTelemetry]
    The telemetry attributes of the endpoint. Telemetry variables are associated through the digital twin model used by the endpoint.
```

### EndpointProperty

Data field that represents a state of the endpoint. No historical values. [(DTDL Property)](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=the%20following%20fields%3A-,Property,-%2D%20Properties%20are%20data).

#### Properties

```
name: str
    Name of the property.
description: str
schemaType: str : "integer", "double", "string", "boolean", "dateTime", "duration"
    The type of the variable.
writable: bool
    Indicates if the value of the property can be updated.
value: str
    The current value of the property. All variable types are wrapped in a string.
timestamp: str
    Timestamp (in milliseconds) that the current value was written.
```

### EndpointTelemetry

Data field representing measurements or events. Values are stored in a time series database. Telemetry values must be queried for separately (queryByTimeRange, listEndpointLastValues). [(DTDL Telemetry)](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=and%20telemetry%20below.-,Telemetry,-%2D%20Telemetry%20fields%20represent).

#### Properties

```
name: str
    Name of the property.
description: str
schemaType: str : "integer", "double", "string", "boolean", "dateTime", "duration"
    The type of the variable.
```

## Development

lone the repository with command `git clone https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk.git`.

Use VS Code with the Python extension to utilize formatting and code completion.

Deployment related code is in the root directory and the package code is found in `src/avista_digital_exchange_sdk`.

## Deployment

Follow the steps below to build and push the new package version to PyPi. [(Python packaging reference used)](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

**Steps**

1. Update `CHANGELOG.md` with new release notes.queryTimeSeriesDatabaseWithFilters
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