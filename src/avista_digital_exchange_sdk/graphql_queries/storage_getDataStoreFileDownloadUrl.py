from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.presigned_url import PresignedUrl
from ..data_types.service import Service


class storage_getDataStoreFileDownloadUrl(Query):

    def __init__(self, client, debug, dataStoreId, dataStoreFileId):
        super().__init__(client, debug, "storage_getDataStoreFileDownloadUrl", PresignedUrl)
        if dataStoreId is None:
            raise MissingParameterException("Missing parameter dataStoreId")
        if dataStoreFileId is None:
            raise MissingParameterException(
                "Missing parameter dataStoreFileId")
        self.dataStoreId = dataStoreId
        self.dataStoreFileId = dataStoreFileId

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(dataStoreFileId: "{self.dataStoreFileId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        print('Retrieving file download url...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> PresignedUrl:
        super()._processResult()
        try:
            return PresignedUrl(self._result['data'][self.queryName], self._client, self._debug)
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
