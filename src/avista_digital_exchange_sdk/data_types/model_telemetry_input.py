from ..exceptions import *
from .. import globals


class ModelTelemetryInput:
    def __init__(self, name, description, schemaType, index):
        self.name = name
        self.description = description
        self.schemaType = schemaType
        self.index = index
        return

    def getMutationParameterString(self, tabs):
        tabStr = globals.getTabStr(tabs)
        result = f""" {{
{tabStr}name: "{self.name}",
{tabStr}{f'description: "{self.description}",' if self.description != None else ""}
{tabStr}schemaType: {self.schemaType},
{tabStr}index: {self.index}
{tabStr[0:-4]}}} """
        return result

    @staticmethod
    def checkDictForCorrectFields(dict):
        if "name" not in dict:
            raise InvalidParameterException(
                "Model telemetry entry is missing 'name'")
        if "schemaType" not in dict:
            raise InvalidParameterException(
                "Model telemetry entry is missing 'schemaType'")
        return True
