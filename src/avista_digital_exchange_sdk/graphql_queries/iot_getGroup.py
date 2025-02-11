from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_group import IotGroup


class iot_getGroup(Query):

    def __init__(self, client, debug, iotGroupId, includeEndpoints):
        super().__init__(client, debug, "iot_getGroup", IotGroup)
        if iotGroupId is None:
            raise MissingParameterException("Missing iotGroupId")
        
        self.iotGroupId =iotGroupId
        self.includeEndpointsStr = "true" if includeEndpoints else "false"

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(iotGroupId: "{self.iotGroupId}", includeEndpoints: {self.includeEndpointsStr}) {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        print(f'Retrieving iot endpoint {self.iotGroupId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> IotGroup:
        super()._processResult()
        try:
            self.endpoint = IotGroup(
                self._result['data'][self.queryName], self._client, self._debug)
            return self.endpoint
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
        