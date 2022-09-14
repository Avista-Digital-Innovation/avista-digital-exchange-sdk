from ..exceptions import *
from ..common import *
from .service import Service
import requests

class DataStore(Service):
    def __init__(self, dict, client):
        super().__init__(dict, client)
        self.client = client
        if dict is None:
            return
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""Data Store: {self.dataStoreId}
   name: {self.name}
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

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}dataStoreId
{tabStr}name
{tabStr}description
{tabStr}ownerUserId
{tabStr}homeDirectoryId
{tabStr[0:-4]}}} """

    def listDirectoryContents(self, dataStoreDirectoryId):
        # TODO
        return

    def getFileUrl(self, dataStoreFileId):
        from graphql_queries.storage_getDataStoreFileDownloadUrl import storage_getDataStoreFileDownloadUrl
        query = storage_getDataStoreFileDownloadUrl(self.client, self.dataStoreId, dataStoreFileId)
        result = query.performQuery()
        return result

    @staticmethod
    def downloadAndWriteFile(url, writeLocation):
        response = requests.get(url)
        open(writeLocation, "wb").write(response.content)

    def writeFile(self, path, dataStoreDirectoryId):
        # TODO
        return

    def makeDirectory(self, path, dataStoreDirectoryId):
        # TODO
        return
