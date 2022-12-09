from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_endpoint import IotEndpoint
from ..data_types.endpoint_property_input import EndpointPropertyInput


class iot_updateEndpointProperties(Mutation):

    def __init__(self, client, debug, iotEndpointId, properties):
        super().__init__(client, debug, "iot_updateEndpointProperties", IotEndpoint)
        self.iotEndpointId = iotEndpointId
        self.properties = properties

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    iotEndpointId: "{self.iotEndpointId}", 
{tabStr}    properties: [{','.join([property.getMutationParameterString(tabs+1) for property in self.properties])}]) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print(f"Updating properties for endpoint {self.iotEndpointId}...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = IotEndpoint(
                self._result['data'][self.mutationName], self._client, self._debug)
            return self.response
        except Exception as e:
            raise e
