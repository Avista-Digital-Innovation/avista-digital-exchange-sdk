from ..exceptions import *
from .. import globals


class DataStoreObject:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionaryRoot(dict)

    def buildFromDictionaryRoot(self, dict):
        # from .data_store_file import DataStoreFile
        # from .data_store_directory import DataStoreDirectory

        if dict is None:
            raise MissingDataInResultException
        if 'objectType' in dict:
            self.objectType = dict['objectType']
            if self.objectType == "FILE":
                # DataStoreFile(dict['dataStoreFile'], self._client, self._debug)
                self.dataStoreFile = dict['dataStoreFile']
            elif self.objectType == "DIRECTORY":
                # DataStoreDirectory(dict['dataStoreDirectory'], self._client, self._debug)
                self.dataStoreDirectory = dict['dataStoreDirectory']
        elif 'dataStoreDirectoryId' in dict:
            self.objectType = "DIRECTORY"
        elif 'dataStoreFileId' in dict:
            self.objectType = "FILE"
        else:
            raise ServiceTypeNotAvailable

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        from .data_store_file import DataStoreFile
        from .data_store_directory import DataStoreDirectory
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}objectType
{tabStr}{f"dataStoreFile {DataStoreFile.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}{f"dataStoreDirectory {DataStoreDirectory.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """

    # @staticmethod
    # def getCorrectServiceTypeFromServiceObject(dict, client):
    #     if dict["objectType"] == "FILE":
    #         return DataStoreFile(dict['dataStoreFile'], self._client)
    #     elif dict["objectType"] == "DIRECTORY":
    #         return TimeSeriesDb(dict['dataStoreDirectory'], self._client)
