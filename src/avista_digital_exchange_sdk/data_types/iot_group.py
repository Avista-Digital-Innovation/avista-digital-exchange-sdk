from ..exceptions import *
from .. import globals
from .iot_endpoint import IotEndpoint


class IotGroup(object):
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.iotGroupId = dict["iotGroupId"]
        self.iotHubId = dict["iotHubId"]
        self.ownerUserId = dict["ownerUserId"]
        self.name = dict["name"]
        self.description = dict["description"]
        self.endpoints = []
        for entry in dict["endpoints"]:
            self.endpoints.append(IotEndpoint(
                entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}iotGroupId
{tabStr}iotHubId
{tabStr}ownerUserId
{tabStr}name
{tabStr}description
{tabStr}{f"endpoints {IotEndpoint.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
