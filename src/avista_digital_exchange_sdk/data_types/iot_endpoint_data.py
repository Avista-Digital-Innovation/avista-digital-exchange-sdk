from ..exceptions import *
from .. import globals
from .iot_data_record import IotDataRecord
from .iot_data_record_error import IotDataRecordError


class IotEndpointData:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        result = f"""iot data:
    iotEndpointId: {self.record.iotEndpointId} attributes: [{",".join(self.includedAttributeNames)}]"""
        for record in self.records:
            result += f"""
    {record}"""
        return result

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.iotEndpointId = dict['iotEndpointId']
        self.includedAttributeNames = dict['includedAttributeNames']
        self.records = []
        for entry in dict['records']:
            self.records.append(
                IotDataRecord(entry, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{ 
{tabStr}iotEndpointId
{tabStr}includedAttributeNames
{tabStr}{f"records {IotDataRecord.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
