from ..exceptions import *
from ..common import *
import json

class QueryResult_TimestreamVariables:
    def __init__(self, dict, client, timeSeriesDbId, queryString, maxRows):
        self.client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)
        self.timeSeriesDbId = timeSeriesDbId
        self.queryString = queryString
        self.maxRows = maxRows

    def __str__(self):
        return f"""Query Status: {self.QueryStatus}
clientToken: {self.clientToken}
NextToken: {self.NextToken}
Column info: {self.ColumnInfo}
Data rows: {self.Rows}
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.timestreamResultsJSONString = dict["resultJSONString"]
        self.clientToken = dict["clientToken"]
        self.timestreamResults = json.loads(self.timestreamResultsJSONString)
        self.QueryId = self.timestreamResults["QueryId"]
        self.QueryStatus = self.timestreamResults["QueryStatus"]
        self.Rows = self.timestreamResults["Rows"]
        self.ColumnInfo = self.timestreamResults["ColumnInfo"]
        self.NextToken = self.timestreamResults["NextToken"] if "NextToken" in self.timestreamResults else None

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}resultJSONString
{tabStr}clientToken
{tabStr[0:-4]}}} """

    def method(self):
        # TODO
        return