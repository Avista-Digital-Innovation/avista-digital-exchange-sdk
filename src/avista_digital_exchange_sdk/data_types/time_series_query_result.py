from ..exceptions import *
from .. import globals
import json


class TimeSeriesQueryResult:
    def __init__(self, dict, client, debug, timeSeriesDbId, maxRows):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)
        self.timeSeriesDbId = timeSeriesDbId
        self.maxRows = maxRows

    def __str__(self):
        return f"""Query Result:
    clientToken: {self.clientToken}
    nextToken: {self.nextToken}"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException

        self.queryProgressPercentage = dict["queryProgressPercentage"]
        self.clientToken = dict["clientToken"]
        self.nextToken = dict["nextToken"]
        self.queryString = dict["queryString"]
        self.queryId = dict["queryId"]
        self.presignedUrl = dict["presignedUrl"]
        self.resultChunkIndex = dict["resultChunkIndex"]

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}queryProgressPercentage
{tabStr}clientToken
{tabStr}nextToken
{tabStr}queryString
{tabStr}queryId
{tabStr}presignedUrl
{tabStr}resultChunkIndex
{tabStr[0:-4]}}} """
