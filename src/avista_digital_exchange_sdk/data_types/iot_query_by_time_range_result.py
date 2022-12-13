
from ..exceptions import *
from .. import globals
from .endpoint_last_values import EndpointLastValues
from .iot_endpoint_data import IotEndpointData


class IotQueryByTimeRangeResult:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    # def __str__(self):
    #     result = f"""Endpoint last values:"""
    # # Record: iotEndpointId: {self.record.iotEndpointId} timestamp: {self.record.timestamp} ({self.record.timeUnit})
    # # Errors:"""
    # #     for error in self.errors:
    # #         result += f"""
    # #     - {error.message}"""
    #     return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        if self._debug:
            print(dict)
        self.clientToken = dict['clientToken']
        self.nextToken = dict['nextToken'] if 'nextToken' in dict else None
        self.queryId = dict['queryId']
        self.resultChunkIndex = dict['resultChunkIndex']
        self.presignedUrl = dict['presignedUrl']
        self.queryString = dict['queryString']
        # self.data = []
        # if "data" in dict and dict["data"] != None:
        #     for entry in dict["data"]:
        #         self.data.append(IotEndpointData(
        #             entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{ 
{tabStr}clientToken
{tabStr}nextToken
{tabStr}queryId
{tabStr}resultChunkIndex
{tabStr}presignedUrl
{tabStr}queryString
{tabStr[0:-4]}}} """
# {tabStr}{f"data {IotEndpointData.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
# {tabStr[0:-4]}}} """
