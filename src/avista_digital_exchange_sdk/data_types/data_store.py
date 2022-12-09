from ..exceptions import *
from .. import globals
from .service import Service
import requests


class DataStore(Service):
    def __init__(self, dict, client, debug):
        super().__init__(dict, client, debug)
        self.dataStore = self
        self._client = client
        self._debug = debug
        if dict is None:
            return
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""name: {self.name}
   dataStoreId: {self.dataStoreId}
   description: {self.description}
   homeDirectoryId: {self.homeDirectoryId}"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.dataStoreId = dict['dataStoreId']
        self.name = dict['name']
        self.description = dict['description'] if 'description' in dict else ""
        self.ownerUserId = dict['ownerUserId']
        self.homeDirectoryId = dict['homeDirectoryId']

        self.serviceType = "DATA_STORE"
        self.serviceId = self.dataStoreId
        self.currentDirectory = self._getDirectoryObject(
            self.homeDirectoryId)

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}dataStoreId
{tabStr}name
{tabStr}description
{tabStr}ownerUserId
{tabStr}homeDirectoryId
{tabStr[0:-4]}}} """

    def getFileUrl(self, dataStoreFileId):
        from ..graphql_queries.storage_getDataStoreFileDownloadUrl import storage_getDataStoreFileDownloadUrl
        query = storage_getDataStoreFileDownloadUrl(
            self._client, self.dataStoreId, dataStoreFileId)
        result = query.performQuery()
        return result

    @staticmethod
    def downloadAndWriteFile(url, writeLocation):
        response = requests.get(url)
        open(writeLocation, "wb").write(response.content)

    def _getDirectoryObject(self, dataStoreDirectoryId):
        from .data_store_directory import DataStoreDirectory
        return DataStoreDirectory.getDirectory(self._client, self._debug, dataStoreDirectoryId)

    def cd(self, path):
        if path is None:
            raise Exception('path is a required parameter')
        print(
            f'{self.getWorkingDirectoryPath()}: cd {path if path is not None else ""}')
        self.currentDirectory = self.currentDirectory.cd(path)

    def ls(self, path=None):
        lsResult = None
        if path is None:
            lsResult = self.currentDirectory.getLsString()
        else:
            lsResult = self.currentDirectory.ls(path)

        print(f'{self.getWorkingDirectoryPath()}: ls {path if path is not None else ""}\n{lsResult if lsResult is not None else ""}')

    def pwd(self):
        print(
            f'{self.getWorkingDirectoryPath()}: pwd\n{self.getWorkingDirectoryPath()}')

    def getWorkingDirectoryPath(self):
        return self.currentDirectory.getPath()

    @staticmethod
    def help():
        print("Available methods:")
        print(" - ls(path)                    | Print contents of a directory.")
        print("                               | Parameters:")
        print("                               |  - path: string, optional")
        print("                               |      The relative path to the directory to print contents of")
        print("")
        print(" - cd(path)                    | Change working directory")
        print("                               | Parameters:")
        print("                               |  - path: string, required")
        print("                               |      The relative path of the desired directory")
        print("")
        print(" - pwd()                       | Print the path of the working directory.")
        print("")
        print(
            " - uploadFile(localFilePath,   | Upload a file to the data store in the working directory.")
        print("            name,              | Parameters:")
        print("            description)       |  - localFilePath: string, required")
        print("                               |      The location of the file on your local file system.")
        print("                               |  - name: string, optional")
        print("                               |      What the file should be named in the data store.")
        print("                               |  - description: string, optional")
        print("                               |      A brief description of the file and it's contents.")
        print(
            "                               |      Will use local filename if not provided.")
        print("                               |  - description: string, optional")
        print("                               |      A description of what the file is and the data")
        print("                               |      it contains")
        print("")
        print(" - downloadFile(filename,      | Download the specified file.")
        print("                writeLocation) | Parameters:")
        print("                               |  - filename: string, required")
        print("                               |      Name of the remote file in the current directory.")
        print("                               |  - writeLocation: string, required")
        print("                               |      The location to store the downloaded file. If a filename")
        print("                               |      is not given it will be saved with it's remote name.")
        print("")
        print(
            " - deleteFile(filename)        | Deletes the file from the working directory.")
        print("                               | Parameters:")
        print("                               |  - filename: string, required")
        print("                               |      Name of the file to delete.")

    def downloadFile(self, filename, writeLocation):
        return self.currentDirectory.downloadFile(filename, writeLocation)

    def uploadFile(self, localFilePath, name=None, description=None):
        from .data_store_file import DataStoreFile
        file = DataStoreFile.createAndUploadFile(
            self._client, self._debug, localFilePath, self.dataStoreId, self.currentDirectory.dataStoreDirectoryId, name, description)
        self.updateCurrentDirectoryContents()
        return file

    def deleteFile(self, filename):
        file = self.currentDirectory.deleteFile(filename)
        self.updateCurrentDirectoryContents()
        return file

    def updateCurrentDirectoryContents(self):
        parent = self.currentDirectory.parentDirectory
        self.currentDirectory = self._getDirectoryObject(
            self.currentDirectory.dataStoreDirectoryId)
        self.currentDirectory.parentDirectory = parent
