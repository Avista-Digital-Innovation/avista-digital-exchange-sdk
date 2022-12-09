
from .data_types.service import Service

from .data_types.collaborative import Collaborative
from .graphql_mutations.collaborative_removeServiceFromCollaborative import collaborative_removeServiceFromCollaborative
from .graphql_mutations.collaborative_addServiceToCollaborative import collaborative_addServiceToCollaborative
from .graphql_queries.collaborative_getCollaborative import collaborative_getCollaborative
from .graphql_queries.collaborative_listCollaborativesServiceSharedWith import collaborative_listCollaborativesServiceSharedWith
from .graphql_queries.collaborative_listCollaborativeServices import collaborative_listCollaborativeServices
from .graphql_queries.collaborative_listCollaboratives import collaborative_listCollaboratives

import time
import signal


class CollaborativeUtil(object):

    def __init__(self, debug, client):
        self._debug = debug
        self._client = client

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
        elif 'iot' in serviceId:
            serviceType = 'IOT_GROUP'
        query = collaborative_listCollaborativesServiceSharedWith(
            self._client, self._debug, serviceType, serviceId)
        result = query.performQuery()
        return result

    def addServiceToCollaborative(self, serviceId, collaborativeId) -> Service:
        """Shares the Service to the Collaborative"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'iotGroup' in serviceId:
            serviceType = 'IOT_GROUP'
        mutation = collaborative_addServiceToCollaborative(
            self._client, self._debug, collaborativeId, serviceType, serviceId)
        result = mutation.performMutation()
        return result

    def removeServiceFromCollaborative(self, serviceId, collaborativeId) -> Service:
        """Removes the Service from the Collaborative"""
        serviceType = 'unknown'
        if 'dataStore' in serviceId:
            serviceType = 'DATA_STORE'
        elif 'iotGroup' in serviceId:
            serviceType = 'IOT_GROUP'
        mutation = collaborative_removeServiceFromCollaborative(
            self._client, self._debug, collaborativeId, serviceType, serviceId)
        result = mutation.performMutation()
        return result
