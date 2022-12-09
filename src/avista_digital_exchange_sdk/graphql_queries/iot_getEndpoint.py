from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_endpoint import IotEndpoint


class iot_getEndpoint(Query):

    def __init__(self, client, debug, iotEndpointId):
        super().__init__(client, debug, "iot_getEndpoint", IotEndpoint)
        if iotEndpointId is None:
            raise MissingParameterException("Missing iotEndpointId")
        self.iotEndpointId = iotEndpointId

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(iotEndpointId: "{self.iotEndpointId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        print(f'Retrieving iot endpoint {self.iotEndpointId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> IotEndpoint:
        super()._processResult()
        try:
            self.endpoint = IotEndpoint(
                self._result['data'][self.queryName], self._client, self._debug)
            return self.endpoint
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
