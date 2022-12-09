from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_data_record_input import IotDataRecordInput
from ..data_types.publish_iot_data_result import PublishIotDataResult


class iot_publish(Mutation):

    def __init__(self, client, debug, iotEndpointId, data):
        super().__init__(client, debug, "iot_publish", PublishIotDataResult)
        self.iotEndpointId = iotEndpointId
        self.data = data

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    iotEndpointId: "{self.iotEndpointId}", 
{tabStr}    data: [{','.join([record.getMutationParameterString(tabs+1) for record in self.data])}]) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print(f"Publishing data to endpoint {self.iotEndpointId}...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = PublishIotDataResult(
                self._result['data'][self.mutationName], self._client, self._debug)
            print("Publish succeeded")
            return self.response
        except Exception as e:
            raise e
