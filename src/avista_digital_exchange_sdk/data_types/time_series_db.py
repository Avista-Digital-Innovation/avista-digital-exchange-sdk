from ..exceptions import *
from .. import globals
from .service import Service


class TimeSeriesDb(Service):
    def __init__(self, dict, client, debug):
        super().__init__(dict, client, debug)
        self.timeSeriesDb = self
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""name: {self.name}
    timeSeriesDbId: {self.timeSeriesDbId}
    description: {self.description}
    databaseName: {self.databaseName}
    tableName: {self.tableName}"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.timeSeriesDbId = dict['timeSeriesDbId']
        self.name = dict['name']
        self.description = dict['description']
        self.ownerUserId = dict['ownerUserId']
        self.databaseName = dict['databaseName']
        self.tableName = dict['tableName']

        self.serviceType = "TIME_SERIES_DB"
        self.serviceId = self.timeSeriesDbId

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}timeSeriesDbId
{tabStr}name
{tabStr}description
{tabStr}ownerUserId
{tabStr}databaseName
{tabStr}tableName
{tabStr[0:-4]}}} """
