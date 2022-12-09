
from ..exceptions import *
from .. import globals
from .endpoint_telemetry_data_record import EndpointTelemetryDataRecord


class EndpointLastValues:
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

        self.iotEndpointId = dict["iotEndpointId"]
        self.telemetryValues = []
        for entry in dict["telemetryValues"]:
            self.telemetryValues.append(EndpointTelemetryDataRecord(
                entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{ 
{tabStr}iotEndpointId
{tabStr}{f"telemetryValues {EndpointTelemetryDataRecord.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
