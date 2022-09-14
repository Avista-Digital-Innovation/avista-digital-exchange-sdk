from .query import *
from ..exceptions import *
from ..common import *
from ..data_types.collaborative import Collaborative

class collaborative_getCollaborative(Query):

    def __init__(self, client, collaborativeId):
        super().__init__(client, "collaborative_getCollaborative", Collaborative)
        if collaborativeId is None:
            raise MissingParameterException("Missing collaborativeId")
        self.collaborativeId = collaborativeId
    
    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(collaborativeId: "{self.collaborativeId}") {self.resultType.getQueryString()} }}'


    def performQuery(self) -> str:
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self) -> Collaborative:
        super()._processResult()
        try:
            return Collaborative(self._result['data'][self.queryName], self.client)
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
