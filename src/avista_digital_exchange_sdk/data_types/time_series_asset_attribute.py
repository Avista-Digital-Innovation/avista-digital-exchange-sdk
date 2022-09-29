from ..exceptions import *
from .. import globals
from .time_series_asset_attribute_data import TimeSeriesAssetAttributeData


class TimeSeriesAssetAttribute:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""
        {self.name}
            attributeType: {self.attributeType}
            lastValue: {self.lastValue}
            lastValueTime: {self.lastValueTime}"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.attributeType = dict['attributeType']
        self.lastValue = dict['lastValue']
        self.lastValueTime = dict['lastValueTime']
        self.name = dict['name']
        self.data = []
        for entry in dict['data']:
            self.data.append(TimeSeriesAssetAttributeData(
                entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}attributeType
{tabStr}lastValue
{tabStr}lastValueTime
{tabStr}name
{tabStr}{f"data {TimeSeriesAssetAttributeData.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
