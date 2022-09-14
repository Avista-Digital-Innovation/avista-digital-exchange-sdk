from ..exceptions import *
from ..common import *

class TimeSeriesMeasureValue:
    def __init__(self, Type, Name, Value):
        self.Type = Type
        self.Name = Name
        self.Value = Value
        return

    def __str__(self):
        return f"""      MeasureValue:
        Type: {self.Type}
        Name: {self.Name}
        Value: {self.Value}
"""

    def getMutationParameterString(self, tabs):
        tabStr = ""
        tab = "    "
        for i in range(tabs):
            tabStr += tab

        return f""" {{
{tabStr}Type: {self.Type},
{tabStr}Name: "{self.Name}",
{tabStr}Value: "{self.Value}"
{tabStr[0:-4]}}}"""
