from .query import *
from ..exceptions import *
from ..common import *
from ..data_types.data_store_directory import DataStoreDirectory

class storage_getDataStoreDirectory(Query):

    def __init__(self, client, dataStoreDirectoryId):
        super().__init__(client, "storage_getDataStoreDirectory", DataStoreDirectory)
        if dataStoreDirectoryId is None:
            raise MissingParameterException("Missing dataStoreDirectoryId")
        self.dataStoreDirectoryId = dataStoreDirectoryId
    
    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(dataStoreDirectoryId: "{self.dataStoreDirectoryId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        if(debug):
            print(f"Retrieving directory {self.dataStoreDirectoryId}...")
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self) -> DataStoreDirectory:
        super()._processResult()
        try:
            dir = DataStoreDirectory(self._result['data'][self.queryName], self.client)
            if(debug):
                print(f"Result {dir}")
            return dir
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
