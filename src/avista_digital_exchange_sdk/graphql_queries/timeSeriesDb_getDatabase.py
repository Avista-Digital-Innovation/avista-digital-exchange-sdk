from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.time_series_db import TimeSeriesDb


class timeSeriesDb_getDatabase(Query):

    def __init__(self, client, debug, timeSeriesDbId):
        super().__init__(client, debug, "timeSeriesDb_getDatabase", TimeSeriesDb)
        if timeSeriesDbId is None:
            raise MissingParameterException("Missing timeSeriesDbId")
        self.timeSeriesDbId = timeSeriesDbId

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(timeSeriesDbId: "{self.timeSeriesDbId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        print(f'Retrieving time series db {self.timeSeriesDbId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> TimeSeriesDb:
        super()._processResult()
        try:
            self.database = TimeSeriesDb(
                self._result['data'][self.queryName], self._client, self._debug)
            print(f'{self.database}')
            return self.database
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
