from ..exceptions import *
from .. import globals
import requests
from ..data_types.user import User
from ..data_types.data_store_object import DataStoreObject
from ..data_types.data_store_file import DataStoreFile


class DataStoreDirectory(DataStoreObject):
    def __init__(self, dict, client, debug, parentDirectory=None, retrieveContentObjects=True):
        super().__init__(dict, client, debug)
        self.dataStoreDirectory = self
        self._client = client
        self._debug = debug
        self.parentDirectory = parentDirectory
        if dict is None:
            return
        else:
            self.buildFromDictionary(dict, retrieveContentObjects)

    def __str__(self):
        return f"""name: ${self.name}
    dataStoreDirectoryId: {self.dataStoreDirectoryId}
    dataStoreId: {self.dataStoreId}
    parentDirectory: {self.parentDirectoryId}
    contents: 
{"        empty" if len(self.directories) == 0 and len(self.files) == 0 else self.printContents()} """

    def printContents(self):
        result = ""
        if len(self.directories) > 0:
            for dir in self.directories:
                result += f"        {dir.name}/ | id: {dir.dataStoreDirectoryId}\n"
        if len(self.files) > 0:
            for file in self.files:
                result += f"        {file.getFilename()} | id: {file.dataStoreFileId}\n"
        return result

    def buildFromDictionary(self, dict, retrieveContentObjects=True):
        if dict is None:
            raise MissingDataInResultException
        self.dataStoreDirectoryId = dict['dataStoreDirectoryId']
        self.dataStoreId = dict['dataStoreId']
        self.name = dict['name']
        self.ownerUserId = dict['ownerUserId']
        self.homeDirectory = dict['homeDirectory']
        self.parentDirectoryId = dict['parentDirectoryId']
        self.directories = []
        self.files = []
        for currentObject in dict['contents']:
            if currentObject["objectType"] == "FILE":
                file = self._getFileObject(
                    currentObject["dataStoreFile"]["dataStoreFileId"])
                file.directory = self
                self.files.append(file)
            elif currentObject["objectType"] == "DIRECTORY":
                dir = self.getDirectory(
                    self._client, self._debug, currentObject["dataStoreDirectory"]["dataStoreDirectoryId"])
                dir.parentDirectory = self
                self.directories.append(dir)

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}dataStoreDirectoryId
{tabStr}dataStoreId
{tabStr}name
{tabStr}ownerUserId
{tabStr}homeDirectory
{tabStr}parentDirectoryId
{tabStr}{f"contents {DataStoreObject.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """

    def ls(self, path):
        dir = self.cd(path)
        return self.getLsString()

    def getLsString(self):
        result = ".\n"
        if self.homeDirectory is not True:
            result += "..\n"
        for dir in self.directories:
            result += f"{dir.name}/ | id: {dir.dataStoreDirectoryId}\n"
        for file in self.files:
            result += f"{file.getFilename()} | id: {file.dataStoreFileId}\n"
        return result

    def getPath(self):
        if self.homeDirectory:
            self.path = "/"
        else:
            self.path = self.parentDirectory.getPath() + f'{self.name}/'
        return self.path

    def cd(self, path):
        path = path.strip()
        nextDir = None
        if path == "":
            return self
        elif path == "../" or path == "..":
            if self.homeDirectory:
                raise Exception("Invalid path")
                return self
            else:
                return self.parentDirectory
        elif path == "./" or path == ".":
            return self
        elif path.startswith("/"):
            raise Exception("Invalid path")
            return self
        elif path.startswith("../"):
            return self.parentDirectory.cd(path[3:])
        elif path.startswith("./"):
            return self.cd(path[2:])
        else:
            nextDirName = ""
            try:
                names = path.split("/")
                nextDirName = names[0]
            except:
                raise Exception("Invalid path")
                return self
            else:
                for dir in self.directories:
                    if dir.name == nextDirName:
                        nextDir = dir

        if nextDir is not None:
            if nextDir == self:
                return self

            remainingPath = ""
            try:
                names = path.split("/")
                remainingPath = ("/").join(names[1:])
            except Exception as e:
                print(e)
                return nextDir
            else:
                return nextDir.cd(remainingPath)

        raise Exception("Invalid path")
        return self

    def _getFileObject(self, dataStoreFileId):
        from ..graphql_queries.storage_getDataStoreFile import storage_getDataStoreFile
        query = storage_getDataStoreFile(
            self._client, self._debug, dataStoreFileId)
        dataStoreFile = query.performQuery()
        return dataStoreFile

    def downloadFile(self, filename, writeLocation):
        for file in self.files:
            if file.getFilename() == filename:
                url = file.getFileUrl(file.dataStoreFileId)
                location = file.downloadAndWriteFile(url.url, writeLocation)
                return file

        raise Exception("No file matching filename in current directory")

    def deleteFile(self, filename):
        for file in self.files:
            if file.getFilename() == filename:
                file.deleteDataStoreFile(
                    self._client, self._debug, file.dataStoreFileId)
                return file

        raise Exception("No file matching filename in current directory")

    @staticmethod
    def getDirectory(client, debug, dataStoreDirectoryId):
        from ..graphql_queries.storage_getDataStoreDirectory import storage_getDataStoreDirectory
        query = storage_getDataStoreDirectory(
            client, debug, dataStoreDirectoryId)
        result = query.performQuery()
        return result
