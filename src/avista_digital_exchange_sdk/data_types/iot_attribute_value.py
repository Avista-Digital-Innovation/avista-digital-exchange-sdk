from ..exceptions import *
from .. import globals


class IotAttributeValue:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""attribute value:
    name: {self.name}
    value: {self.value}
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.name = dict['name'] if 'name' in dict else None
        self.schemaType = dict['schemaType'] if 'schemaType' in dict else None
        self.value = dict['value'] if 'value' in dict else None

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}name
{tabStr}value
{tabStr[0:-4]}}} """
