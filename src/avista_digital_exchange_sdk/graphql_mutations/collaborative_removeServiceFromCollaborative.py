from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.data_store import DataStore
from ..data_types.time_series_db import TimeSeriesDb
from ..data_types.service import Service


class collaborative_removeServiceFromCollaborative(Mutation):

    def __init__(self, client, debug, collaborativeId, serviceType, serviceId):
        super().__init__(client, debug, "collaborative_removeServiceFromCollaborative", Service)
        self.collaborativeId = collaborativeId
        self.serviceType = serviceType
        self.serviceId = serviceId

    def _getMutationString(self):
        return f"""mutation {self.mutationName} {{ {self.mutationName}(collaborativeId: "{self.collaborativeId}", serviceType: {self.serviceType}, serviceId: "{self.serviceId}") {self.resultType.getQueryString()} }}"""

    def performMutation(self):
        print("Removing the service from the collaborative...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.service = Service(
                self._result['data'][self.mutationName], self._client, self._debug)
            print("Service was removed")
            return self.service
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of mutation {self.mutationName}")
