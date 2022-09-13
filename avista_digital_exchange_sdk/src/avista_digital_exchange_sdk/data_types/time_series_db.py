from ..exceptions import *
from ..common import *
from .service import Service

class TimeSeriesDb(Service):
    def __init__(self, dict, client):
        super().__init__(dict, client)
        self.client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""Time Series Db: {self.timeSeriesDbId}
   name: {self.name}
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
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}timeSeriesDbId
{tabStr}name
{tabStr}description
{tabStr}ownerUserId
{tabStr}databaseName
{tabStr}tableName
{tabStr[0:-4]}}} """

    def method(self):
        # TODO
        return