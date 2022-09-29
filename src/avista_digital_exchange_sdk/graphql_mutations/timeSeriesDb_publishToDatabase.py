from .mutation import *
from ..exceptions import *
from .. import globals
from ..data_types.time_series_publish_input import TimeSeriesPublishInput
from ..data_types.time_series_publish_response import TimeSeriesPublishResponse
from ..data_types.time_series_asset_data import TimeSeriesAssetData


class timeSeriesDb_publishToDatabase(Mutation):

    def __init__(self, client, debug, timeSeriesDbId, assetId, records):
        super().__init__(client, debug, "timeSeriesDb_publishToDatabase", TimeSeriesAssetData)
        self.timeSeriesDbId = timeSeriesDbId
        self.assetId = assetId
        self.records = records
        self.dataInput = TimeSeriesPublishInput(self.records)

    def _getMutationString(self):
        tabs = 1
        tabStr = globals.getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    assetId: "{self.assetId}", 
{tabStr}    timeSeriesDbId: "{self.timeSeriesDbId}", 
{tabStr}    data: {self.dataInput.getMutationParameterString(tabs+2)}) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        print(f"Publishing records to the database {self.timeSeriesDbId}...")
        self._result = self._client.performMutation(self._getMutationString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            # self.response = TimeSeriesPublishResponse(self._result['data'][self.mutationName], self._client)
            self.assetData = []
            for current in self._result['data'][self.mutationName]:
                self.assetData.append(
                    TimeSeriesAssetData(current, self._client, self._debug))
            print("Publish succeeded")
            return self.assetData
        except Exception as e:
            raise e
