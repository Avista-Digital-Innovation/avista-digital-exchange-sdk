from ..exceptions import *
from ..common import *

class TimeSeriesDimension:
    def __init__(self, DimensionValueType, Name, Value):
        self.DimensionValueType = DimensionValueType
        self.Name = Name
        self.Value = Value
        return

    def __str__(self):
        return f"""      Dimension:
        DimensionValueType: {self.DimensionValueType}
        Name: {self.Name}
        Value: {self.Value}
"""

    def getMutationParameterString(self, tabs):
        tabStr = ""
        tab = "    "
        for i in range(tabs):
            tabStr += tab

        return f""" {{
{tabStr}DimensionValueType: {self.DimensionValueType},
{tabStr}Name: "{self.Name}",
{tabStr}Value: "{self.Value}"
{tabStr[0:-4]}}}"""
