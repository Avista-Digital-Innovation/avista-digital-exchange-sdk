from ..exceptions import *
from ..common import *

class TimeSeriesPublishResponse:
    def __init__(self, dict, client):
        self.client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""Publish Response:
  Total Records Written: {self.totalRecordsWritten}
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.totalRecordsWritten = dict["RecordsIngested"]["Total"]

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}RecordsIngested {{
{tabStr}{tab}Total
{tabStr}}}
{tabStr[0:-4]}}} """