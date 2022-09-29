import os
from .exceptions import *
from .data_types.time_series_query_result import TimeSeriesQueryResult
from .data_types.timestream_query_result import QueryResult_TimestreamVariables
from .data_types.time_series_dimension import TimeSeriesDimension
from .data_types.time_series_measure_value import TimeSeriesMeasureValue
from .data_types.time_series_input_record import TimeSeriesInputRecord
from .data_types.service import Service
from .data_types.time_series_db import TimeSeriesDb
from .data_types.data_store_directory import DataStoreDirectory
from .data_types.data_store_file import DataStoreFile
from .data_types.data_store import DataStore
from .data_types.collaborative import Collaborative
from .data_types.user import User
from .graphql_subscriptions.onNotifyTimeSeriesQueryExportComplete import onNotifyTimeSeriesQueryExportComplete
from .graphql_mutations.timeSeriesDb_generateQueryResultExportFile import timeSeriesDb_generateQueryResultExportFile
from .graphql_mutations.timeSeriesDb_publishToDatabase import timeSeriesDb_publishToDatabase
from .graphql_mutations.collaborative_removeServiceFromCollaborative import collaborative_removeServiceFromCollaborative
from .graphql_mutations.collaborative_addServiceToCollaborative import collaborative_addServiceToCollaborative
from .graphql_mutations.storage_deleteDataStoreFile import storage_deleteDataStoreFile
from .graphql_mutations.storage_createDataStoreFile import storage_createDataStoreFile
from .graphql_mutations.timeSeriesDb_cancelDatabaseQuery import timeSeriesDb_cancelDatabaseQuery
from .graphql_queries.timeSeriesDb_listAllAssetLastValues import timeSeriesDb_listAllAssetLastValues
from .graphql_queries.timeSeriesDb_queryDatabaseWithTimestreamQuery import timeSeriesDb_queryDatabaseWithTimestreamQuery
from .graphql_queries.timeSeriesDb_queryDatabase import timeSeriesDb_queryDatabase
from .graphql_queries.timeSeriesDb_getDatabase import timeSeriesDb_getDatabase
from .graphql_queries.timeSeriesDb_listDatabases import timeSeriesDb_listDatabases
from .graphql_queries.storage_getDataStoreDirectory import storage_getDataStoreDirectory
from .graphql_queries.storage_getDataStoreFile import storage_getDataStoreFile
from .graphql_queries.storage_getDataStore import storage_getDataStore
from .graphql_queries.storage_listDataStores import storage_listDataStores
from .graphql_queries.collaborative_getCollaborative import collaborative_getCollaborative
from .graphql_queries.collaborative_listCollaborativesServiceSharedWith import collaborative_listCollaborativesServiceSharedWith
from .graphql_queries.collaborative_listCollaborativeServices import collaborative_listCollaborativeServices
from .graphql_queries.collaborative_listCollaboratives import collaborative_listCollaboratives
from .graphql_queries.user_getUserSession import user_getUserSession
from asyncio import queues
from time import sleep
from .client import Client
from . import globals
import signal
import time


# from .graphql_queries.storage_getDataStoreFileDownloadUrl import storage_getDataStoreFileDownloadUrl


# from .data_types.time_series_publish_input import TimeSeriesPublishInput
# from .data_types.time_series_asset_data import TimeSeriesAssetData


class AvistaDigitalExchange(object):
    def __init__(self, token, debug=False):
        if type(debug) is not bool:
            raise InvalidParameterException(
                "AvistaDigitalExchange debug parameter must be a bool")
        self._stage = "DEVELOPMENT"
        self._debug = debug
        self._token = token
        self._client = Client(self._token, self._stage, self._debug)
        print("SDK initialized!")

    def getUserInfo(self) -> User:
        """Retrieves the user information of the user associated with the authentication token in use."""
        query = user_getUserSession(self._client, self._debug)
        result = query.performQuery()
        return result

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
        query = storage_getDataStoreDirectory(
            self._client, self._debug, dataStoreDirectoryId)
        result = query.performQuery()
        return result

    def getDataStoreFileMeta(self, dataStoreFileId) -> DataStoreFile:
        """Retrieves a Data Store file's metadata by dataStoreFileId"""
        query = storage_getDataStoreFile(
            self._client, self._debug, dataStoreFileId)
        dataStoreFile = query.performQuery()
        return dataStoreFile

    def downloadDataStoreFile(self, dataStoreFileId, writeLocation) -> DataStoreFile:
        """Retrieves a Data Store file's metadata and downloads and writes the file to the local file system"""
        query = storage_getDataStoreFile(
            self._client, self._debug, dataStoreFileId)
        dataStoreFile = query.performQuery()
        presignedUrl = dataStoreFile.getFileUrl(dataStoreFileId)
        location = dataStoreFile.downloadAndWriteFile(
            presignedUrl.url, writeLocation)
        return dataStoreFile

    def listCollaboratives(self):
        """Lists the Collaboratives the user is a member of"""
        query = collaborative_listCollaboratives(self._client, self._debug)
        result = query.performQuery()
        return result

    def getCollaborative(self, collaborativeId) -> Collaborative:
        """Gets the Collaborative's metadata by collaborativeId"""
        query = collaborative_getCollaborative(
            self._client, self._debug, collaborativeId)
        result = query.performQuery()
        return result

    def listCollaborativeServices(self, collaborativeId):
        """Lists all Services shared in the Collaborative"""
        query = collaborative_listCollaborativeServices(
            self._client, self._debug, collaborativeId)
        result = query.performQuery()
        return result

    def listCollaborativesServiceSharedWith(self, serviceId):
        """Lists the Collaboratives that a Service is shared with"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'timeSeriesDb' in serviceId:
            serviceType = 'TIME_SERIES_DB'
        query = collaborative_listCollaborativesServiceSharedWith(
            self._client, self._debug, serviceType, serviceId)
        result = query.performQuery()
        return result

    def listTimeSeriesDatabases(self):
        """Lists the Time Series Databases belonging to the user"""
        query = timeSeriesDb_listDatabases(self._client, self._debug)
        result = query.performQuery()
        return result

    def getTimeSeriesDatabase(self, timeSeriesDbId) -> TimeSeriesDb:
        """Gets the Time Series Database's metadata"""
        query = timeSeriesDb_getDatabase(
            self._client, self._debug, timeSeriesDbId)
        result = query.performQuery()
        return result

    # List Assets and their last known value
    def listTimeSeriesAssetsAndLatestValues(self, timeSeriesDbId, resultFileWriteLocation=None):
        """Gets the table's assets, their attributes, and attribute last known value"""
        query = timeSeriesDb_listAllAssetLastValues(
            self._client, self._debug, timeSeriesDbId)
        result = query.performQuery()
        return result

    # Query Time Series with structure query of array of assets and attributes, return paginated friendly format
    def queryTimeSeriesDatabaseWithFilters(self, timeSeriesDbId, assetAndAttributesFilter, startTime, endTime, resultFileWriteLocation, exportFileFormat="CSV", maxRows=None):
        """Queries the Time Series Database using AWS Timestream query format"""

        exportFileFormat = exportFileFormat.upper()

        if not isValidISO8601Timestamp(startTime):
            raise InvalidParameterException(
                "Invalid startTime. Must be in format YYYY-MM-DD'T'hh:mm:ss.SSS'Z' which is ISO-8601")
        if not isValidISO8601Timestamp(endTime):
            raise InvalidParameterException(
                "Invalid endTime. Must be in format YYYY-MM-DD'T'hh:mm:ss.SSS'Z' which is ISO-8601")

        if exportFileFormat != 'CSV' and exportFileFormat != 'JSON':
            raise InvalidParameterException(
                'exportFileFormat must be CSV or JSON')

        nextToken = None
        clientToken = None
        # attributesArray should be in format [{"assetId": "id123", "attributeNamesFilter": ["name1", "name2"]}]

        queryId = None

        def quitHandler(signum, frame):
            # Stop query
            if queryId is not None:
                print("Cancelling query....")
                mutation = timeSeriesDb_cancelDatabaseQuery(
                    self._client, self._debug, timeSeriesDbId, queryId)
                cancelResult = mutation.performMutation()
            exit(1)

        signal.signal(signal.SIGINT, quitHandler)

        print("querying the database...")
        query = timeSeriesDb_queryDatabase(
            self._client, self._debug, timeSeriesDbId, assetAndAttributesFilter, startTime, endTime, maxRows, nextToken, clientToken)
        result = query.performQuery()

        queryProgressPercentage = result.queryProgressPercentage
        clientToken = result.clientToken
        nextToken = result.nextToken
        queryString = result.queryString
        queryId = result.queryId
        presignedUrl = result.presignedUrl
        resultChunkIndex = result.resultChunkIndex
        print(f"received query result chunk #{resultChunkIndex}...")
        i = 0

        while i < 100 and nextToken is not None:
            query = timeSeriesDb_queryDatabase(
                self._client, self._debug, timeSeriesDbId, assetAndAttributesFilter, startTime, endTime, maxRows, nextToken, clientToken, queryString)
            result = query.performQuery()

            queryProgressPercentage = result.queryProgressPercentage
            clientToken = result.clientToken
            nextToken = result.nextToken
            queryString = result.queryString
            queryId = result.queryId
            presignedUrl = result.presignedUrl
            resultChunkIndex = result.resultChunkIndex
            print(f"received query result chunk #{resultChunkIndex}...")
            i += 1

        if nextToken is not None:
            mutation = timeSeriesDb_cancelDatabaseQuery(
                self._client, self._debug, timeSeriesDbId, queryId)
            cancelResult = mutation.performMutation()
            print('Stopped query because it surpassed sdk nextToken limit')
        else:
            print('Query complete')

        # get onNotifyObject
        subscription = self._getSubscriptionToTimeSeriesQueryExportFileCompletion(
            queryId)

        # Generate export file
        mutationResult = self.generateQueryResultFile(
            timeSeriesDbId, queryId, exportFileFormat)
        if self._debug:
            print(f'mutation result {mutationResult}')

        # wait for subscription notification
        exportFileResult = subscription.waitForResponse(120)
        print(exportFileResult)

        exportFileResult.downloadAndWriteFile(
            exportFileResult.url, resultFileWriteLocation)

        return True

    def queryTimeSeriesDatabase_TimestreamFormat(self, timeSeriesDbId, queryString, maxRows=None, nextToken=None, clientToken=None) -> QueryResult_TimestreamVariables:
        """Queries the Time Series Database using AWS Timestream query format"""
        query = timeSeriesDb_queryDatabaseWithTimestreamQuery(
            self._client, self._debug, timeSeriesDbId, queryString, maxRows, nextToken, clientToken)
        result = query.performQuery()
        return result

    def _getSubscriptionToTimeSeriesQueryExportFileCompletion(self, queryId):
        subscription = onNotifyTimeSeriesQueryExportComplete(
            self._client, self._debug, queryId)
        subscribedThread = subscription.initiateSubscriptionOnNewThread()
        return subscription

    def uploadFileToDataStore(self, dataStoreId, dataStoreDirectoryId, localFilePath, name=None, description=None) -> DataStoreFile:
        """Copies a local file to the Data Store and is placed in the directory matching dataStoreDirectoryId"""
        # Check if file exists in local file system
        if not os.path.isfile(localFilePath):
            raise FileNotFoundException
        if not name:
            name = localFilePath.split('/')[-1]
        fileExtension = '.'.join(name.split('.')[1:])
        fileRoot = name.split('.')[0]

        # Create the file in the Digital Exchange and receive a presigned url to upload the file to
        mutation = storage_createDataStoreFile(
            self._client, self._debug, dataStoreId, dataStoreDirectoryId, fileRoot, fileExtension, description)
        presignedUrl = mutation.performMutation()
        dataStoreFileId = presignedUrl.itemId
        uploadResult = None
        try:
            if presignedUrl.url is None:
                raise Exception('Did not receive upload endpoint as expected')
            uploadResult = DataStoreFile.uploadFile(
                presignedUrl.url, localFilePath, self._debug)
        except FileUploadException as err:
            self.deleteDataStoreFile(dataStoreFileId)
            raise err
        return self.getDataStoreFileMeta(dataStoreFileId)

    def deleteDataStoreFile(self, dataStoreFileId) -> DataStoreFile:
        """Deletes the file from the Data Store"""
        mutation = storage_deleteDataStoreFile(
            self._client, self._debug, dataStoreFileId)
        dataStoreFile = mutation.performMutation()
        return dataStoreFile

    def addServiceToCollaborative(self, serviceId, collaborativeId) -> Service:
        """Shares the Service to the Collaborative"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'timeSeriesDb' in serviceId:
            serviceType = 'TIME_SERIES_DB'
        mutation = collaborative_addServiceToCollaborative(
            self._client, self._debug, collaborativeId, serviceType, serviceId)
        result = mutation.performMutation()
        return result

    def removeServiceFromCollaborative(self, serviceId, collaborativeId) -> Service:
        """Removes the Service from the Collaborative"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'timeSeriesDb' in serviceId:
            serviceType = 'TIME_SERIES_DB'
        mutation = collaborative_removeServiceFromCollaborative(
            self._client, self._debug, collaborativeId, serviceType, serviceId)
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
        mutation = timeSeriesDb_publishToDatabase(
            self._client, self._debug, timeSeriesDbId, assetId, records)
        result = mutation.performMutation()
        return result

    def createTimeSeriesMeasureValue(self, type, name, value) -> TimeSeriesMeasureValue:
        return TimeSeriesMeasureValue(type, name, value)

    def createTimeSeriesDimension(self, dimensionValueType, name, value) -> TimeSeriesDimension:
        return TimeSeriesDimension(dimensionValueType, name, value)

    def createTimeSeriesInputRecord(self, time, timeUnit, measureName, measureValueType, measureValue=None, measureValues=None, dimensions=None, version=1) -> TimeSeriesInputRecord:
        """Creates and returns a TimeSeriesInputRecord object.

        @Time
        """
        return TimeSeriesInputRecord(time, timeUnit, version, measureName, measureValueType, measureValue, measureValues, dimensions)

    def generateQueryResultFile(self, timeSeriesDbId, queryId, fileFormat="CSV"):
        mutation = timeSeriesDb_generateQueryResultExportFile(
            self._client, self._debug, timeSeriesDbId, queryId, fileFormat)
        result = mutation.performMutation()
        return result


def isValidISO8601Timestamp(timestamp):
    import re

    matched = re.match("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z", timestamp)
    isMatch = bool(matched)

    return isMatch
    # try:
    #     datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    # except:
    #     return False
    # return True
