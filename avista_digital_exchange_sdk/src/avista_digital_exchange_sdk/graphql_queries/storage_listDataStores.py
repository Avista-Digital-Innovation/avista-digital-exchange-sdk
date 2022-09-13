from .query import *
from ..exceptions import *
from ..common import *
from ..data_types.data_store import DataStore
from ..data_types.service import Service

class storage_listDataStores(Query):

    def __init__(self, client):
        super().__init__(client, "storage_listDataStores", DataStore)
    
    def _getQueryString(self):
        return super()._getQueryString()

    def performQuery(self) -> str:
        if debug:
            print('Retrieving your data stores...')
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self):
        super()._processResult()
        try:
            self.dataStores = []
            print('Your data stores:')
            for currentDataStore in self._result['data'][self.queryName]:
                self.dataStores.append(DataStore(currentDataStore, self.client))
            i = 0
            for dataStore in self.dataStores:
                print(f'{i}: {dataStore}')
                i += 1
            return self.dataStores
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
