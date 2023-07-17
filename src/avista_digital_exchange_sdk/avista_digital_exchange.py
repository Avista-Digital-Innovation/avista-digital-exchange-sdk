import logging
from .exceptions import *
from .iotUtil import *
from .dataStoreUtil import *
from .dataCaptureUtil import *
from .collaborativeUtil import *

from .data_types.user import User
from .graphql_queries.user_getUserSession import user_getUserSession
from .client import Client


class AvistaDigitalExchange(object):

    def __init__(self, token, debug=False):
        if type(debug) is not bool:
            raise InvalidParameterException(
                "AvistaDigitalExchange debug parameter must be a bool")
        self._stage: str = "DEVELOPMENT"
        self._debug: bool = debug
        self._token: str = token
        self._client: Client = Client(self._token, self._stage, self._debug)
        self._logger: Logger = logging.getLogger(name="dx-logger")
        self._logger.setLevel(20)
        self.iot: IoTUtil = IoTUtil(self._debug, self._client)
        # self.collaboratives = CollaborativeUtil(self._debug, self._client)
        self.dataStores: DataStoreUtil = DataStoreUtil(
            self._debug, self._client)
        self.dataCapture: DataCaptureUtil = DataCaptureUtil(
            self._debug, self._client, self._logger)
        print("SDK initialized!")

    def getUserInfo(self) -> User:
        """Retrieves user information associated with the authentication token."""
        query = user_getUserSession(self._client, self._debug)
        result = query.performQuery()
        return result


def isValidISO8601Timestamp(timestamp) -> bool:
    import re

    matched = re.match("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z", timestamp)
    isMatch = bool(matched)

    return isMatch
