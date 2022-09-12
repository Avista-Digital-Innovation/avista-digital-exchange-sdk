from .query import *
from exceptions import *
from common import *
from data_types.collaborative import Collaborative
from data_types.service import Service

class collaborative_listCollaboratives(Query):

    def __init__(self, client):
        super().__init__(client, "collaborative_listCollaboratives", Collaborative)
    
    def _getQueryString(self):
        return super()._getQueryString()

    def performQuery(self) -> str:
        if debug:
            print('Retrieving your collaboratives...')
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self) -> [Collaborative]:
        super()._processResult()
        try:
            self.collaboratives = []
            for currentCollaborative in self._result['data'][self.queryName]:
                self.collaboratives.append(Collaborative(currentCollaborative, self.client))
            if debug:
                i = 0
                print("Collaboratives you are a member of:")
                for entry in self.collaboratives:
                    print(f'{i}: {entry.name}')
                    print(f'   collaborativeId: {entry.collaborativeId}')
                    i += 1
            return self.collaboratives
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
