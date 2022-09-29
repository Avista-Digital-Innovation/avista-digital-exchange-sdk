from ..exceptions import *
from .. import globals


class TimeSeriesDimension:
    def __init__(self, DimensionValueType, Name, Value):
        self.dimensionValueType = DimensionValueType
        self.name = Name
        self.value = Value
        return

    def __str__(self):
        return f"""      Dimension:
        dimensionValueType: {self.dimensionValueType}
        name: {self.name}
        value: {self.value}
"""

    def getMutationParameterString(self, tabs):
        tabStr = ""
        tab = "    "
        for i in range(tabs):
            tabStr += tab

        return f""" {{
{tabStr}DimensionValueType: {self.dimensionValueType},
{tabStr}Name: "{self.name}",
{tabStr}Value: "{self.value}"
{tabStr[0:-4]}}}"""
