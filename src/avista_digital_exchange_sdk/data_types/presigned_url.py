from ..exceptions import *
from .. import globals


class PresignedUrl:

    def __init__(self, dict, client):
        self._client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.url = dict['url']
        self.uploadId = dict['uploadId']
        self.itemId = dict['itemId']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}url
{tabStr}uploadId
{tabStr}itemId
{tabStr[0:-4]}}} """
