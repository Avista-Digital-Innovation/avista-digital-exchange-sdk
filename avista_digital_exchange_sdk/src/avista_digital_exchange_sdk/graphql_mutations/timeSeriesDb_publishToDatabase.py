from .mutation import *
from ..exceptions import *
from ..common import *
from ..data_types.time_series_publish_input import TimeSeriesPublishInput
from ..data_types.time_series_publish_response import TimeSeriesPublishResponse
from ..data_types.time_series_asset_data import TimeSeriesAssetData

class timeSeriesDb_publishToDatabase(Mutation):

    def __init__(self, client, timeSeriesDbId, assetId, records):
        super().__init__(client, "timeSeriesDb_publishToDatabase", TimeSeriesAssetData)
        self.timeSeriesDbId = timeSeriesDbId
        self.assetId = assetId
        self.records = records
        self.dataInput = TimeSeriesPublishInput(self.records)
    
    def _getMutationString(self):
        tabs = 1        
        tabStr = getTabStr(tabs)
        return f"""mutation {self.mutationName} {{ 
{tabStr}{self.mutationName}(
{tabStr}    assetId: "{self.assetId}", 
{tabStr}    timeSeriesDbId: "{self.timeSeriesDbId}", 
{tabStr}    data: {self.dataInput.getMutationParameterString(tabs+2)}) {self.resultType.getQueryString(tabs+1)} 
}}"""

    def performMutation(self):
        if debug:
            print("Publishing records to the database...")
        self._result = self.client.performMutation(self._getMutationString())
        return self._processResult()
    
    def _processResult(self):
        super()._processResult()
        try:
            # self.response = TimeSeriesPublishResponse(self._result['data'][self.mutationName], self.client)
            self.assetData = []
            for current in self._result['data'][self.mutationName]:
                self.assetData.append(TimeSeriesAssetData(current, self.client))
            if debug:
                print("Publish succeeded")
                print(self.assetData)
            return self.assetData
        except Exception as e:
            raise e
