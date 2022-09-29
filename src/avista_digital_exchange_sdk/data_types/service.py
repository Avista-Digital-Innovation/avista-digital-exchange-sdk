from ..exceptions import *
from .. import globals


class Service:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        if self.serviceType == "DATA_STORE":
            return f"""{self.dataStore}"""
        elif self.serviceType == "TIME_SERIES_DB":
            return f"""{self.timeSeriesDb}"""
        else:
            return f"""{self.serviceType} - id: {self.serviceId}"""

    def buildFromDictionary(self, dict):
        from .data_store import DataStore
        from .time_series_db import TimeSeriesDb

        if dict is None:
            raise MissingDataInResultException
        self.serviceId = dict['serviceId']
        self.serviceType = dict['serviceType']
        if self.serviceType == "DATA_STORE":
            self.dataStore = DataStore(
                dict['dataStore'], self._client, self._debug)
        elif self.serviceType == "TIME_SERIES_DB":
            self.timeSeriesDb = TimeSeriesDb(
                dict['timeSeriesDb'], self._client, self._debug)
        else:
            raise ServiceTypeNotAvailable

    @staticmethod
    def getCorrectServiceTypeFromServiceObject(dict, client, debug):
        from .data_store import DataStore
        from .time_series_db import TimeSeriesDb
        if dict["serviceType"] == "DATA_STORE":
            return DataStore(dict['dataStore'], client, debug)
        elif dict["serviceType"] == "TIME_SERIES_DB":
            return TimeSeriesDb(dict['timeSeriesDb'], client, debug)
        else:
            raise ServiceTypeNotAvailable

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        from .data_store import DataStore
        from .time_series_db import TimeSeriesDb
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}serviceId
{tabStr}serviceType
{tabStr}{f"timeSeriesDb {TimeSeriesDb.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}{f"dataStore {DataStore.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
