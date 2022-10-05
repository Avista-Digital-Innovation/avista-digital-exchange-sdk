from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.data_store_file import DataStoreFile


class storage_getDataStoreFile(Query):

    def __init__(self, client, debug, dataStoreFileId):
        super().__init__(client, debug, "storage_getDataStoreFile", DataStoreFile)
        if dataStoreFileId is None:
            raise MissingParameterException("Missing dataStoreFileId")
        self.dataStoreFileId = dataStoreFileId

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(dataStoreFileId: "{self.dataStoreFileId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        if self._debug:
            print(f"DEBUG - Retrieving file {self.dataStoreFileId}...")
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> DataStoreFile:
        super()._processResult()
        try:
            result = DataStoreFile(
                self._result['data'][self.queryName], self._client, self._debug)
            return result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
