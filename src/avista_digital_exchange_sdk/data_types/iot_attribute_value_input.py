from ..exceptions import *
from .. import globals


class IotAttributeValueInput:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        return

    def getMutationParameterString(self, tabs):
        tabStr = globals.getTabStr(tabs)
        result = f""" {{
{tabStr}name: "{self.name}",
{tabStr}value: "{self.value}"
{tabStr[0:-4]}}} """
        return result
