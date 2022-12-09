from .data_types.service import Service
from .data_types.data_store_directory import DataStoreDirectory
from .data_types.data_store_file import DataStoreFile
from .data_types.data_store import DataStore
from .graphql_mutations.storage_deleteDataStoreFile import storage_deleteDataStoreFile
from .graphql_mutations.storage_createDataStoreFile import storage_createDataStoreFile
from .graphql_queries.storage_getDataStoreDirectory import storage_getDataStoreDirectory
from .graphql_queries.storage_getDataStoreFile import storage_getDataStoreFile
from .graphql_queries.storage_getDataStore import storage_getDataStore
from .graphql_queries.storage_listDataStores import storage_listDataStores

import time
import signal


class DataStoreUtil(object):

    def __init__(self, debug, client):
        self._debug = debug
        self._client = client

    def listDataStores(self):
        """Lists the Data Stores belonging to the user"""
        query = storage_listDataStores(self._client, self._debug)
        result = query.performQuery()
        return result

    def getDataStore(self, dataStoreId) -> DataStore:
        """Retrieves the Data Store's metadata by dataStoreId"""
        query = storage_getDataStore(self._client, self._debug, dataStoreId)
        result = query.performQuery()
        return result

    def getDataStoreDirectory(self, dataStoreDirectoryId) -> DataStoreDirectory:
        """Retrieves a Data Store directory and it's contents by dataStoreDirectoryId"""
        return DataStoreDirectory.getDirectory(self._client, self._debug, dataStoreDirectoryId)

    def getDataStoreFileMeta(self, dataStoreFileId) -> DataStoreFile:
        """Retrieves a Data Store file's metadata by dataStoreFileId"""
        return DataStoreFile.getDataStoreFile(self._client, self._debug, dataStoreFileId)

    def downloadDataStoreFile(self, dataStoreFileId, writeLocation) -> DataStoreFile:
        """Retrieves a Data Store file's metadata and downloads and writes the file to the local file system"""
        return DataStoreFile.downloadDataStoreFile(self._client, self._debug, dataStoreFileId, writeLocation)

    def uploadFileToDataStore(self, dataStoreId, dataStoreDirectoryId, localFilePath, name=None, description=None) -> DataStoreFile:
        """Copies a local file to the Data Store and is placed in the directory matching dataStoreDirectoryId"""

        return DataStoreFile.createAndUploadFile(self._client,
                                                 self._debug, localFilePath, dataStoreId, dataStoreDirectoryId, name, description)

    def deleteDataStoreFile(self, dataStoreFileId) -> DataStoreFile:
        """Deletes the file from the Data Store"""
        return DataStoreFile.deleteDataStoreFile(self._client, self._debug, dataStoreFileId)
