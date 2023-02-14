from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_endpoint import IotEndpoint


class iot_createEndpoint(Mutation):

    def __init__(self, client, debug, iotHubId, modelId, name, description):
        super().__init__(client, debug, "iot_createEndpoint", IotEndpoint)
        self.iotHubId = iotHubId
        self.modelId = modelId
        self.name = name
        self.description = description

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    iotHubId: "{self.iotHubId}", 
{tabStr}    modelId: "{self.modelId}", 
{tabStr}    name: "{self.name}", 
{tabStr}{'    description: "{self.description}"' if self.description != None else ''}) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print(f"Creating endpoint {self.name}...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = IotEndpoint(
                self._result['data'][self.mutationName], self._client, self._debug)
            print("Create endpoint succeeded")
            return self.response
        except Exception as e:
            raise e
