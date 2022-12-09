from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_endpoints_last_values_query_result import IotEndpointsLastValuesQueryResult
import json


class iot_listEndpointLastValues(Query):

    def __init__(self, client, debug, iotEndpointId, clientToken=None, nextToken=None):
        super().__init__(client, debug, "iot_listEndpointLastValues",
                         IotEndpointsLastValuesQueryResult)
        if iotEndpointId is None:
            raise MissingParameterException("Missing iotEndpointId parameter")
        self.iotEndpointId = iotEndpointId
        self.nextToken = nextToken
        self.clientToken = clientToken

    def _getQueryString(self):
        query = f'query {self.queryName} {{ {self.queryName}(iotEndpointId: "{self.iotEndpointId}"'
        if self.nextToken:
            query += f', nextToken: "{self.nextToken}"'
        if self.clientToken:
            query += f', clientToken: "{self._clientToken}"'
        query += f') {self.resultType.getQueryString()} }}'
        return query

    def performQuery(self) -> str:
        print(
            f'Listing last values for telemetry of endpoint {self.iotEndpointId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> IotEndpointsLastValuesQueryResult:
        super()._processResult()
        try:
            self.result = IotEndpointsLastValuesQueryResult(
                self._result['data'][self.queryName], self._client, self._debug)
            print(f'{self.result}')
            return self.result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
