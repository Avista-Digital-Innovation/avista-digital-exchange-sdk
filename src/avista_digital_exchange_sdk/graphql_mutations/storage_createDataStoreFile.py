from .mutation import *
from ..exceptions import *
from ..common import *
from ..data_types.presigned_url import PresignedUrl

class storage_createDataStoreFile(Mutation):

    def __init__(self, client, dataStoreId, dataStoreDirectoryId, name, fileExtension, description = None):
        super().__init__(client, "storage_createDataStoreFile", PresignedUrl)
        self.dataStoreDirectoryId = dataStoreDirectoryId
        self.dataStoreId = dataStoreId
        self.name = name
        self.fileExtension = fileExtension
        self.description = description
    
    def _getMutationString(self):
        return f"""mutation {self.mutationName} {{ {self.mutationName}(dataStoreDirectoryId: "{self.dataStoreDirectoryId}", dataStoreId: "{self.dataStoreId}", name: "{self.name}", fileExtension: "{self.fileExtension}" {f', description: "{self.description}"' if self.description is not None else ''}) {self.resultType.getQueryString()} }}"""

    def performMutation(self):
        if debug:
            print("Creating data store file...")
        self._result = self.client.performMutation(self._getMutationString())
        return self._processResult()
    
    def _processResult(self):
        super()._processResult()
        try:
            self.presignedUrl = PresignedUrl(self._result['data'][self.mutationName], self.client)
            if debug:
                print("received upload endpoint for file...")
            return self.presignedUrl
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of mutation {self.mutationName}")
