from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.data_store_file import DataStoreFile


class storage_deleteDataStoreFile(Mutation):

    def __init__(self, client, debug, dataStoreFileId):
        super().__init__(client, debug, "storage_deleteDataStoreFile", DataStoreFile)
        self.dataStoreFileId = dataStoreFileId

    def _getMutationString(self):
        return f"""mutation {self.mutationName} {{ {self.mutationName}(dataStoreFileId: "{self.dataStoreFileId}") {self.resultType.getQueryString()} }}"""

    def performMutation(self):
        print(
            f"Deleting file {self.dataStoreFileId}...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.result = DataStoreFile(
                self._result['data'][self.mutationName], self._client, self._debug)
            print(f"File deleted")
            return self.result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of mutation {self.mutationName}")
