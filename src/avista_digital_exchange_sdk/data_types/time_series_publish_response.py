from ..exceptions import *
from .. import globals


class TimeSeriesPublishResponse:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""Publish Response:
    Records Written: {self.totalRecordsWritten}
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
{tabStr}{globals.tab}Total
{tabStr}}}
{tabStr[0:-4]}}} """
