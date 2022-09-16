from ..exceptions import *
from .. import globals


class TimeSeriesPublishResponse:
    def __init__(self, dict, client):
        self._client = client
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
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}RecordsIngested {{
{tabStr}{tab}Total
{tabStr}}}
{tabStr[0:-4]}}} """
