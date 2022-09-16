from ..exceptions import *
from .. import globals
from .time_series_asset_attribute import TimeSeriesAssetAttribute


class TimeSeriesAssetData:
    def __init__(self, dict, client):
        self._client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""Asset Data:
    assetId: {self.assetId}
    name: {self.name}
    attributes: {len(self.attributes)} attributes"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.assetId = dict['assetId']
        self.name = dict['name']
        self.attributes = []
        for attribute in dict['attributes']:
            self.attributes.append(
                TimeSeriesAssetAttribute(attribute, self._client))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}assetId
{tabStr}name
{tabStr}{f"attributes {TimeSeriesAssetAttribute.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
