from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.timestream_query_result import QueryResult_TimestreamVariables
import json


class timeSeriesDb_queryDatabaseWithTimestreamQuery(Query):

    def __init__(self, client, debug, timeSeriesDbId, queryString, maxRows, nextToken, clientToken):
        super().__init__(client, debug, "timeSeriesDb_queryDatabaseWithTimestreamQuery",
                         QueryResult_TimestreamVariables)
        if timeSeriesDbId is None:
            raise MissingParameterException("Missing timeSeriesDbId")
        self.timeSeriesDbId = timeSeriesDbId
        self.queryString = json.dumps(queryString)
        self.maxRows = maxRows
        self.nextToken = nextToken
        self._clientToken = clientToken

    def _getQueryString(self):
        query = f'query {self.queryName} {{ {self.queryName}(timeSeriesDbId: "{self.timeSeriesDbId}", queryString: {self.queryString}'
        if self.maxRows:
            query += f', maxRows: {self.maxRows}'
        if self.nextToken:
            query += f', nextToken: "{self.nextToken}"'
        if self._clientToken:
            query += f', clientToken: "{self._clientToken}"'
        query += f') {self.resultType.getQueryString()} }}'
        return query

    def performQuery(self) -> str:
        print(
            f'Querying time series db {self.timeSeriesDbId}{f" with nextToken" if self.nextToken is not None else ""}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> QueryResult_TimestreamVariables:
        super()._processResult()
        try:
            self.result = QueryResult_TimestreamVariables(
                self._result['data'][self.queryName], self._client, self._debug, self.timeSeriesDbId, self.queryString, self.maxRows)
            print(f'{self.result}')
            return self.result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
