from ..exceptions import *
from ..common import *
import requests
from ..data_types.user import User
from ..data_types.data_store_object import DataStoreObject
from ..data_types.data_store_file import DataStoreFile

class DataStoreDirectory(DataStoreObject):
    def __init__(self, dict, client):
        super().__init__(dict, client)
        self.client = client
        if dict is None:
            return
        else:
            self.buildFromDictionary(dict)
    
    def __str__(self):
        return f"""Directory: {self.dataStoreDirectoryId}
name: ${self.name}
dataStoreId: {self.dataStoreId}
parentDirectory: {self.parentDirectoryId}
contents: 
{"  empty" if len(self.directories) == 0 and len(self.files) == 0 else self.printContents()} """       

    def printContents(self):
        result = ""
        if len(self.directories) > 0:
            for dir in self.directories:
                result += f"  (directory) {dir.name} | {dir.dataStoreDirectoryId}\n"
        if len(self.files) > 0:
            for file in self.files:
                result += f"  (file) {file.getFilename()} | id: {file.dataStoreFileId}\n"
        return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.dataStoreDirectoryId = dict['dataStoreDirectoryId']
        self.dataStoreId = dict['dataStoreId']
        self.name = dict['name']
        self.owner = User(dict['owner'], self.client)
        self.homeDirectory = dict['homeDirectory']
        self.parentDirectoryId = dict['parentDirectoryId']
        self.directories = []
        self.files = []
        for currentObject in dict['contents']:
            if currentObject["objectType"] == "FILE":
                self.files.append(DataStoreFile(currentObject["dataStoreFile"], self.client))
            elif currentObject["objectType"] == "DIRECTORY":
                self.directories.append(DataStoreDirectory(currentObject["dataStoreDirectory"], self.client))


    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}dataStoreDirectoryId
{tabStr}dataStoreId
{tabStr}name
{tabStr}{f"owner {User.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}homeDirectory
{tabStr}parentDirectoryId
{tabStr}{f"contents {DataStoreObject.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
