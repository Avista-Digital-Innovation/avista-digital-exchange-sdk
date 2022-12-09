from ..exceptions import *
from .. import globals


class EndpointPropertyInput:
    def __init__(self, name, value, timestamp):
        self.name = name
        self.value = value
        self.timestamp = timestamp
        return

    def getMutationParameterString(self, tabs):
        tabStr = globals.getTabStr(tabs)
        result = f""" {{
{tabStr}name: "{self.name}",
{tabStr}value: "{self.value}",
{tabStr}timestamp: "{self.timestamp}"
{tabStr[0:-4]}}} """
        return result

    @staticmethod
    def checkDictForCorrectFields(dict):
        if "name" not in dict:
            raise InvalidParameterException(
                "Endpoint property entry is missing 'name'")
        if "value" not in dict:
            raise InvalidParameterException(
                "Endpoint property entry is missing 'value'")
        if "timestamp" not in dict:
            raise InvalidParameterException(
                "Endpoint property entry is missing 'timestamp'")
        return True
