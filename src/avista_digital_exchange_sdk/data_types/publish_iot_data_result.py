from ..exceptions import *
from .. import globals
from .iot_data_record import IotDataRecord
from .iot_data_record_with_errors import IotDataRecordWithErrors


class PublishIotDataResult:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    #     def __str__(self):
    #         return f"""Publish Response:
    #     Records Written: {self.recordsWritten}
    # """

    def buildFromDictionary(self, dict):
        self.resultDict = dict
        print(dict)
        if dict is None:
            raise MissingDataInResultException
        self.recordsWritten = []
        for record in dict['recordsWritten']:
            self.recordsWritten.append(
                IotDataRecord(record, self._client, self._debug))
        self.failedRecords = []
        for record in dict['failedRecords']:
            self.failedRecords.append(
                IotDataRecordWithErrors(record, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}{f"recordsWritten {IotDataRecord.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}{f"failedRecords {IotDataRecordWithErrors.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
