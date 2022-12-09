from ..exceptions import *
from .. import globals
import json


class IotGenerateQueryResultExport:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException

        self.queryId = dict["queryId"]
        self.fileFormat = dict["fileFormat"]

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}queryId
{tabStr}fileFormat
{tabStr[0:-4]}}} """
