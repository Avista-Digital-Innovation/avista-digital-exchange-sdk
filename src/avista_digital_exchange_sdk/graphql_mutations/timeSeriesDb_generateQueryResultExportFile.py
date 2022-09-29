from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.time_series_generate_query_export_result import GenerateQueryResultExportFileResult


class timeSeriesDb_generateQueryResultExportFile(Mutation):

    def __init__(self, client, debug, timeSeriesDbId, queryId, fileFormat):
        super().__init__(client, debug, "timeSeriesDb_generateQueryResultExportFile",
                         GenerateQueryResultExportFileResult)
        self.timeSeriesDbId = timeSeriesDbId
        self.queryId = queryId
        self.fileFormat = fileFormat

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    queryId: "{self.queryId}", 
{tabStr}    fileFormat: {self.fileFormat}, 
{tabStr}    timeSeriesDbId: "{self.timeSeriesDbId}") {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print(f"Requesting query result export...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = GenerateQueryResultExportFileResult(
                self._result['data'][self.mutationName], self._client, self._debug)
            print("Server is compiling result export...")
            return self.response
        except Exception as e:
            raise e
