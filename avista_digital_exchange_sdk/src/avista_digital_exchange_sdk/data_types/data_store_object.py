from ..exceptions import *
from ..common import *

class DataStoreObject:
    def __init__(self, dict, client):
        self.client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def buildFromDictionary(self, dict):
        # from .data_store_file import DataStoreFile
        # from .data_store_directory import DataStoreDirectory

        if dict is None:
            raise MissingDataInResultException
        self.objectType = dict['objectType']
        if self.objectType == "FILE":
            self.dataStoreFile = dict['dataStoreFile']# DataStoreFile(dict['dataStoreFile'], self.client)
        elif self.objectType == "DIRECTORY":
            self.dataStoreDirectory = dict['dataStoreDirectory']# DataStoreDirectory(dict['dataStoreDirectory'], self.client)
        else:
            raise ServiceTypeNotAvailable

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        from .data_store_file import DataStoreFile
        from .data_store_directory import DataStoreDirectory
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}objectType
{tabStr}{f"dataStoreFile {DataStoreFile.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}{f"dataStoreDirectory {DataStoreDirectory.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """



    # @staticmethod
    # def getCorrectServiceTypeFromServiceObject(dict, client):
    #     if dict["objectType"] == "FILE":
    #         return DataStoreFile(dict['dataStoreFile'], self.client)
    #     elif dict["objectType"] == "DIRECTORY":
    #         return TimeSeriesDb(dict['dataStoreDirectory'], self.client)