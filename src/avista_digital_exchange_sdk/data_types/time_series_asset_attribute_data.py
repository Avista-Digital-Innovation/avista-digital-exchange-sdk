from ..exceptions import *
from .. import globals


class TimeSeriesAssetAttributeData:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""
   timestamp: {self.timestamp}
   description: {self.value}"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.timestamp = dict['timestamp']
        self.value = dict['value']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}timestamp
{tabStr}value
{tabStr[0:-4]}}} """
