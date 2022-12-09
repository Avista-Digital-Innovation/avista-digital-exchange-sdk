from ..exceptions import *
from .. import globals
from .endpoint_property import EndpointProperty
from .endpoint_telemetry import EndpointTelemetry


class IotEndpoint(object):
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    #     def __str__(self):
    #         return f"""endpoint:
    #     name: {self.name}
    #     iotEndpointId: {self.iotEndpointId}
    #     modelId: {self.modelId}
    # """

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.iotEndpointId = dict["iotEndpointId"]
        self.iotHubId = dict["iotHubId"]
        self.modelId = dict["modelId"]
        self.ownerUserId = dict["ownerUserId"]
        self.name = dict["name"]
        self.description = dict["description"]
        self.properties = []
        for entry in dict["properties"]:
            self.properties.append(EndpointProperty(
                entry, self._client, self._debug))
        self.telemetry = []
        for entry in dict["telemetry"]:
            self.telemetry.append(EndpointTelemetry(
                entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}iotEndpointId
{tabStr}iotHubId
{tabStr}modelId
{tabStr}ownerUserId
{tabStr}name
{tabStr}description
{tabStr}{f"properties {EndpointProperty.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}{f"telemetry {EndpointTelemetry.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
