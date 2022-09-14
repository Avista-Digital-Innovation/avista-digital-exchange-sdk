from .query import *
from ..exceptions import *
from ..common import *
from ..data_types.collaborative import Collaborative
from ..data_types.data_store import Service

class collaborative_listCollaborativesServiceSharedWith(Query):

    def __init__(self, client, serviceType, serviceId):
        super().__init__(client, "collaborative_listCollaborativesServiceSharedWith", Collaborative)
        if serviceType is None:
            raise MissingParameterException("Missing serviceType")
        if serviceId is None:
            raise MissingParameterException("Missing serviceId")
        self.serviceType = serviceType
        self.serviceId = serviceId
    
    def _getQueryString(self):
        return f'query {self.queryName} {{ {self.queryName}(serviceType: {self.serviceType}, serviceId: "{self.serviceId}") {self.resultType.getQueryString()} }}'


    def performQuery(self) -> str:
        if debug:
            print('Retrieving the collaboratives service is shared with...')
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self):
        super()._processResult()
        try:
            self.collaboratives = []
            for currentCollaborative in self._result['data'][self.queryName]:
                self.collaboratives.append(Collaborative(currentCollaborative, self.client))
            if debug:
                print(f'Service is shared with {len(self.collaboratives)} collaborative{"s" if len(self.collaboratives) > 1 else ""}:')
                i = 0
                for entry in self.collaboratives:
                    print(f'{i}: {entry}')
                    i += 1
            return self.collaboratives
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")