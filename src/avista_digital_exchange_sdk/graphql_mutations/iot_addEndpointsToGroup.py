from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_group import IotGroup


class iot_addEndpointsToGroup(Mutation):

    def __init__(self, client, debug, iotGroupId, iotEndpointIds):
        super().__init__(client, debug, "iot_addEndpointsToGroup", IotGroup)
        self.iotGroupId = iotGroupId
        self.iotEndpointIds = iotEndpointIds

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        temp = "{\n         iotGroupId}"
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    iotGroupId: "{self.iotGroupId}", 
{tabStr}    iotEndpointIds: ["{'","'.join(self.iotEndpointIds)}"] ) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = IotGroup(
                self._result['data'][self.mutationName], self._client, self._debug)
            print("Publish succeeded")
            return self.response
        except Exception as e:
            raise e
