from ..exceptions import *
from .. import globals
import requests
from ..data_types.user import User
from ..data_types.data_store_object import DataStoreObject
import os


class DataStoreFile(DataStoreObject):
    def __init__(self, dict, client, debug, directory=None):
        super().__init__(dict, client, debug)
        self.dataStoreFile = self
        self._client = client
        self._debug = debug
        self.directory = directory
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
        self.ownerUserId = dict['ownerUserId']
        self.fileExtension = dict['fileExtension']
        self.storageSizeBytes = dict['storageSizeBytes']
        self.dataStoreDirectoryId = dict['dataStoreDirectoryId']
        self.s3ConfirmedUpload = dict['s3ConfirmedUpload']
        self.lastModified = dict['lastModified']
        self.contentType = dict['contentType']
        # self.dataViewIds = dict['dataViewIds']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}dataStoreFileId
{tabStr}dataStoreId
{tabStr}dataStoreDirectoryId
{tabStr}name
{tabStr}fileExtension
{tabStr}description
{tabStr}storageSizeBytes
{tabStr}ownerUserId
{tabStr}s3ConfirmedUpload
{tabStr}lastModified
{tabStr}contentType
{tabStr}dataViewIds
{tabStr[0:-4]}}} """

    def getFileUrl(self, dataStoreFileId):
        from ..graphql_queries.storage_getDataStoreFileDownloadUrl import storage_getDataStoreFileDownloadUrl
        if self._debug:
            print('DEBUG - Retrieving file download url...')
        query = storage_getDataStoreFileDownloadUrl(
            self._client, self._debug, self.dataStoreId, dataStoreFileId)
        result = query.performQuery()
        if self._debug:
            print('DEBUG - File download url received...')
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
        print(f'Wrote file to {fullWritePath}')

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
    def uploadFile(url, filePath, debug):
        if debug:
            print(f'DEBUG - Uploading file {filePath}')
        try:
            result = requests.put(url, data=open(filePath, 'rb'))
            print(f'upload file returned status code: {result.status_code}')
            if result.ok:
                if debug:
                    print("DEBUG - File uploaded successfully")
            else:
                raise FileUploadException
        except Exception as err:
            print(f"Upload failed: {err}")
            raise FileUploadException(err)

    @staticmethod
    def getFilenameSegments(name):
        fileExtension = '.'.join(name.split('.')[1:])
        fileRoot = name.split('.')[0]
        return (fileRoot, fileExtension)

    @staticmethod
    def createAndUploadFile(client, debug, localFilePath, dataStoreId, dataStoreDirectoryId, name=None, description=None):
        from ..graphql_mutations.storage_createDataStoreFile import storage_createDataStoreFile

        # Check if file exists in local file system
        if not os.path.isfile(localFilePath):
            raise FileNotFoundException
        if not name:
            name = localFilePath.split('/')[-1]

        (fileRoot, fileExtension) = DataStoreFile.getFilenameSegments(name)

        # Create the file in the Digital Exchange and receive a presigned url to upload the file to
        mutation = storage_createDataStoreFile(
            client, debug, dataStoreId, dataStoreDirectoryId, fileRoot, fileExtension, description)
        presignedUrl = mutation.performMutation()
        dataStoreFileId = presignedUrl.itemId
        uploadResult = None
        try:
            if presignedUrl.url is None:
                raise Exception('Did not receive upload endpoint as expected')
            uploadResult = DataStoreFile.uploadFile(
                presignedUrl.url, localFilePath, debug)
        except FileUploadException as err:
            DataStoreFile.deleteDataStoreFile(
                client, debug, dataStoreFileId)
            raise err
        return DataStoreFile.getDataStoreFile(client, debug, dataStoreFileId)

    @staticmethod
    def deleteDataStoreFile(client, debug, dataStoreFileId):
        from ..graphql_mutations.storage_deleteDataStoreFile import storage_deleteDataStoreFile
        mutation = storage_deleteDataStoreFile(
            client, debug, dataStoreFileId)
        dataStoreFile = mutation.performMutation()
        return dataStoreFile

    @staticmethod
    def getDataStoreFile(client, debug, dataStoreFileId):
        from ..graphql_queries.storage_getDataStoreFile import storage_getDataStoreFile
        query = storage_getDataStoreFile(
            client, debug, dataStoreFileId)
        dataStoreFile = query.performQuery()
        return dataStoreFile

    @staticmethod
    def downloadDataStoreFile(client, debug, dataStoreFileId, writeLocation):
        from ..graphql_queries.storage_getDataStoreFile import storage_getDataStoreFile
        query = storage_getDataStoreFile(
            client, debug, dataStoreFileId)
        dataStoreFile = query.performQuery()
        presignedUrl = dataStoreFile.getFileUrl(dataStoreFileId)
        location = dataStoreFile.downloadAndWriteFile(
            presignedUrl.url, writeLocation)
        return dataStoreFile
