from ..exceptions import *
from ..common import *
import requests
from ..data_types.user import User
from ..data_types.data_store_object import DataStoreObject
import os

class DataStoreFile(DataStoreObject):
    def __init__(self, dict, client):
        super().__init__(dict, client)
        self.client = client
        if dict is None:
            return
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""File: {self.dataStoreFileId}
  name: {self.getFilename()}
  description: {self.description}
  dataStoreId: {self.dataStoreId}
  directoryId: {self.dataStoreDirectoryId}
  size: {self.storageSizeBytes} bytes"""       

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.dataStoreFileId = dict['dataStoreFileId']
        self.dataStoreId = dict['dataStoreId']
        self.name = dict['name']
        self.description = dict['description'] if 'description' in dict else ''
        self.owner = User(dict['owner'], self.client)
        self.fileExtension = dict['fileExtension']
        self.storageSizeBytes = dict['storageSizeBytes']
        self.dataStoreDirectoryId = dict['dataStoreDirectoryId']
        self.s3ConfirmedUpload = dict['s3ConfirmedUpload']
        self.lastModified = dict['lastModified']
        self.contentType = dict['contentType']
        # self.dataViewIds = dict['dataViewIds']

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}dataStoreFileId
{tabStr}dataStoreId
{tabStr}dataStoreDirectoryId
{tabStr}name
{tabStr}fileExtension
{tabStr}description
{tabStr}storageSizeBytes
{tabStr}{f"owner {User.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}s3ConfirmedUpload
{tabStr}lastModified
{tabStr}contentType
{tabStr}dataViewIds
{tabStr[0:-4]}}} """

    def getFileUrl(self, dataStoreFileId):
        from graphql_queries.storage_getDataStoreFileDownloadUrl import storage_getDataStoreFileDownloadUrl
        if debug:
            print('Retrieving file download url...')
        query = storage_getDataStoreFileDownloadUrl(self.client, self.dataStoreId, dataStoreFileId)
        result = query.performQuery()
        if debug:
            print('File download url received...')
        return result

    def getFilename(self):
        temp = self.name
        if self.fileExtension is not None:
            temp += '.' + self.fileExtension
        return temp

    def downloadAndWriteFile(self, url, writeLocation):
        response = requests.get(url)
        fullWritePath = self.createWritePath(writeLocation, self.getFilename())
        open(fullWritePath, "wb").write(response.content)
        if debug:
            print('Wrote file to ' + fullWritePath)

    @staticmethod
    def createWritePath(writeLocation, cloudFilename):
        # if location is a directory, append the cloudFilename
        if os.path.isdir(writeLocation):
            return os.path.join(writeLocation, cloudFilename)
        # if not, use the writeLocation
        elif os.path.isfile(writeLocation):
            return writeLocation
        else:
            return writeLocation

    @staticmethod
    def uploadFile(url, filePath):
        if debug:
            print(f'Uploading file {filePath}')
        try:
            result = requests.put(url, data=open(filePath, 'rb'))
            print(f'upload file returned status code: {result.status_code}')
            if result.ok:
                print("File uploaded successfully")
            else:
                raise FileUploadException
        except Exception as err:
            print(f"Upload failed: {err}")
            raise FileUploadException(err)