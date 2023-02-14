from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.digital_twin_model import DigitalTwinModel


class iot_createModel(Mutation):

    def __init__(self, client, debug, displayName, dtmiSegment, description, properties, telemetry):
        super().__init__(client, debug, "iot_createModel", DigitalTwinModel)
        self.displayName = displayName
        self.dtmiSegment = dtmiSegment
        self.description = description
        self.properties = properties
        self.telemetry = telemetry

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    displayName: "{self.displayName}", 
{tabStr}    dtmiSegment: "{self.dtmiSegment}", 
{tabStr}{f'    description: "{self.description}",' if self.description != None else "" }
{tabStr}    properties: [{','.join([property.getMutationParameterString(tabs+1) for property in self.properties])}],
{tabStr}    telemetry: [{','.join([telem.getMutationParameterString(tabs+1) for telem in self.telemetry])}]) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print(f"Creating model {self.displayName}...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.response = DigitalTwinModel(
                self._result['data'][self.mutationName], self._client, self._debug)
            print("Create succeeded")
            return self.response
        except Exception as e:
            raise e
