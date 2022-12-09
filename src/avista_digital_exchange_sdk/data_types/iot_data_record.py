from ..exceptions import *
from .. import globals
from .iot_attribute_value import IotAttributeValue


class IotDataRecord:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""DataRecord:
    iotEndpointId: {self.iotEndpointId}
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.iotEndpointId = dict['iotEndpointId']
        self.timestamp = dict['timestamp']
        self.attributes = []
        for attribute in dict['attributes']:
            self.attributes.append(
                IotAttributeValue(attribute, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}iotEndpointId
{tabStr}timestamp
{tabStr}{f"attributes {IotAttributeValue.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
