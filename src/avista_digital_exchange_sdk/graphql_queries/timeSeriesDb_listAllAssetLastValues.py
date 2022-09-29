from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.time_series_assets_and_last_values_result import TimeSeriesAssetsAndLastValuesResult
import json


class timeSeriesDb_listAllAssetLastValues(Query):

    def __init__(self, client, debug, timeSeriesDbId, clientToken=None, nextToken=None):
        super().__init__(client, debug, "timeSeriesDb_listAllAssetLastValues",
                         TimeSeriesAssetsAndLastValuesResult)
        if timeSeriesDbId is None:
            raise MissingParameterException("Missing timeSeriesDbId parameter")
        self.timeSeriesDbId = timeSeriesDbId
        self.nextToken = nextToken
        self.clientToken = clientToken

    def _getQueryString(self):
        query = f'query {self.queryName} {{ {self.queryName}(timeSeriesDbId: "{self.timeSeriesDbId}"'
        if self.nextToken:
            query += f', nextToken: "{self.nextToken}"'
        if self.clientToken:
            query += f', clientToken: "{self._clientToken}"'
        query += f') {self.resultType.getQueryString()} }}'
        return query

    def performQuery(self) -> str:
        print(
            f'Listing assets and attributes in time series db {self.timeSeriesDbId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> TimeSeriesAssetsAndLastValuesResult:
        super()._processResult()
        try:
            self.result = TimeSeriesAssetsAndLastValuesResult(
                self._result['data'][self.queryName], self.timeSeriesDbId, self._client, self._debug)
            print(f'{self.result}')
            return self.result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
