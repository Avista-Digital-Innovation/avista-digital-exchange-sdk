from ..exceptions import *
from ..common import *
from ..data_types.time_series_measure_value import TimeSeriesMeasureValue
from ..data_types.time_series_dimension import TimeSeriesDimension


class TimeSeriesInputRecord:
    def __init__(self, Time: str, TimeUnit: str, Version: int, MeasureName: str, MeasureValueType: str, MeasureValue: str = None, MeasureValues = None, Dimensions = None):
        """An object parameter for publishing to a Time Series Database.

        The parameters/members are capitalized to better match the Timestream API specification.
        Reference https://docs.aws.amazon.com/timestream/latest/developerguide/API_Record.html

        Parameters
        ----------
        Time : str, required
        TimeUnit : str, required
        Version : int, optional
        MeasureName : str, required
        MeasureValueType : str, required
        MeasureValue : str, optional
        MeasureValues : [TimeSeriesMeasureValue], optional
        Dimensions : [TimeSeriesDimension], optional
        """
        
        self.Time = Time
        self.TimeUnit = TimeUnit
        self.Version = Version
        self.MeasureName = MeasureName
        self.MeasureValueType = MeasureValueType
        self.MeasureValue = MeasureValue
        self.MeasureValues = MeasureValues
        if self.MeasureValues is not None:
            for measure in self.MeasureValues:
                if not isinstance(measure, TimeSeriesMeasureValue):
                    InvalidParameterException("Element in MeasureValues array is an incorrect type.")
        self.Dimensions = Dimensions
        if self.Dimensions is not None:
            for dimension in self.Dimensions:
                if not isinstance(dimension, TimeSeriesDimension):
                    InvalidParameterException("Element in Dimensions array is an incorrect type.")
        return

    def __str__(self):
        return f"""Time Series Record:
   Time: {self.Time}
   TimeUnit: {self.TimeUnit}
   Version: {self.Version}
   MeasureName: {self.MeasureName}
   MeasureValueType: {self.MeasureValueType}
   MeasureValue: {self.MeasureValue}
   MeasureValues: 
""" + self.getMeasureValuesStr() + f"""   Dimensions: 
""" + self.getDimensionsStr()

    def getMeasureValuesStr(self):
        result = ""
        for measure in self.MeasureValues:
            result += f"{measure}"
        return result

    def getDimensionsStr(self):
        result = ""
        for dimension in self.Dimensions:
            result += f"{dimension}"
        return result

    def getMutationParameterString(self, tabs):
        tabStr = ""
        tab = "    "
        for i in range(tabs):
            tabStr += tab
            
        return f""" {{
{f'{tabStr}Dimensions: [{",".join([Dimension.getMutationParameterString(tabs+1) for Dimension in self.Dimensions])}],' if self.Dimensions is not None and len(self.Dimensions) > 0 else ''}
{tabStr}MeasureName: "{self.MeasureName}",
{f'{tabStr}MeasureValue: "{self.MeasureValue}",' if self.MeasureValueType != "MULTI" else
f'{tabStr}MeasureValues: [{",".join([MeasureValue.getMutationParameterString(tabs+1) for MeasureValue in self.MeasureValues])}],'}
{tabStr}MeasureValueType: {self.MeasureValueType},
{tabStr}Time: "{self.Time}",
{tabStr}TimeUnit: {self.TimeUnit},
{f'{tabStr}Version: {self.Version}' if self.Version is not None else ''}
{tabStr[0:-4]}}}"""
        
# # MeasureValueType must be MULTI if using MeasureValues array

#     def getDimensionsParameterString(self, tabs):
#         tabStr = ""
#         tab = "    "
#         for i in range(tabs):
#             tabStr += tab
#         result = ""
#         for Dimension in self.Dimensions[0:-1]:
#             result += f"""{Dimension.getMutationParameterString(tabs+1)},"""
#         result += f"""{self.Dimensions[-1].getMutationParameterString(tabs+1)}"""
#         return result

#     def getMeasureValuesParameterString(self, tabs):
#         tabStr = ""
#         tab = "    "
#         for i in range(tabs):
#             tabStr += tab
#         result = ""
#         for MeasureValue in self.MeasureValues[0:-1]:
#             result += f"""{MeasureValue.getMutationParameterString(tabs+1)},"""
#         result += f"""{self.MeasureValues[-1].getMutationParameterString(tabs+1)}"""
#         return result

# # mutation MyMutation {
# #   timeSeriesDb_publishToDatabase(assetId: "", timeSeriesDbId: "", 
# data: {records: [
#     {
#         Dimensions: [
#             {DimensionValueType: VARCHAR, 
#              Name: "dimName", 
#              Value: "dimValue"}], 
#         MeasureName: "measureName", 
#         MeasureValue: "measureValue", 
#         MeasureValues: [
#             {Type: VARCHAR, 
#             Name: "name123", 
#             Value: "value123"}], 
#         MeasureValueType: MULTI, 
#         Time: "timestring", 
#         TimeUnit: MICROSECONDS, 
#         Version: 1
#     }]}
