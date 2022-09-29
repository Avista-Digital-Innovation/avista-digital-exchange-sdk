from ..exceptions import *
from .. import globals


class Organization:
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
        self.organizationId = dict['organizationId']
        self.name = dict['name']
        # self.hostOrganization = dict['hostOrganization']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}hostOrganization
{tabStr}name
{tabStr}organizationId 
{tabStr[0:-4]}}} """
