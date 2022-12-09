from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_query_by_time_range_result import IotQueryByTimeRangeResult
import json


class iot_queryByTimeRange(Query):

    def __init__(self, client, debug, endpointQueryFilters, startTime, endTime, nextToken=None, clientToken=None, queryString=None, queryId=None):
        super().__init__(client, debug, "iot_queryByTimeRange",
                         IotQueryByTimeRangeResult)

        self.endpointQueryFilters = endpointQueryFilters

        self.startTime = f'{startTime}'
        self.endTime = f'{endTime}'

        self.queryString = queryString
        self.nextToken = nextToken
        self.clientToken = clientToken
        self.queryId = queryId

    def getAttributeNamesListString(self, attributeNamesArray):

        result = f'"{attributeNamesArray[0]}"'
        for i in range(1, len(attributeNamesArray)):
            result += f', "{attributeNamesArray[i]}"'
        return result

    def _getQueryString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        endpointFilterQueryString = ""
        for entry in self.endpointQueryFilters:
            endpointFilterQueryString += entry.getMutationParameterString(
                tabs + 1)
        query = f'''query {self.queryName} {{ {self.queryName} ( endpointQueryFilters: [{endpointFilterQueryString}], 
    startTime: "{self.startTime}", 
    endTime: "{self.endTime}"'''
        if self.nextToken:
            query += f', nextToken: "{self.nextToken}"'
        if self.queryString:
            query += f', queryString: {json.dumps(self.queryString)}'
        if self.clientToken:
            query += f', clientToken: "{self.clientToken}"'
        if self.clientToken:
            query += f', queryId: "{self.queryId}"'
        query += f') {self.resultType.getQueryString()} }}'
        return query

    def performQuery(self) -> str:
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> IotQueryByTimeRangeResult:
        super()._processResult()
        try:
            self.result = IotQueryByTimeRangeResult(
                self._result['data'][self.queryName], self._client, self._debug)
            return self.result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
