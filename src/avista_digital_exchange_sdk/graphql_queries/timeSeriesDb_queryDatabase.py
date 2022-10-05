from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.time_series_query_result import TimeSeriesQueryResult
import json


class timeSeriesDb_queryDatabase(Query):

    def __init__(self, client, debug, timeSeriesDbId, assetsArray, startTime, endTime, maxRows=None, nextToken=None, clientToken=None, queryString=None):
        super().__init__(client, debug, "timeSeriesDb_queryDatabase",
                         TimeSeriesQueryResult)

        self.timeSeriesDbId = timeSeriesDbId
        self.assetsArray = assetsArray
        self.maxRows = maxRows

        if not isValidTimestampFormat(startTime):
            raise InvalidTimestampParameter("startTime", startTime)
        self.startTime = startTime
        if not isValidTimestampFormat(endTime):
            raise InvalidTimestampParameter("endTime", endTime)
        self.endTime = endTime

        self.queryString = queryString
        self.nextToken = nextToken
        self.clientToken = clientToken

        if self.nextToken is not None:
            self.queryType = "NEXT_TOKEN"
        else:
            self.queryType = "TIME_PERIOD"

    def getAttributeNamesListString(self, attributeNamesArray):

        result = f'"{attributeNamesArray[0]}"'
        for i in range(1, len(attributeNamesArray)):
            result += f', "{attributeNamesArray[i]}"'
        return result

    def _getQueryString(self):
        assetsArrayString = "["
        i = 0
        for entry in self.assetsArray:
            assetsArrayString += f'{{assetId: "{entry["assetId"]}", attributeNamesFilter: [{self.getAttributeNamesListString(entry["attributeNames"])}]}}'
            i += 1
            if i >= len(self.assetsArray):
                assetsArrayString += ','

        assetsArrayString += "]"

        query = f'''query {self.queryName} {{ {self.queryName}
            (timeSeriesDbId: "{self.timeSeriesDbId}", 
             queryType: TIME_PERIOD, 
             startTime: "{self.startTime}", 
             endTime: "{self.endTime}", 
             assets: {assetsArrayString}'''
        if self.maxRows:
            query += f', maxRows: {self.maxRows}'
        if self.nextToken:
            query += f', nextToken: "{self.nextToken}"'
        if self.queryString:
            query += f', queryString: {json.dumps(self.queryString)}'
        if self.clientToken:
            query += f', clientToken: "{self.clientToken}"'
        query += f') {self.resultType.getQueryString()} }}'
        return query

    def performQuery(self) -> str:
        print(f'Querying database {self.timeSeriesDbId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> TimeSeriesQueryResult:
        super()._processResult()
        try:
            self.result = TimeSeriesQueryResult(
                self._result['data'][self.queryName], self._client, self._debug, self.timeSeriesDbId, self.maxRows)
            return self.result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")


def isValidTimestampFormat(timestamp):
    return True
