from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.collaborative import Collaborative
from ..data_types.service import Service


class collaborative_listCollaboratives(Query):

    def __init__(self, client, debug):
        super().__init__(client, debug, "collaborative_listCollaboratives", Collaborative)

    def _getQueryString(self):
        return super()._getQueryString()

    def performQuery(self) -> str:
        print('Listing your collaboratives...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.collaboratives = []
            for currentCollaborative in self._result['data'][self.queryName]:
                self.collaboratives.append(Collaborative(
                    currentCollaborative, self._client, self._debug))
            i = 0
            for entry in self.collaboratives:
                print(f'{i}: {entry}')
                i += 1
            return self.collaboratives
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
