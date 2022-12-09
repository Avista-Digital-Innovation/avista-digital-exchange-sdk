
from ..exceptions import *
from .. import globals
from .endpoint_telemetry import EndpointTelemetry


class EndpointTelemetryDataRecord:

    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    # def __str__(self):
    #     result = f"""Endpoint last values:"""
    # # Record: iotEndpointId: {self.record.iotEndpointId} timestamp: {self.record.timestamp} ({self.record.timeUnit})
    # # Errors:"""
    # #     for error in self.errors:
    # #         result += f"""
    # #     - {error.message}"""
    #     return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException

        self.telemetryModel = EndpointTelemetry(
            dict['telemetryModel'], self._client, self._debug)
        self.timestamp = dict['timestamp']
        self.value = dict['value']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{ 
{tabStr}{f"telemetryModel {EndpointTelemetry.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}timestamp
{tabStr}value
{tabStr[0:-4]}}} """
