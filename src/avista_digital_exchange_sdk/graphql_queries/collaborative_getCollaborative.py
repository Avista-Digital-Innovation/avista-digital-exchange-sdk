from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.collaborative import Collaborative


class collaborative_getCollaborative(Query):

    def __init__(self, client, debug, collaborativeId):
        super().__init__(client, debug, "collaborative_getCollaborative", Collaborative)
        if collaborativeId is None:
            raise MissingParameterException("Missing collaborativeId")
        self.collaborativeId = collaborativeId

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(collaborativeId: "{self.collaborativeId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        print(f'Retrieving collaborative {self.collaborativeId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self) -> Collaborative:
        super()._processResult()
        try:
            result = Collaborative(
                self._result['data'][self.queryName], self._client, self._debug)
            print(result)
            return result
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
