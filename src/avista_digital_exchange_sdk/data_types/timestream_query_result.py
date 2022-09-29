from ..exceptions import *
from .. import globals
import json


class QueryResult_TimestreamVariables:
    def __init__(self, dict, client, debug, timeSeriesDbId, queryString, maxRows):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)
        self.timeSeriesDbId = timeSeriesDbId
        self.queryString = queryString
        self.maxRows = maxRows

    def __str__(self):
        return f"""Query Result
    clientToken: {self.clientToken}
    nextToken: {self.nextToken}
    columnInfo: {len(self.columnInfo)} columns
    dataRows: {len(self.dataRows)} data rows
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.timestreamResultsJSONString = dict["resultJSONString"]
        self.clientToken = dict["clientToken"]
        self.timestreamResults = json.loads(self.timestreamResultsJSONString)
        self.queryId = self.timestreamResults["QueryId"]
        self.queryStatus = self.timestreamResults["QueryStatus"]
        self.rows = self.timestreamResults["Rows"]
        self.dataRows = self.rows
        self.columnInfo = self.timestreamResults["ColumnInfo"]
        self.nextToken = self.timestreamResults["NextToken"] if "NextToken" in self.timestreamResults else None

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}resultJSONString
{tabStr}clientToken
{tabStr[0:-4]}}} """
