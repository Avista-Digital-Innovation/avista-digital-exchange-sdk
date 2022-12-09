from ..exceptions import *
from .. import globals
from .iot_data_record import IotDataRecord
from .iot_data_record_error import IotDataRecordError


class IotDataRecordWithErrors:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        result = f"""Record errors:
    Record: iotEndpointId: {self.record.iotEndpointId} timestamp: {self.record.timestamp} ({self.record.timeUnit})
    Errors:"""
        for error in self.errors:
            result += f"""
        - {error.message}"""
        return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.record = IotDataRecord(dict['record'], self._client, self._debug)
        self.errors = []
        for error in dict['errors']:
            self.errors.append(
                IotDataRecordError(error, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{ 
{tabStr}{f"record {IotDataRecord.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}{f"errors {IotDataRecordError.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
