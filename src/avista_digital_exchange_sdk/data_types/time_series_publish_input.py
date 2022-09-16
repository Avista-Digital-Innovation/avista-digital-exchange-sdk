from ..exceptions import *
from .. import globals
from ..data_types.time_series_input_record import TimeSeriesInputRecord


class TimeSeriesPublishInput:
    def __init__(self, records):
        self.records = []
        if records:
            self.addRecords(records)
        return

    def addRecords(self, records):
        # Check that records are of the correct type
        for record in records:
            if not isinstance(record, TimeSeriesInputRecord):
                raise InvalidParameterException(
                    "Records array contains elements that are not of type TimeSeriesInputRecord")
        self.records.extend(records)

    def getMutationParameterString(self, tabs):
        tabStr = globals.getTabStr(tabs)
        result = f""" {{
{tabStr}records: [{','.join([record.getMutationParameterString(tabs+1) for record in self.records])}]
{tabStr[0:-4]}}} """
        return result
