from ..exceptions import *
from .. import globals
from .iot_attribute_value_input import IotAttributeValueInput
import time
from datetime import datetime


class IotDataRecordInput:
    def __init__(self, timestamp, timeUnit, attributes):
        if timeUnit == "ISO8601":
            self.timeUnit = "MILLISECONDS"
            date = datetime.strptime(
                timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            self.timestamp = f'{int((date - datetime(1970, 1, 1)).total_seconds()*1000)}'
        else:
            self.timestamp = timestamp
            self.timeUnit = timeUnit

        self.attributes = []
        if attributes:
            self.addAttributes(attributes)
        return

    def addAttributes(self, attributes):
        # Check that records are of the correct type
        for attribute in attributes:
            if not isinstance(attribute, IotAttributeValueInput):
                raise InvalidParameterException(
                    "Attributes array contains elements that are not of type IotAttributeValueInput")
        self.attributes.extend(attributes)

    def getMutationParameterString(self, tabs):
        tabStr = globals.getTabStr(tabs)
        result = f""" {{
{tabStr}timestamp: "{self.timestamp}",
{tabStr}timeUnit: {self.timeUnit},
{tabStr}attributes: [{','.join([attribute.getMutationParameterString(tabs+1) for attribute in self.attributes])}]
{tabStr[0:-4]}}} """
        return result

    @staticmethod
    def checkDictForCorrectFields(obj):
        if "attributes" not in obj:
            raise InvalidParameterException(
                "Record is missing 'data' array")
        elif type(obj["attributes"]) is not dict:
            raise InvalidParameterException(
                "Record 'attributes' should be of type dict."
            )
        return dict
