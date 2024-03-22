
from .endpointUtil import *
from .exceptions import *

from .graphql_mutations.iot_publish import iot_publish
from .graphql_mutations.iot_updateEndpointProperties import iot_updateEndpointProperties
from .graphql_mutations.iot_generateQueryResultExport import iot_generateQueryResultExport
from .graphql_mutations.iot_cancelQuery import iot_cancelQuery
from .graphql_mutations.iot_createEndpoint import iot_createEndpoint
from .graphql_mutations.iot_createModel import iot_createModel
from .graphql_queries.iot_getEndpoint import iot_getEndpoint
from .graphql_queries.iot_listEndpointLastValues import iot_listEndpointLastValues
from .graphql_queries.iot_queryByTimeRange import iot_queryByTimeRange
from .graphql_subscriptions.onNotifyIotQueryExportComplete import onNotifyIotQueryExportComplete
from .data_types.iot_data_record_input import IotDataRecordInput
from .data_types.iot_attribute_value_input import IotAttributeValueInput
from .data_types.endpoint_property_input import EndpointPropertyInput
from .data_types.endpoint_query_filter_input import EndpointQueryFilterInput
from .data_types.model_property_input import ModelPropertyInput
from .data_types.model_telemetry_input import ModelTelemetryInput
import time
import signal
import datetime
import re


class IoTUtil(object):

    def __init__(self, debug, client):
        self._debug = debug
        self._client = client
        self.endpoint = EndpointUtil(debug, client)

    def publish(self, iotEndpointId, data):
        inputData = []
        for record in data:
            attributes = []
            if "timestamp" not in record:
                record["timestamp"] = f'{round(time.time()*1000)}'
            if "timeUnit" not in record:
                record["timeUnit"] = f'MILLISECONDS'
            IotDataRecordInput.checkDictForCorrectFields(record)
            for attributeName, value in (record["attributes"]).items():
                attributes.append(IotAttributeValueInput(
                    attributeName, value))
            inputData.append(IotDataRecordInput(
                record["timestamp"], record["timeUnit"] if "timeUnit" in record else "MILLISECONDS", attributes))

        mutation = iot_publish(
            self._client, self._debug, iotEndpointId, inputData)
        result = mutation.performMutation()

        resultDict = result.resultDict

        return {
            'recordsWritten': resultDict["recordsWritten"],
            'recordsFailed': resultDict["failedRecords"]
        }

    def updateEndpointProperties(self, iotEndpointId, properties):
        for key in properties:
            if 'value' not in properties[key]:
                raise Exception(f"Missing 'value' in properties['{key}']")

        propertiesInput = []
        for key in properties:
            propertiesInput.append(EndpointPropertyInput(
                key,
                properties[key]["value"],
                properties[key]["timestamp"] if 'timestamp' in properties[key] else f'{round(time.time()*1000)}'))

        mutation = iot_updateEndpointProperties(
            self._client, self._debug, iotEndpointId, propertiesInput)
        result = mutation.performMutation()
        return result

    def queryByTimeRange(self, iotEndpointId, attributeNames, startTime, endTime, resultWriteLocation):
        exportFileResult = self._genQueryByTimeRange(iotEndpointId, attributeNames, startTime, endTime, resultWriteLocation)
        
        exportFileResult.downloadAndWriteFile(exportFileResult.url, resultWriteLocation)

        return True

    def queryDataByTimeRange(self, iotEndpointId, attributeNames, startTime, endTime):
        exportFileResult = self._genQueryByTimeRange(iotEndpointId, attributeNames, startTime, endTime)
        
        exportText = exportFileResult.downloadFile(exportFileResult.url)
        export = self._generateRangeQueryDict(exportText)
        
        return export


    def _genQueryByTimeRange(self, iotEndpointId, attributeNames, startTime, endTime, resultWriteLocation=None):

        date = datetime.datetime.strptime(startTime, '%Y-%m-%dT%H:%M:%S.%fZ')
        startTime = int(
            (date - datetime.datetime(1970, 1, 1)).total_seconds()*1000)
        date = datetime.datetime.strptime(endTime, '%Y-%m-%dT%H:%M:%S.%fZ')
        endTime = int(
            (date - datetime.datetime(1970, 1, 1)).total_seconds()*1000)

        filter = EndpointQueryFilterInput(iotEndpointId, attributeNames)
        endpointFilterInput = [filter]
        query = iot_queryByTimeRange(
            self._client, self._debug, endpointFilterInput, startTime, endTime)
        result = query.performQuery()
        queryId = result.queryId
        if self._debug:
            print(
                f'received query result chunk {result.resultChunkIndex}')

        def quitHandler(signum, frame):
            # Stop query
            if queryId is not None:
                if self._debug:
                    print("Cancelling query....")
                mutation = iot_cancelQuery(
                    self._client, self._debug, queryId)
                cancelResult = mutation.performMutation()

        signal.signal(signal.SIGINT, quitHandler)

        while result.nextToken is not None:
            query = iot_queryByTimeRange(
                self._client, self._debug, endpointFilterInput, startTime, endTime, result.nextToken, result.clientToken, result.queryString, result.queryId)
            result = query.performQuery()
            if self._debug:
                print(
                    f'received query result chunk {result.resultChunkIndex}')
                    
        export = True
        # get onNotifyObject
        subscription = self._getSubscriptionToQueryExportFileCompletion(
            queryId)


        # Generate export file
        mutationResult = self._generateQueryResultFile(queryId, "CSV")
        if self._debug:
            print(f'mutation result {mutationResult}')

        # wait for subscription notification
        exportFileResult = subscription.waitForResponse(240)
        if self._debug:
            print(exportFileResult)

        return exportFileResult


    def getEndpoint(self, iotEndpointId):
        query = iot_getEndpoint(
            self._client, self._debug, iotEndpointId)
        result = query.performQuery()
        return result

    def listEndpointLastValues(self, iotEndpointId):
        query = iot_listEndpointLastValues(
            self._client, self._debug, iotEndpointId)
        result = query.performQuery()
        resultArray = []
        if len(result.data) > 0:
            for entry in result.data[0].telemetryValues:
                resultArray.append({
                    "attributeName": entry.telemetryModel.name,
                    "lastValue": entry.value,
                    "timestamp": entry.timestamp
                })
        return resultArray

    def _getSubscriptionToQueryExportFileCompletion(self, queryId):
        subscription = onNotifyIotQueryExportComplete(
            self._client, self._debug, queryId)
        subscribedThread = subscription.initiateSubscriptionOnNewThread()
        return subscription

    def _generateQueryResultFile(self, queryId, fileFormat="CSV"):
        mutation = iot_generateQueryResultExport(
            self._client, self._debug, queryId, fileFormat)
        result = mutation.performMutation()
        return result

    def _generateRangeQueryDict(self, text):
        rows = text.split('\n')
        if rows[-1] == '':
            rows.pop()
        
        # First row in the csv text file is the headers
        headers = rows[0].split(',')

        result = []
        for data_row in rows[1:]:

            data = {}

            headerCount = 0
            data_values = data_row.split(',')
            for header in headers:
                data[header] = self._convertFromString(data_values[headerCount])
                headerCount += 1

            result.append(data)
        
        return result
    
    def _convertFromString(self, value):
        result = value
        if re.search('^-?\d+\.\d+$', value):
            result = float(value)
        elif re.search('^-?\d+$', value):
            result = int(value)

        return result

    def createEndpoint(self, iotHubId, modelId, name, description=None):
        mutation = iot_createEndpoint(
            self._client, self._debug, iotHubId, modelId, name, description)
        result = mutation.performMutation()
        return result

    def createModel(self, name, description, properties, telemetry):
        propertyObjects = []
        telemetryObjects = []
        index = 0

        if not name.isalnum():
            raise InvalidParameterException(
                "Model name must contain only alphanumeric characters")
        dtmiSegment = name

        for prop in properties:
            writable = None
            if "writable" in prop:
                if prop["writable"]:
                    writable = "true"
                else:
                    writable = "false"

            propertyObjects.append(
                ModelPropertyInput(
                    prop["name"],
                    prop["description"] if "description" in prop else None,
                    prop["schemaType"],
                    prop["defaultValue"] if "defaultValue" in prop else None,
                    writable,
                    index))
            index = index + 1

        index = 0
        for telem in telemetry:
            telemetryObjects.append(
                ModelTelemetryInput(
                    telem["name"],
                    telem["description"] if "description" in telem else None,
                    telem["schemaType"],
                    index))
            index = index + 1

        mutation = iot_createModel(
            self._client, self._debug, name, dtmiSegment, description, propertyObjects, telemetryObjects)
        result = mutation.performMutation()
        return result
