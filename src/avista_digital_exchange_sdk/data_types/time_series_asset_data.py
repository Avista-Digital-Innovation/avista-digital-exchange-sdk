from ..exceptions import *
from .. import globals
from .time_series_asset_attribute import TimeSeriesAssetAttribute


class TimeSeriesAssetData:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""asset: {self.name if self.name is not None else '<unknown>'}
    assetId: {self.assetId}
    attributes: {self.getAttributesString()}
"""

    def getAttributesString(self):
        result = ""
        for entry in self.attributes:
            result += f'{entry}'
        return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.assetId = dict['assetId']
        self.name = dict['name']
        self.attributes = []
        for attribute in dict['attributes']:
            self.attributes.append(
                TimeSeriesAssetAttribute(attribute, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}assetId
{tabStr}name
{tabStr}{f"attributes {TimeSeriesAssetAttribute.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
