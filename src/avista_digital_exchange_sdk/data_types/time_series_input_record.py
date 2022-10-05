from ..exceptions import *
from .. import globals
from ..data_types.time_series_measure_value import TimeSeriesMeasureValue
from ..data_types.time_series_dimension import TimeSeriesDimension


class TimeSeriesInputRecord:
    def __init__(self, Time: str, TimeUnit: str, Version: int, MeasureName: str, MeasureValueType: str, MeasureValue: str = None, MeasureValues=None, Dimensions=None):
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

        self.time = Time
        self.timeUnit = TimeUnit
        self.version = Version
        self.measureName = MeasureName
        self.measureValueType = MeasureValueType
        self.measureValue = MeasureValue
        self.measureValues = MeasureValues
        if self.measureValues is not None:
            for measure in self.measureValues:
                if not isinstance(measure, TimeSeriesMeasureValue):
                    InvalidParameterException(
                        "Element in measureValues array is an incorrect type.")
        self.dimensions = Dimensions
        if self.dimensions is not None:
            for dimension in self.dimensions:
                if not isinstance(dimension, TimeSeriesDimension):
                    InvalidParameterException(
                        "Element in dimensions array is an incorrect type.")
        else:
            self.dimensions = []
        return

    def __str__(self):
        return f"""Time Series Record:
   time: {self.time}
   timeUnit: {self.timeUnit}
   version: {self.version}
   measureName: {self.measureName}
   measureValueType: {self.measureValueType}
   measureValue: {self.measureValue}
   measureValues: 
""" + self.getMeasureValuesStr() + f"""   dimensions: 
""" + self.getDimensionsStr()

    def getMeasureValuesStr(self):
        result = ""
        for measure in self.measureValues:
            result += f"{measure}"
        return result

    def getDimensionsStr(self):
        result = ""
        for dimension in self.dimensions:
            result += f"{dimension}"
        return result

    def getMutationParameterString(self, tabs):
        tabStr = ""
        tab = "    "
        for i in range(tabs):
            tabStr += tab

        return f""" {{
{f'{tabStr}Dimensions: [{",".join([dimension.getMutationParameterString(tabs+1) for dimension in self.dimensions])}],' if self.dimensions is not None and len(self.dimensions) > 0 else 'Dimensions: [],'}
{tabStr}MeasureName: "{self.measureName}",
{f'{tabStr}MeasureValue: "{self.measureValue}",' if self.measureValueType != "MULTI" else
f'{tabStr}MeasureValues: [{",".join([measureValue.getMutationParameterString(tabs+1) for measureValue in self.measureValues])}],'}
{tabStr}MeasureValueType: {self.measureValueType},
{tabStr}Time: "{self.time}",
{tabStr}TimeUnit: {self.timeUnit},
{f'{tabStr}Version: {self.version}' if self.version is not None else ''}
{tabStr[0:-4]}}}"""
