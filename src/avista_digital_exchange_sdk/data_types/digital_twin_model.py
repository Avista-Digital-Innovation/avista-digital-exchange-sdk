from ..exceptions import *
from .. import globals
from .model_property import ModelProperty
from .model_telemetry import ModelTelemetry


class DigitalTwinModel(object):
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
        self.modelId = dict["modelId"]
        self.dtmi = dict["dtmi"]
        self.ownerUserId = dict["ownerUserId"]
        self.displayName = dict["displayName"]
        self.description = dict["description"]
        self.properties = []
        for entry in dict["properties"]:
            self.properties.append(ModelProperty(
                entry, self._client, self._debug))
        self.telemetry = []
        for entry in dict["telemetry"]:
            self.telemetry.append(ModelTelemetry(
                entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}modelId
{tabStr}dtmi
{tabStr}ownerUserId
{tabStr}displayName
{tabStr}description
{tabStr}{f"properties {ModelProperty.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}{f"telemetry {ModelTelemetry.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
