from ..exceptions import *
from .. import globals


class TimeSeriesMeasureValue:
    def __init__(self, Type, Name, Value):
        self.type = Type
        self.name = Name
        self.value = Value
        return

    def __str__(self):
        return f"""      measureValue:
        type: {self.type}
        name: {self.name}
        value: {self.value}
"""

    def getMutationParameterString(self, tabs):
        tabStr = ""
        tab = "    "
        for i in range(tabs):
            tabStr += tab

        return f""" {{
{tabStr}Type: {self.type},
{tabStr}Name: "{self.name}",
{tabStr}Value: "{self.value}"
{tabStr[0:-4]}}}"""
