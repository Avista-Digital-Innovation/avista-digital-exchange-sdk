from .mutation import *
from ..exceptions import *
from ..common import *
from ..data_types.data_store import DataStore
from ..data_types.time_series_db import TimeSeriesDb
from ..data_types.service import Service

class collaborative_addServiceToCollaborative(Mutation):

    def __init__(self, client, collaborativeId, serviceType, serviceId):
        super().__init__(client, "collaborative_addServiceToCollaborative", Service)
        self.collaborativeId = collaborativeId
        self.serviceType = serviceType
        self.serviceId = serviceId
    
    def _getMutationString(self):
        return f"""mutation {self.mutationName} {{ {self.mutationName}(collaborativeId: "{self.collaborativeId}", serviceType: {self.serviceType}, serviceId: "{self.serviceId}") {self.resultType.getQueryString()} }}"""

    def performMutation(self):
        if debug:
            print("Adding your service to the collaborative...")
        self._result = self.client.performMutation(self._getMutationString())
        return self._processResult()
    
    def _processResult(self):
        super()._processResult()
        try:
            if debug:
                print("Service was successfully shared to the collaborative")
            self.service = Service(self._result['data'][self.mutationName], self.client)
            return self.service
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of mutation {self.mutationName}")
