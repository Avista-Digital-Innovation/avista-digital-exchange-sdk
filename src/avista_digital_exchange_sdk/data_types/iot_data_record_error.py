from ..exceptions import *
from .. import globals


class IotDataRecordError:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""IotDataRecordError:
        errorType: {self.errorType}
        errorMessage: {self.errorMessage}
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.errorType = dict['errorType']
        self.errorMessage = dict['errorMessage']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}errorType
{tabStr}errorMessage
{tabStr[0:-4]}}} """
