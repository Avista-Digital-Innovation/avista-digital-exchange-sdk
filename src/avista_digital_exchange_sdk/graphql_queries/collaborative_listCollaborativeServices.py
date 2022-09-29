from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.collaborative import Collaborative
from ..data_types.service import Service


class collaborative_listCollaborativeServices(Query):

    def __init__(self, client, debug, collaborativeId):
        super().__init__(client, debug, "collaborative_listCollaborativeServices", Service)
        self.collaborativeId = collaborativeId

    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(collaborativeId: "{self.collaborativeId}") {self.resultType.getQueryString()} }}'

    def performQuery(self) -> str:
        print(
            f'Listing services available in collaborative {self.collaborativeId}...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.services = []
            for currentService in self._result['data'][self.queryName]:
                self.services.append(Service.getCorrectServiceTypeFromServiceObject(
                    currentService, self._client, self._debug))
            i = 0
            for entry in self.services:
                print(f'{i}: {entry}')
                i += 1
            return self.services
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
