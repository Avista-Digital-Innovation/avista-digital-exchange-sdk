from .query import *
from ..exceptions import *
from ..common import *
from ..data_types.timestream_query_result import QueryResult_TimestreamVariables
import json

class timeSeriesDb_queryDatabaseWithTimestreamQuery(Query):

    def __init__(self, client, timeSeriesDbId, queryString, maxRows, nextToken, clientToken):
        super().__init__(client, "timeSeriesDb_queryDatabaseWithTimestreamQuery", QueryResult_TimestreamVariables)
        if timeSeriesDbId is None:
            raise MissingParameterException("Missing timeSeriesDbId")
        self.timeSeriesDbId = timeSeriesDbId
        self.queryString = json.dumps(queryString)
        self.maxRows = maxRows
        self.nextToken = nextToken
        self.clientToken = clientToken
    
    def _getQueryString(self):
        query = f'query {self.queryName} {{ {self.queryName}(timeSeriesDbId: "{self.timeSeriesDbId}", queryString: {self.queryString}'
        if self.maxRows:
            query += f', maxRows: {self.maxRows}'
        if self.nextToken:
            query += f', nextToken: {self.nextToken}'
        if self.clientToken:
            query += f', clientToken: {self.clientToken}'
        query += f') {self.resultType.getQueryString()} }}'
        return query

    def performQuery(self) -> str:
        if debug:
            print(f'Retrieving time series db {self.timeSeriesDbId}')
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self) -> QueryResult_TimestreamVariables:
        super()._processResult()
        try:
            self.database = QueryResult_TimestreamVariables(self._result['data'][self.queryName], self.client, self.timeSeriesDbId, self.queryString, self.maxRows)
            if debug:
                print(f'Result {self.database}')
            return self.database
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
