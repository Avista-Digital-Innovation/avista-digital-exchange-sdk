from ..exceptions import *
from .. import globals


class ModelProperty:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""model property:
    name: {self.name}
    schemaType: {self.schemaType}
    description: {self.description}
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.attributeType = dict['attributeType']
        self.name = dict['name']
        self.description = dict['description']
        self.schemaType = dict['schemaType']
        self.defaultValue = dict['defaultValue']
        self.writable = dict['writable']
        self.index = dict['index']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}name
{tabStr}attributeType
{tabStr}description
{tabStr}schemaType
{tabStr}defaultValue
{tabStr}writable
{tabStr}index
{tabStr[0:-4]}}} """
