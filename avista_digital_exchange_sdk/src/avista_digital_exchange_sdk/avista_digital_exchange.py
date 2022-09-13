from .client import Client
from .common import *
from .graphql_queries.user_getUserSession import user_getUserSession
from .graphql_queries.collaborative_listCollaboratives import collaborative_listCollaboratives
from .graphql_queries.collaborative_listCollaborativeServices import collaborative_listCollaborativeServices
from .graphql_queries.collaborative_listCollaborativesServiceSharedWith import collaborative_listCollaborativesServiceSharedWith
from .graphql_queries.collaborative_getCollaborative import collaborative_getCollaborative
from .graphql_queries.storage_listDataStores import storage_listDataStores
from .graphql_queries.storage_getDataStore import storage_getDataStore
from .graphql_queries.storage_getDataStoreFile import storage_getDataStoreFile
from .graphql_queries.storage_getDataStoreDirectory import storage_getDataStoreDirectory
from .graphql_queries.storage_getDataStoreFileDownloadUrl import storage_getDataStoreFileDownloadUrl
from .graphql_queries.timeSeriesDb_listDatabases import timeSeriesDb_listDatabases
from .graphql_queries.timeSeriesDb_getDatabase import timeSeriesDb_getDatabase
from .graphql_queries.timeSeriesDb_queryDatabaseWithTimestreamQuery import timeSeriesDb_queryDatabaseWithTimestreamQuery

from .graphql_mutations.storage_createDataStoreFile import storage_createDataStoreFile
from .graphql_mutations.storage_deleteDataStoreFile import storage_deleteDataStoreFile
from .graphql_mutations.collaborative_addServiceToCollaborative import collaborative_addServiceToCollaborative
from .graphql_mutations.collaborative_removeServiceFromCollaborative import collaborative_removeServiceFromCollaborative
from .graphql_mutations.timeSeriesDb_publishToDatabase import timeSeriesDb_publishToDatabase
# from .graphql_mutations.timeSeriesDb_generateQueryResultExportFile import timeSeriesDb_generateQueryResultExportFile

from .data_types.user import User
from .data_types.collaborative import Collaborative
from .data_types.data_store import DataStore
from .data_types.data_store_file import DataStoreFile
from .data_types.data_store_directory import DataStoreDirectory
from .data_types.time_series_db import TimeSeriesDb
from .data_types.service import Service
from .data_types.time_series_publish_input import TimeSeriesPublishInput
from .data_types.time_series_asset_data import TimeSeriesAssetData
from .data_types.time_series_input_record import TimeSeriesInputRecord
from .data_types.time_series_measure_value import TimeSeriesMeasureValue
from .data_types.time_series_dimension import TimeSeriesDimension
from .data_types.timestream_query_result import QueryResult_TimestreamVariables

from .exceptions import *
import os

class AvistaDigitalExchange(object):
    def __init__(self, token = True, debugParam = None):
        if debugParam is not None:
            global debug
            debug = debug
        self.token = token
        self.client = Client(token)

    def getUserInfo(self) -> User:
        """Retrieves the user information of the user associated with the authentication token in use."""
        query = user_getUserSession(self.client)
        result = query.performQuery()
        return result
    
    def listDataStores(self):
        """Lists the Data Stores belonging to the user"""
        query = storage_listDataStores(self.client)
        result = query.performQuery()
        return result
    
    def getDataStore(self, dataStoreId) -> DataStore:
        """Retrieves the Data Store's metadata by dataStoreId"""
        query = storage_getDataStore(self.client, dataStoreId)
        result = query.performQuery()
        return result
    
    def getDataStoreDirectory(self, dataStoreDirectoryId) -> DataStoreDirectory:
        """Retrieves a Data Store directory and it's contents by dataStoreDirectoryId"""
        query = storage_getDataStoreDirectory(self.client, dataStoreDirectoryId)
        result = query.performQuery()
        return result

    def getDataStoreFileMeta(self, dataStoreFileId) -> DataStoreFile:
        """Retrieves a Data Store file's metadata by dataStoreFileId"""
        query = storage_getDataStoreFile(self.client, dataStoreFileId)
        dataStoreFile = query.performQuery()
        return dataStoreFile

    def downloadDataStoreFile(self, dataStoreFileId, writeLocation) -> DataStoreFile:
        """Retrieves a Data Store file's metadata and downloads and writes the file to the local file system"""
        query = storage_getDataStoreFile(self.client, dataStoreFileId)
        dataStoreFile = query.performQuery()
        presignedUrl = dataStoreFile.getFileUrl(dataStoreFileId)
        location = dataStoreFile.downloadAndWriteFile(presignedUrl.url, writeLocation)
        return dataStoreFile


    def listCollaboratives(self):
        """Lists the Collaboratives the user is a member of"""
        query = collaborative_listCollaboratives(self.client)
        result = query.performQuery()
        return result
     
    def getCollaborative(self, collaborativeId) -> Collaborative:
        """Gets the Collaborative's metadata by collaborativeId"""
        query = collaborative_getCollaborative(self.client, collaborativeId)
        result = query.performQuery()
        return result
     
    def listCollaborativeServices(self, collaborativeId):
        """Lists all Services shared in the Collaborative"""
        query = collaborative_listCollaborativeServices(self.client, collaborativeId)
        result = query.performQuery()
        return result
     
    def listCollaborativesServiceSharedWith(self, serviceId):
        """Lists the Collaboratives that a Service is shared with"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'timeSeriesDb' in serviceId:
            serviceType = 'TIME_SERIES_DB'
        query = collaborative_listCollaborativesServiceSharedWith(self.client, serviceType, serviceId)
        result = query.performQuery()
        return result

    def listTimeSeriesDatabases(self):
        """Lists the Time Series Databases belonging to the user"""
        query = timeSeriesDb_listDatabases(self.client)
        result = query.performQuery()
        return result

    def getTimeSeriesDatabase(self, timeSeriesDbId) -> TimeSeriesDb:
        """Gets the Time Series Database's metadata"""
        query = timeSeriesDb_getDatabase(self.client, timeSeriesDbId)
        result = query.performQuery()
        return result

    def queryTimeSeriesDatabase(self, timeSeriesDbId, queryString, maxRows = None, nextToken = None, clientToken = None) -> QueryResult_TimestreamVariables:
        """Queries the Time Series Database using AWS Timestream query format"""
        query = timeSeriesDb_queryDatabaseWithTimestreamQuery(self.client, timeSeriesDbId, queryString, maxRows, nextToken, clientToken)
        result = query.performQuery()
        return result

    def uploadFileToDataStore(self, dataStoreId, dataStoreDirectoryId, localFilePath, name = None, description = None) -> DataStoreFile:
        """Copies a local file to the Data Store and is placed in the directory matching dataStoreDirectoryId"""
        # Check if file exists in local file system
        if not os.path.isfile(localFilePath):
            raise FileNotFoundException
        if not name:
            name = localFilePath.split('/')[-1]
        fileExtension = '.'.join(name.split('.')[1:])
        fileRoot = name.split('.')[0]

        # Create the file in the Digital Exchange and receive a presigned url to upload the file to
        mutation = storage_createDataStoreFile(self.client, dataStoreId, dataStoreDirectoryId, fileRoot, fileExtension, description)
        presignedUrl = mutation.performMutation()
        dataStoreFileId = presignedUrl.itemId
        uploadResult = None
        try:
            if presignedUrl.url is None:
                raise Exception('Did not receive upload endpoint as expected')
            uploadResult = DataStoreFile.uploadFile(presignedUrl.url, localFilePath)
        except FileUploadException as err:
            self.deleteDataStoreFile(dataStoreFileId)
            raise err
        return self.getDataStoreFileMeta(dataStoreFileId)

    def deleteDataStoreFile(self, dataStoreFileId) -> DataStoreFile:
        """Deletes the file from the Data Store"""
        mutation = storage_deleteDataStoreFile(self.client, dataStoreFileId)
        dataStoreFile = mutation.performMutation()
        return dataStoreFile

    def addServiceToCollaborative(self, serviceId, collaborativeId) -> Service:
        """Shares the Service to the Collaborative"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'timeSeriesDb' in serviceId:
            serviceType = 'TIME_SERIES_DB'
        mutation = collaborative_addServiceToCollaborative(self.client, collaborativeId, serviceType, serviceId)
        result = mutation.performMutation()
        return result

    def removeServiceFromCollaborative(self, serviceId, collaborativeId) -> Service:
        """Removes the Service from the Collaborative"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'timeSeriesDb' in serviceId:
            serviceType = 'TIME_SERIES_DB'
        mutation = collaborative_removeServiceFromCollaborative(self.client, collaborativeId, serviceType, serviceId)
        result = mutation.performMutation()
        return result

    def publishToTimeSeriesDatabase(self, timeSeriesDbId, assetId, records):
        """Publishes data records to the database. 
        
        You may only publish records for 1 asset per request. To support viewing on data on the web, 
        include a Dimension entry with DimensionName 'name' and DimensionValue containing the name of the asset.

        Parameters
        ----------
        timeSeriesDbId : str, required
            The id of the database you are publishing to.
        assetId : str, required
            The id of the asset you are publishing data for (or from).
        records : [TimeSeriesInputRecord], required
            An array of data records to write to the database.

        Raises
        ------
        InvalidParameterException
            If an invalid parameter is passed to a method.
        MutationFailed
            Raised if the GraphQL mutation fails, or there is an issue when parsing the result.
        MissingDataInResultException
            Either an empty result was received, or an expected element is not found.
        Unauthorized
            If your authentication token is invalid, you are performing an action that your 
            user roles do not permit, you are performing an action on a resource that does not
            belong to you, or the operation is invalid.
            
        """
        mutation = timeSeriesDb_publishToDatabase(self.client, timeSeriesDbId, assetId, records)
        result = mutation.performMutation()
        return result

    def createTimeSeriesMeasureValue(self, Type, Name, Value) -> TimeSeriesMeasureValue:
        return TimeSeriesMeasureValue(Type, Name, Value)

    def createTimeSeriesDimension(self, DimensionValueType, Name, Value) -> TimeSeriesDimension:
        return TimeSeriesDimension(DimensionValueType, Name, Value)
    
    def createTimeSeriesInputRecord(self, Time, TimeUnit, MeasureName, MeasureValueType, MeasureValue = None, MeasureValues = None, Dimensions = None, Version = 1) -> TimeSeriesInputRecord:
        """Creates and returns a TimeSeriesInputRecord object.

        @Time
        """
        return TimeSeriesInputRecord(Time, TimeUnit, Version, MeasureName, MeasureValueType, MeasureValue, MeasureValues, Dimensions)

    # def generateQueryResultFile(self):
    #     mutation = timeSeriesDb_generateQueryResultExportFile(self.client)
    #     result = mutation.performMutation()
    #     return result