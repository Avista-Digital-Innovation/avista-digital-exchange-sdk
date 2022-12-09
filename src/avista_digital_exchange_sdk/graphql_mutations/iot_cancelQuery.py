from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.server_response import ServerResponse


class iot_cancelQuery(Mutation):

    def __init__(self, client, debug, queryId):
        super().__init__(client, debug, "iot_cancelQuery", ServerResponse)
        self.queryId = queryId

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    queryId: "{self.queryId}") {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print("Cancelling query...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = ServerResponse(
                self._result['data'][self.mutationName], self._client, self._debug)
            return self.response
        except Exception as e:
            raise e
