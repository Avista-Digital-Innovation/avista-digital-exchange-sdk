from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.data_store import DataStore
from ..data_types.service import Service


class storage_listDataStores(Query):

    def __init__(self, client, debug):
        super().__init__(client, debug, "storage_listDataStores", DataStore)

    def _getQueryString(self):
        return super()._getQueryString()

    def performQuery(self) -> str:
        print('Listing your data stores...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.dataStores = []

            for currentDataStore in self._result['data'][self.queryName]:
                self.dataStores.append(
                    DataStore(currentDataStore, self._client, self._debug))
            i = 0

            for dataStore in self.dataStores:
                print(f'{i}: {dataStore}')
                i += 1
            return self.dataStores
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
