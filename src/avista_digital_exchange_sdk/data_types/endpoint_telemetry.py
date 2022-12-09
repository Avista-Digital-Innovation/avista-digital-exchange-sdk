from ..exceptions import *
from .. import globals


class EndpointTelemetry:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    #     def __str__(self):
    #         return f"""telemetry:
    #     name: {self.name}
    #     type: {self.schemaType}
    # """

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.attributeType = dict['attributeType']
        self.name = dict['name']
        self.description = dict['description']
        self.schemaType = dict['schemaType']
        self.index = dict['index']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}name
{tabStr}attributeType
{tabStr}description
{tabStr}schemaType
{tabStr}index
{tabStr[0:-4]}}} """
