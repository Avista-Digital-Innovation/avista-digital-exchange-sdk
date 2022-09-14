from .query import *
from ..exceptions import *
from ..common import *
from ..data_types.time_series_db import TimeSeriesDb
from ..data_types.service import Service

class timeSeriesDb_listDatabases(Query):

    def __init__(self, client):
        super().__init__(client, "timeSeriesDb_listDatabases", TimeSeriesDb)
    
    def _getQueryString(self):
        return super()._getQueryString()

    def performQuery(self) -> str:
        if debug:
            print('Retrieving your time series databases...')
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self):
        super()._processResult()
        try:
            self.databases = []
            print('Your databases:')
            for currentDatabase in self._result['data'][self.queryName]:
                self.databases.append(TimeSeriesDb(currentDatabase, self.client))
            i = 0
            for database in self.databases:
                print(f'{i}: {database}')
                i += 1
            return self.databases
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
