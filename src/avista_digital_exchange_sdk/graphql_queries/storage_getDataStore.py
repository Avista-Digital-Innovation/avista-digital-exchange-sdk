from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.data_store import DataStore


class storage_getDataStore(Query):

    def __init__(self, client, debug, dataStoreId):
        super().__init__(client, debug, "storage_getDataStore", DataStore)
        if dataStoreId is None:
            raise MissingParameterException("Missing dataStoreId")
        self.dataStoreId = dataStoreId

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(dataStoreId: "{self.dataStoreId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        print(f'Retrieving data store {self.dataStoreId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> DataStore:
        super()._processResult()
        try:
            self.dataStore = DataStore(
                self._result['data'][self.queryName], self._client, self._debug)
            return self.dataStore
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
