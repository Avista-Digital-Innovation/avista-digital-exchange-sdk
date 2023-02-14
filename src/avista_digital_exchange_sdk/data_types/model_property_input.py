from ..exceptions import *
from .. import globals


class ModelPropertyInput:

    def __init__(self, name, description, schemaType, defaultValue, writable, index):
        self.name = name
        self.description = description
        self.schemaType = schemaType
        self.defaultValue = defaultValue
        self.writable = writable
        self.index = index
        return

    def getMutationParameterString(self, tabs):
        tabStr = globals.getTabStr(tabs)
        result = f""" {{
{tabStr}name: "{self.name}",
{tabStr}{f'description: "{self.description}",' if self.description and self.description != None  else ""}
{tabStr}schemaType: {self.schemaType},
{tabStr}{f'defaultValue: "{self.defaultValue}",' if self.defaultValue and self.defaultValue != None else ""}
{tabStr}{f'writable: {self.writable},' if self.writable and self.writable != None else ""}
{tabStr}index: {self.index}
{tabStr[0:-4]}}} """
        return result

    @staticmethod
    def checkDictForCorrectFields(dict):
        if "name" not in dict:
            raise InvalidParameterException(
                "Model property entry is missing 'name'")
        if "schemaType" not in dict:
            raise InvalidParameterException(
                "Model property entry is missing 'schemaType'")
        elif dict["schemaType"] not in ['integer', 'double', 'string', 'boolean', 'dateTime', 'duration']:
            raise InvalidParameterException(
                f"""Property '{dict["name"]}' has invalid schemaType. Accepted values: ['integer', 'double', 'string', 'boolean', 'dateTime, 'duration']""")
        if "writable" in dict and type(dict["writable"]) is not bool:
            raise InvalidParameterException(
                "Model property 'writable' must be a boolean value")
        return True
