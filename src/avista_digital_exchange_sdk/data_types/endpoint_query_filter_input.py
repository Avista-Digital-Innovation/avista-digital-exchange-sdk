from ..exceptions import *
from .. import globals


class EndpointQueryFilterInput:
    def __init__(self, iotEndpointId, attributeNames):
        self.iotEndpointId = iotEndpointId
        self.attributeNames = attributeNames
        return

    def getMutationParameterString(self, tabs):
        tabStr = globals.getTabStr(tabs)
        result = f""" {{
{tabStr}iotEndpointId: "{self.iotEndpointId}",
{tabStr}attributeNames: ["""
        for index, name in enumerate(self.attributeNames):
            result += f'''"{name}"'''
            if index < len(self.attributeNames) - 1:
                result += ', '
        result += f"""]
{tabStr[0:-4]}}} """
        return result
