
from .time_series_asset_data import TimeSeriesAssetData

from ..exceptions import *
from .. import globals
import json


class TimeSeriesAssetsAndLastValuesResult:
    def __init__(self, dict, client, debug, timeSeriesDbId):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)
        self.timeSeriesDbId = timeSeriesDbId

    def __str__(self):
        return f"""Query Progress Percentage: {self.queryProgressPercentage}
clientToken: {self.clientToken}
nextToken: {self.nextToken}
queryId: {self.queryId}
assets: 
{self.getDataString()}
"""

    def getDataString(self):
        result = ""
        for entry in self.data:
            result += f'{entry}'
        return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.queryProgressPercentage = dict["queryProgressPercentage"]
        self.clientToken = dict["clientToken"]
        self.nextToken = dict["nextToken"] if "nextToken" in dict else None
        self.queryId = dict["queryId"]
        self.resultChunkIndex = dict["resultChunkIndex"]
        self.data = []
        for i in range(0, len(dict["data"])):
            self.data.append(TimeSeriesAssetData(dict["data"][i],
                                                 self._client,
                                                 self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}queryProgressPercentage
{tabStr}clientToken
{tabStr}nextToken
{tabStr}queryId
{tabStr}resultChunkIndex
{tabStr}resultChunkIndex
{tabStr}{f"data {TimeSeriesAssetData.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
