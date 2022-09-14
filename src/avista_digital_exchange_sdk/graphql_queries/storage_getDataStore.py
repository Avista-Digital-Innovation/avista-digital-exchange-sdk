from .query import *
from ..exceptions import *
from ..common import *
from ..data_types.data_store import DataStore

class storage_getDataStore(Query):

    def __init__(self, client, dataStoreId):
        super().__init__(client, "storage_getDataStore", DataStore)
        if dataStoreId is None:
            raise MissingParameterException("Missing dataStoreId")
        self.dataStoreId = dataStoreId
    
    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(dataStoreId: "{self.dataStoreId}") {self.resultType.getQueryString()} }}'


    def performQuery(self) -> str:
        if debug:
            print(f'Retrieving data store {self.dataStoreId}')
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self) -> DataStore:
        super()._processResult()
        try:
            self.dataStore = DataStore(self._result['data'][self.queryName], self.client)
            if debug:
                print(f'Result {self.dataStore}')
            return self.dataStore
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
