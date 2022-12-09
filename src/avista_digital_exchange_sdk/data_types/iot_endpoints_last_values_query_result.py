
from ..exceptions import *
from .. import globals
from .endpoint_last_values import EndpointLastValues
from .endpoint_telemetry_data_record import EndpointTelemetryDataRecord


class IotEndpointsLastValuesQueryResult:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    # def __str__(self):
    #     #     result = f"""Endpoint last values:"""
    #     # # Record: iotEndpointId: {self.record.iotEndpointId} timestamp: {self.record.timestamp} ({self.record.timeUnit})
    #     # # Errors:"""
    #     # #     for error in self.errors:
    #     # #         result += f"""
    #     # #     - {error.message}"""
    #     #     return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException

        self.clientToken = dict['clientToken']
        self.nextToken = dict['nextToken']
        self.queryId = dict['queryId']
        self.resultChunkIndex = dict['resultChunkIndex']

        self.resultStoredInS3 = dict['resultStoredInS3']
        self.presignedUrl = dict['presignedUrl']
        self.data = []
        for entry in dict["data"]:
            self.data.append(EndpointLastValues(
                entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{ 
{tabStr}clientToken
{tabStr}nextToken
{tabStr}queryId
{tabStr}resultChunkIndex
{tabStr}resultStoredInS3
{tabStr}presignedUrl
{tabStr}{f"data {EndpointLastValues.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
