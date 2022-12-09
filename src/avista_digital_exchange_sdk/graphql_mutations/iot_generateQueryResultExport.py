from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.iot_generate_query_result_export import IotGenerateQueryResultExport


class iot_generateQueryResultExport(Mutation):

    def __init__(self, client, debug, queryId, fileFormat):
        super().__init__(client, debug, "iot_generateQueryResultExport",
                         IotGenerateQueryResultExport)
        self.queryId = queryId
        self.fileFormat = fileFormat

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    queryId: "{self.queryId}", 
{tabStr}    fileFormat: {self.fileFormat}) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print(f"Requesting query result export...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = IotGenerateQueryResultExport(
                self._result['data'][self.mutationName], self._client, self._debug)
            print("Server is compiling result export...")
            return self.response
        except Exception as e:
            raise e
