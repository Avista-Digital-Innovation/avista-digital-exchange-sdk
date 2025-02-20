# Avista Digital Exchange SDK<a id="avista-digital-exchange-sdk"></a>

This package allows you to access the Avista Digital Exchange and perform a subset of its features programmatically. All that you need is a personal authentication token that can be generated at [energy.collaboratives.io](https://energy.collaboratives.io).

[PyPi listing](https://pypi.org/project/avista-digital-exchange-sdk/)

[GitHub Repository](https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk)

*Note: This document contains HTML tags at each section header to support internal document references in the PyPi markdown viewer. View [this readme_renderer issue](https://github.com/pypa/readme_renderer/issues/169) for more information.*


## Table of Contents<a id="table-of-contents"></a>

*Note: Internal document links are not working when viewing this document in PyPi because of this [readme_renderer](https://github.com/pypa/readme_renderer/issues/169) issue*

1. [Avista Digital Exchange SDK](#avista-digital-exchange-sdk)
   1. [Table of Contents](#table-of-contents)
   2. [Getting Started](#getting-started)
   3. [AvistaDigitalExchange Functions](#avistadigitalexchange-functions)
      1. [getUserInfo](#getuserinfo)
      2. [dataStore](#datastore)
         1. [listDataStores](#listdatastores)
         2. [getDataStore](#getdatastore)
         3. [getDataStoreDirectory](#getdatastoredirectory)
         4. [getDataStoreFileMeta](#getdatastorefilemeta)
         5. [downloadDataStoreFile](#downloaddatastorefile)
         6. [uploadFileToDataStore](#uploadfiletodatastore)
         7. [deleteDataStoreFile](#deletedatastorefile)
      3. [iot](#iot)
         1. [getEndpoint](#getendpoint)
         1. [getGroup](#getgroup)
         2. [createEndpoint](#createendpoint)
         2. [addEndpointsToGroup](#addendpointstogroup)
         3. [createModel](#createmodel)
         4. [listEndpointLastValues](#listendpointlastvalues)
         5. [queryByTimeRange](#querybytimerange)
         6. [queryDataByTimeRange](#querydatabytimerange)
         7. [publish](#publish)
         8. [updateEndpointProperties](#updateendpointproperties)
         9. [subscribeToEndpoint ](#subscribetoendpoint-)
      4. [dataCapture](#datacapture)
         1. [startCapture](#startcapture)
         2. [stopCapture](#stopcapture)
         3. [publishData](#publishdata)
         4. [subscribeToData](#subscribetodata)
   4. [Types](#types)
      1. [User](#user)
      2. [Organization](#organization)
      3. [DataStore](#datastore-1)
         1. [Methods](#methods)
            1. [cd](#cd)
            2. [ls](#ls)
            3. [pwd](#pwd)
            4. [uploadFile](#uploadfile)
            5. [downloadFile](#downloadfile)
            6. [deleteFile](#deletefile)
      4. [DataStoreDirectory](#datastoredirectory)
         1. [Methods](#methods-1)
            1. [printContents](#printcontents)
      5. [DataStoreFile](#datastorefile)
      6. [DigitalTwinModel](#digitaltwinmodel)
      7. [ModelProperty](#modelproperty)
      8. [ModelTelemetry](#modeltelemetry)
      9. [IotEndpoint](#iotendpoint)
      10. [EndpointProperty](#endpointproperty)
      11. [EndpointTelemetry](#endpointtelemetry)
      12. [DxTypes.CaptureDataRecordInput](#dxtypescapturedatarecordinput)
      13. [DxTypes.PublishCaptureDataResult](#dxtypespublishcapturedataresult)
      14. [DxTypes.PublishCaptureDataSuccessfulRecord](#dxtypespublishcapturedatasuccessfulrecord)
      15. [DxTypes.PublishCaptureDataFailedRecord](#dxtypespublishcapturedatafailedrecord)
      16. [DxTypes.StartCaptureResult](#dxtypesstartcaptureresult)
      17. [DxTypes.StopCaptureResult](#dxtypesstopcaptureresult)
   5. [Troubleshooting](#troubleshooting)
   6. [Development](#development)
   7. [Deployment](#deployment)
   8. [Generating Python types and GraphQL Client from GraphQL Schema](#generating-python-types-and-graphql-client-from-graphql-schema)
   9. [Fix for py-graphql-mapper module](#fix-for-py-graphql-mapper-module)
   10. [websocketclient / websocket-client submodule](#websocketclient--websocket-client-submodule)
   11. [Resources](#resources)

## Getting Started<a id="getting-started"></a>

1. Install the python package.

```bash
pip3 install avista-digital-exchange-sdk
```

2. Ensure you have the latest version.

```bash
pip3 install --upgrade avista-digital-exchange-sdk
```

3. Import the module in your python script.
4. Initialize the module with your authentication token.  The authentication token can be a user authentication token, or an iot endpoint authentication token.  If an endpoint token is used, only iot operations can be performed.

```py
from avista_digital_exchange_sdk import AvistaDigitalExchange

digitalExchange = AvistaDigitalExchange("tokenvalue")

# Alternatively, instantiate with debug mode enabled
# digitalExchange = AvistaDigitalExchange("tokenvalue", True)
```

---

## AvistaDigitalExchange Functions<a id="avistadigitalexchange-functions"></a>

### getUserInfo<a id="getuserinfo"></a>

Retrieves your user information.

**Parameters**

None

**Return Type**

[User](#user)

**Example**

```py
user = digitalExchange.getUserInfo()
```

---

### dataStore<a id="datastore"></a>

#### listDataStores<a id="listdatastores"></a>

Lists the data stores you own.

**Parameters**

None

**Return Type**

[[DataStore]](#datastore)

**Example**

```py
dataStores = digitalExchange.dataStores.listDataStores()
```

#### getDataStore<a id="getdatastore"></a>

Gets a data store object. The object can be interacted with as a command line utility to navigate the data store. See [DataStore](#datastore).

**Parameters**

```
dataStoreId :  str, required
    The id of the data store.
```

**Return Type**

[DataStore](#datastore)

**Example**

```py
dataStore = digitalExchange.dataStores.getDataStore("dataStoreId.1234")

dataStore.ls()
dataStore.cd("dirname1")

```

#### getDataStoreDirectory<a id="getdatastoredirectory"></a>

Gets the directory metadata and contents.

**Parameters**

```
dataStoreDirectoryId :  str, required
    The id of the directory.
```

**Return Type**

[DataStoreDirectory](#datastoredirectory)

**Example**

```py
dir = digitalExchange.dataStores.getDataStoreDirectory("dataStoreDirectoryId.1234")
```

#### getDataStoreFileMeta<a id="getdatastorefilemeta"></a>

Gets the metadata of a file.

**Parameters**

```
dataStoreFileId :  str, required
    The id of the file.
```

**Return Type**

[DataStoreFile](#datastorefile)

**Example**

```py
file = digitalExchange.dataStores.getDataStoreFileMeta("dataStoreFileId.1234")
```

#### downloadDataStoreFile<a id="downloaddatastorefile"></a>

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

```py
file = digitalExchange.dataStores.downloadDataStoreFile("dataStoreFileId.1234", "./")
```

#### uploadFileToDataStore<a id="uploadfiletodatastore"></a>

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

```py
file = digitalExchange.dataStores.uploadFileToDataStore("dataStoreId.1234", "dataStoreDirectoryId.1234", "./testFile.txt")
```

#### deleteDataStoreFile<a id="deletedatastorefile"></a>

Removes a file from the data store and deletes it from the Digital Exchange.

**Parameters**

```
dataStoreFileId :  str, required
    The id of the file to delete.
```

**Return Type**

[DataStoreFile](#datastorefile)

**Example**

```py
file = digitalExchange.dataStores.deleteDataStoreFile("dataStoreFileId.1234")
```

---

### iot<a id="iot"></a>

#### getEndpoint<a id="getendpoint"></a>

Gets information about the iot endpoint.  Includes the digital twin data model.

**Parameters**

```
iotEndpointId :  str, required
```

**Return Type**

[IotEndpoint](#iotendpoint)

**Example**

```py
iotEndpointId = "iotEndpointId.1234"
endpoint = digitalExchange.iot.getEndpoint(
     iotEndpointId)

for property in endpoint.properties:
    print(f"Property {property.name} has type {property.schemaType}.")
for telemetry in endpoint.telemetry:
    print(f"Telemetry attribute {telemetry.name} has type {telemetry.schemaType}.")
```

#### getGroup<a id="getgroup"></a>

Gets information about the iot group.  Can include information about the endpoints.

**Parameters**

```
iotGroupId :  str, required
includeEndpoints :  bool, required
```

**Return Type**

[IotGroup](#iotgroup)

**Example**

```py
iotGroupId = "iotGroupId.1234"
includeEndpoints = True
group = digitalExchange.iot.getGroup(
     iotEndpointId
     includeEndpoints)

for endpoint in group.endpoints:
    print(f"Endpoint {endpoint.name} has id {endpoint.iotEndpointId}.")
```


#### createEndpoint<a id="createendpoint"></a>

Creates a new IoT Endpoint within an existing IoT Hub.

**Parameters**

```
iotHubId :  str, required
    The hub in which to create the endpoint in.
modelId :  str, required
    The digital twin model for this endpoint to use.
name :  str, required
    The name of the iot endpoint.
description :  str, optional
```

**Return Type**

[IotEndpoint](#iotendpoint)

**Example**

```py
iotHubId = "iotHubId.1234"
modelId = "modelId.4321"
name = "Temperature Sensor"
description = "The sensor on top of the house"


endpoint = digitalExchange.iot.createEndpoint(
    iotHubId,
    modelId,
    name,
    description)
```


#### addEndpointsToGroup<a id="addendpointstogroup"></a>

Adds an existing IoT Endpoint to an IoT Group.

**Parameters**

```
iotGroupId :  str, required
    The group that will get the endpoint(s).
iotEndpointId :  str|list, required
    The endpoints that will be added. If there is only one endpoint, a string may be passed in place of a list.
```

**Return Type**

[IotGroup](#iotgroup)

**Example**

```py
iotGroupId = "iotGroupId.1234"
iotEndpointIds = ["iotEndpointId.4321", "iotEndpointId.5678"]


group = digitalExchange.iot.addEndpointsToGroup(
    iotGroupId,
    iotEndpointIds)
```



#### createModel<a id="createmodel"></a>

Creates a digital twin data model.

**Parameters**

```
name :  str, required
    Name should not contain spaces or special characters. Alphanumeric characters only.
description :  str, optional
properties :  [dict], required
    Array of dictionaries representing the properties to associate with the model. See https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=the%20following%20fields%3A-,Property,-%2D%20Properties%20are%20data for more information on model properties.
    The expected dictionary keys are as follows:
        - name : str, required
            Name of the property
        - description : str, optional
            Description of the property
        - schemaType : str, required
            The variable type of the property. Valid values are "integer", "double", "string", "boolean", "dateTime", and "duration"
        - defaultValue : str, optional
            Wrap the value, regardless of schemaType, in a string
        - writable : bool, optional
            Determines if the proeprty value can be updated. Default value is False

telemetry :  [dict], required
    Array of dictionaries representing the telemetry variables to associate with the model. See https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=and%20telemetry%20below.-,Telemetry,-%2D%20Telemetry%20fields%20represent for more information on model telemetry.
    The expected dictionary keys are as follows:
        - name : str, required
            Name of the telemetry
        - description : str, optional
            Description of the telemetry
        - schemaType : str, required
            The variable type of the telemetry. Valid values are "integer", "double", "string", "boolean", "dateTime", and "duration"

```

**Return Type**

[DigitalTwinModel](#digitaltwinmodel)

**Example**

```py
properties = [
    {
        "name": "Longitude",
        "description": "the last known longitude of the device",
        "schemaType": "double",
        "defaultValue": "-117.426048",
        "writable": True
    },
    {
        "name": "Latitude",
        "description": "the last known latitude of the device",
        "schemaType": "double",
        "defaultValue": "47.658779",
        "writable": True
    }
]

telemetry = [
    {
        "name": "Temperature",
        "description": "Temp from the sensor in celsius",
        "schemaType": "double"
    },
    {
        "name": "Humidity",
        "description": "Humidity from the sensor",
        "schemaType": "double"
    }
]

model = digitalExchange.iot.createModel(
    "MyFirstModel", 
    "A simple example digital twin model", 
    properties, 
    telemetry)
```

#### listEndpointLastValues<a id="listendpointlastvalues"></a>

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

```py
iotEndpointId = "iotEndpointId.1234"
result = digitalExchange.iot.listEndpointLastValues(
     iotEndpointId)

# Example iteration through result
for entry in result:
    attributeName = entry["attributeName"]
    lastValue = entry["lastValue"]
    timestamp = entry["timestamp"]
```

#### queryByTimeRange<a id="querybytimerange"></a>

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

```py
result = digitalExchange.iot.queryByTimeRange(
    "iotEndpointId.1234", 
    ["SOC", "V", "V - Setpoint"], 
    "2022-09-25T20:13:04.465Z", 
    "2022-09-26T20:58:04.465Z", 
    "./")
```

#### queryDataByTimeRange<a id="querydatabytimerange"></a>

Queries the endpoint data using attribute and time filters, returning as a dictionary

You must provide a time range and the attributeNames that you wish to query. The method automatically 
iterates over all pagination tokens so the result will be compiled upon completion. When the compiled result is available.

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
```

**Return Type**

List including the response values

    [
        { 'iotEndpointId': 'iotEndpointId.1234', name: 'Iot Endpoint Name', timestamp: '2024-03-19 10:39:31.942000000', 'attribute1': 1.0, 'attribute2': 2.0'},
        { 'iotEndpointId': 'iotEndpointId.1234', name: 'Iot Endpoint Name', timestamp: '2024-03-19 10:40:31.942000000', 'attribute1': 1.1, 'attribute2': 2.1'}   
    ]

**Example**

```py
result = digitalExchange.iot.queryDataByTimeRange(
    "iotEndpointId.1234", 
    ["SOC", "V", "V - Setpoint"], 
    "2022-09-25T20:13:04.465Z", 
    "2022-09-26T20:58:04.465Z")
```

#### publish<a id="iotpublish"></a>

Publish telemetry values for an endpoint.  One or more data records can be written at one time.

**Parameters**

```
iotEndpointId :  str, required
    The id of the endpoint.
data :  [dict], required
    Array of data records to write.  Each dict should contain the record's timestamp (defaults to current milliseconds), timeUnit ("MILLISECONDS", "SECONDS", "MICROSECONDS", "NANOSECONDS", "ISO8601") ("MILLISECONDS" by default), and a dicitonary of attribute name, value pairs. Example shown below.
    ISO8601 timestamps should match format yyyy-MM-ddTHH:mm:ss.SSSZ
```

**Return Type**

Dictionary shown below

```
{
    'recordsWritten': [
        {
            'timestamp': '1670008999', 
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
                'timestamp': '1670007999',
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

```py
# Create the input data array
inputData = [
    {
        "timestamp": 1670008999,
        "timeUnit": "MILLISECONDS", # Optional - "MILLISECONDS" by default
        "attributes": {
            "speed": "40.2",
            "altitude": "2413.0"
        }
    }, {
        "timestamp": "2022-12-15T12:45:31.055Z",
        "timeUnit": "ISO8601",
        "attributes": {
            "speed": "40.2",
            "altitude": "2413.0"
        }
    }
]

# Write the records
result = digitalExchange.iot.publish('iotEndpointId.1234', inputData)

recordsWritten = result.recordsWritten
failedRecords = result.failedRecords
```

#### updateEndpointProperties<a id="updateendpointproperties"></a>

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

```py

properties = {
    'moving': False
}

digitalExchange.iot.updateEndpointProperties(
     "iotEndpointId.1234",
     properties)
```

#### subscribeToEndpoint <a id="subscribetoendpoint"></a>

Subscribe to real-time updates from IoT endpoint publish events.

**Parameters**

```
iotEndpointId :  str, required
    The id of the endpoint.
```

**Return Type**

Dictionary shown below

```
{
    'iotEndpointId': 'iotEndpointId.1234',
    'recordsWritten': [
        {
            'timestamp': '1670008999', 
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
                'timestamp': '1670007999',
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

```py
import tracemalloc
import asyncio
from avista_digital_exchange_sdk import AvistaDigitalExchange

# Specify the endpoint you are subscribing to
iotEndpointId = ENDPOINT_ID
authenticationToken = AUTHENTICATION_TOKEN
dxInstance = AvistaDigitalExchange(
    authenticationToken, True)

async def subscriptionTest():
    try:
        async for result in dxInstance.iot.subscribeToEndpoint(
                endpointId=iotEndpointId):
            # This code block runs each time a subscription event is received.
            print(result)

    except Exception as error:
        print(f"iot.subscribeToEndpoint failed with error: {error}")
        raise error


asyncio.run(subscriptionTest())
```

---

### dataCapture<a id="datacapture"></a>


#### startCapture<a id="startcapture"></a>

Commands a Data Capture to begin collecting data. Capture must be in 'Ready' state for startCapture to succeed.

**Parameters**

```
captureId :  str, required
    The id of the Data Capture.
```

**Return Type**

[DxTypes.StartCaptureResult](#dxtypesstartcaptureresult)


**Example**

```py
import asyncio
from avista_digital_exchange_sdk import AvistaDigitalExchange

# NOTE: The capture must be in 'READY' state to be started.
captureId = CAPTURE_ID
authenticationToken = AUTHENTICATION_TOKEN


async def main():
    # Create an instance of the AvistaDigitalExchange SDK
    # You may use a user authentication token or the authentication token of the Data Capture
    digitalExchange = AvistaDigitalExchange(authenticationToken)
    print("Instantiated AvistaDigitalExchange instance with authentication token")

    try:
        print("Calling dataCapture.startCapture")
        result = await digitalExchange.dataCapture.startCapture(
            captureId=captureId)
    except:
        print("dataCapture.startCapture failed")

if __name__ == "__main__":
    asyncio.run(main())

```


#### stopCapture<a id="stopcapture"></a>

Commands a Data Capture to stop collecting data. Capture must be in 'CAPTURING' state for stopCapture to succeed.

**Parameters**

```
captureId :  str, required
    The id of the Data Capture.
```

**Return Type**

[DxTypes.StopCaptureResult](#dxtypesstopcaptureresult)


**Example**

```py
import asyncio
from avista_digital_exchange_sdk import AvistaDigitalExchange

# NOTE: The capture must be in 'CAPTURING' state to be stopped.
captureId = CAPTURE_ID
authenticationToken = AUTHENTICATION_TOKEN


async def main():
    # Create an instance of the AvistaDigitalExchange SDK
    # You may use a user authentication token or the authentication token of the Data Capture
    digitalExchange = AvistaDigitalExchange(authenticationToken)
    print("Instantiated AvistaDigitalExchange instance with authentication token")

    try:
        print("Calling dataCapture.stopCapture")
        result = await digitalExchange.dataCapture.stopCapture(
            captureId=captureId)
    except:
        print("dataCapture.stopCapture failed")

if __name__ == "__main__":
    asyncio.run(main())

```


#### publishData<a id="publishdata"></a>

Publish attribute values to an active Data Capture.

**Parameters**

```
captureId :  str, required
    The id of the Data Capture.
data :  [DxTypes.CaptureDataRecordInput], required
    Array of data records to write.  Each dict should contain the record's timestamp, timeUnit ("MILLISECONDS"), and a dicitonary of attributeId, value pairs. Example shown below.
```

**Return Type**

[DxTypes.PublishCaptureDataResult](#dxtypespublishcapturedataresult)


**Example**

```py
import asyncio
import time
from avista_digital_exchange_sdk import AvistaDigitalExchange, DxTypes

authenticationToken = AUTHENTICATION_TOKEN_VALUE
captureId = YOUR_CAPTURE_ID

# Create an instance of the AvistaDigitalExchange SDK
# You may use a user authentication token or the authentication token of the Data Capture
digitalExchange = AvistaDigitalExchange(authenticationToken)
print("Instantiated AvistaDigitalExchange instance with authentication token")

# Specify the capture you are publishing data to.
# NOTE: The capture must be in Capturing state to accept data

def getCurrentMilliseconds():
    return int(f'{time.time() * 1000}'.split('.')[0])

async def publishDataExample():
    # Prepare the data to be published
    # Replace ATTRIBUTE_ID and ATTRIBUTE_VALUE
    attributeValueMap = {
        ATTRIBUTE_ID: ATTRIBUTE_VALUE,
        ATTRIBUTE_ID: ATTRIBUTE_VALUE,
        ATTRIBUTE_ID: ATTRIBUTE_VALUE,
    }

    data = [DxTypes.CaptureDataRecordInput(
            timestamp=f'{getCurrentMilliseconds()}',
            timeUnit="MILLISECONDS",
            attributeValues=attributeValueMap)]
    try:
        print("Calling dataCapture.publishData")
        result = await digitalExchange.dataCapture.publishData(
            captureId=captureId, data=data)
    except:
        print("dataCapture.publishData failed")

asyncio.run(publishDataExample())
```

#### subscribeToData<a id="subscribetodata"></a>

Listen for data being published to a Data Capture in realtime.

**Parameters**

```
captureId :  str, required
    The id of the Data Capture.
```

**Return Type**

AsyncIterator[[DxTypes.PublishCaptureDataResult](#dxtypespublishcapturedataresult)]

**Example**

```py
import asyncio
from avista_digital_exchange_sdk import AvistaDigitalExchange

authenticationToken = AUTHENTICATION_TOKEN
captureId = CAPTURE_ID


async def main():
    # Create an instance of the AvistaDigitalExchange SDK
    # You may use a user authentication token or the authentication token of the Data Capture
    digitalExchange = AvistaDigitalExchange(authenticationToken)
    print("Instantiated AvistaDigitalExchange instance with authentication token")

    try:
        print("Calling dataCapture.subscribeToData")
        # The for-loop will run each time a data publish event is received.
        async for result in digitalExchange.dataCapture.subscribeToData(
                captureId=captureId):
            print("DataCapture.subscribeToData: Data received.")
            print("Do something with data...")
    except Exception as error:
        print(f"dataCapture.subscribeToData failed with error: {error}")
        raise error

if __name__ == "__main__":
    asyncio.run(main())

```


---

## Types<a id="types"></a>

### User<a id="user"></a>

Stores basic information about a Digital Exchange user.

**Properties**

```
userId : str
    The user's unique id number.
firstName : str
lastName : str
organization : Organization
    The organization that the user is a member of.
```

### Organization<a id="organization"></a>

Stores basic information about a Digital Exchange member organization.

**Properties**

```
name : str
organizationId : str
```

### DataStore<a id="datastore-1"></a>

A Data Store Service object.

**Properties**

```
dataStoreId: str
name: str
description: str
ownerUserId: str
homeDirectoryId: str
    The dataStoreDirectoryId of the Data Store's home directory
```

#### Methods<a id="methods"></a>

##### cd<a id="cd"></a>

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

##### ls<a id="ls"></a>

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

##### pwd<a id="pwd"></a>

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

##### uploadFile<a id="uploadfile"></a>

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

##### downloadFile<a id="downloadfile"></a>

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

##### deleteFile<a id="deletefile"></a>

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

### DataStoreDirectory<a id="datastoredirectory"></a>

A directory in a Data Store file storage hierarchy.

**Properties**

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

#### Methods<a id="methods-1"></a>

##### printContents<a id="printcontents"></a>

Lists all of the directory contents (directories and files), along with their ids.

**Parameters**

None

**Example**

```
dir = digitalExchange.getDataStoreDirectory("dataStoreDirectoryId.1234")
dir.printContents()
```


### DataStoreFile<a id="datastorefile"></a>

A file belonging to a Data Store.

**Properties**

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

### DigitalTwinModel<a id="digitaltwinmodel"></a>

**Properties**

```
modelId: str
    Id of the model
ownerUserId: str
    UserId of the owner of the model
displayName: str
    The name of the model
description: str
    Description of the model
properties: [ModelProperty]
    All properties associated with the model
telemetry: [ModelTelemetry]
    All telemetry associated with the model
```

### ModelProperty<a id="modelproperty"></a>

Data field that represents a state variable. [(DTDL Property)](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=the%20following%20fields%3A-,Property,-%2D%20Properties%20are%20data).

**Properties**

```
name: str
    Name of the property variable.
description: str
schemaType: str : "integer", "double", "string", "boolean", "dateTime", "duration"
    The type of the variable.
defaultValue: str
    The original value of the property.
writable: bool
    Indicates if the value of the property can be updated.
```

### ModelTelemetry<a id="modeltelemetry"></a>

Data field representing measurements or events. Values are stored in a time series database. [(DTDL Telemetry)](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=and%20telemetry%20below.-,Telemetry,-%2D%20Telemetry%20fields%20represent).

**Properties**

```
name: str
    Name of the telmetry.
description: str
schemaType: str : "integer", "double", "string", "boolean", "dateTime", "duration"
    The type of the variable.
```


### IotEndpoint<a id="iotendpoint"></a>

**Properties**

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

### IotGroup<a id="iotgroup"></a>

**Properties**

```
iotGroupId: str
iotHubId: str
    The iot hub the group belongs to.
name: str
    The name of the group.
description: str
endpoints: [IotEndpoint]
    Endpoints contained within the Group.
```

### EndpointProperty<a id="endpointproperty"></a>

Data field that represents a state of the endpoint. No historical values. [(DTDL Property)](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=the%20following%20fields%3A-,Property,-%2D%20Properties%20are%20data).

**Properties**

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

### EndpointTelemetry<a id="endpointtelemetry"></a>

Data field representing measurements or events. Values are stored in a time series database. Telemetry values must be queried for separately (queryByTimeRange, listEndpointLastValues). [(DTDL Telemetry)](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models#:~:text=and%20telemetry%20below.-,Telemetry,-%2D%20Telemetry%20fields%20represent).

**Properties**

```
name: str
    Name of the telemetry.
description: str
schemaType: str : "integer", "double", "string", "boolean", "dateTime", "duration"
    The type of the variable.
```

### DxTypes.CaptureDataRecordInput<a id="dxtypescapturedatarecordinput"></a>

A data record that is to be published to a Data Capture.

**Properties**

```
timestamp: str
    The timestamp of the data record
timeUnit: str
    The format of the timestamp
attributeValues: dict
    A dictionary containing the data to be written for the given timestmap. Key values should be attributeIds that map to the relevant attribute values. 
```

### DxTypes.PublishCaptureDataResult<a id="dxtypespublishcapturedataresult"></a>

Result object for the DataCapture.publishData operation.

**Properties**

```
success: bool
    Indicates if the action was successful
captureId: str
    The captureId of the Data Capture published to.
recordsWritten: [DxTypes.PublishCaptureDataSuccessfulRecord] | None
    An array of input data records that were successfully written.
recordsFailed: [DxTypes.PublishCaptureDataFailedRecord] | None    
    An array of input data records that were not written.
error: str | None
    An error message if a problem was encountered.
```

### DxTypes.PublishCaptureDataSuccessfulRecord<a id="dxtypespublishcapturedatasuccessfulrecord"></a>

A record that was published and written to a Data Capture.

**Properties**

```
timestamp: str
    The timestamp of the data record
timeUnit: str
    The format of the timestamp
attributeId: str
attributeValue: str
```

### DxTypes.PublishCaptureDataFailedRecord<a id="dxtypespublishcapturedatafailedrecord"></a>

A record that was published but not written to a Data Capture.

**Properties**

```
timestamp: str
    The timestamp of the data record
timeUnit: str
    The format of the timestamp
attributeId: str
attributeValue: str
message: str
    Explains why the data record failed.
```


### DxTypes.StartCaptureResult<a id="dxtypesstartcaptureresult"></a>

Result object for the DataCapture.startCapture operation.

**Properties**

```
success: bool
    Indicates if the action was successful
captureId: str
    The captureId of the Data Capture being started.
startedAt: str | None
    The timestamp at which the Data Capture was started (if successful).
error: str | None
    An error message if a problem was encountered.
```


### DxTypes.StopCaptureResult<a id="dxtypesstopcaptureresult"></a>

Result object for the DataCapture.stopCapture operation.

**Properties**

```
success: bool
    Indicates if the action was successful
captureId: str
    The captureId of the Data Capture being stopped.
stoppedAt: str | None
    The timestamp at which the Data Capture was stopped (if successful).
error: str | None
    An error message if a problem was encountered.
```


## Troubleshooting<a id="troubleshooting"></a>



## Development<a id="development"></a>

Clone the repository with command `git clone https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk.git`.

Use VS Code with the Python extension to utilize formatting and code completion.

Deployment related code is in the root directory and the package code is found in `src/avista_digital_exchange_sdk`.

## Deployment<a id="deployment"></a>

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

## Generating Python types and GraphQL Client from GraphQL Schema

See instructions in graphql_codegen/README.md

## Fix for py-graphql-mapper module

The plugin was failing to assign the correct type for attributes of a schema type that were lists of other custom schema types (ie. IotEndpoint contains array of Properties and Telemetry).

I edited the function _init_type(obj, fieldType, fieldName) in the file gql_init.py from commit bc0888b. There are conditions for different fieldTypes. I edited the condition if the field is a list. Changed
'''
    elif fieldType == list or (hasattr(fieldType, '__origin__') and fieldType.__origin__ == list):
'''
to
'''
    elif fieldType == list or (hasattr(fieldType, '__origin__') and fieldType.__origin__ == list) or "gql_types.list_" in str(fieldType):
'''

## websocketclient / websocket-client submodule

To mitigate an issue when using ```import websocket``` when both websocket and websocket-client packages are installed, we added a git submodule to reference websocket-client directly. Once the SDK moves away from the subscriptionClient.py usage, this can be removed.

## Resources<a id="resources"></a>

1. [Avista Digital Exchange](https://energy.collaboratives.io/)
2. [PyPi SDK project listing](https://pypi.org/project/avista-digital-exchange-sdk/)
3. [GitHub project repository](https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk)
4. [Python package deployment tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
5. [PyPi API Token](https://pypi.org/help/#apitoken)