import os
from .exceptions import *
from .iotUtil import *
from .dataStoreUtil import *
from .collaborativeUtil import *

from .data_types.user import User
from .graphql_queries.user_getUserSession import user_getUserSession
from .client import Client
from . import globals


# from .graphql_queries.storage_getDataStoreFileDownloadUrl import storage_getDataStoreFileDownloadUrl

class AvistaDigitalExchange(object):

    def __init__(self, token, debug=False):
        if type(debug) is not bool:
            raise InvalidParameterException(
                "AvistaDigitalExchange debug parameter must be a bool")
        self._stage = "PRODUCTION"
        self._debug = debug
        self._token = token
        self._client = Client(self._token, self._stage, self._debug)
        self.iot = IoTUtil(self._debug, self._client)
        # self.collaboratives = CollaborativeUtil(self._debug, self._client)
        self.dataStores = DataStoreUtil(self._debug, self._client)
        print("SDK initialized!")

    def getUserInfo(self) -> User:
        """Retrieves the user information of the user associated with the authentication token in use."""
        query = user_getUserSession(self._client, self._debug)
        result = query.performQuery()
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
