

import datetime
import time
import random
from src.avista_digital_exchange_sdk import AvistaDigitalExchange
from . import test_dataCapture_publishData
from . import test_iot_publishData


async def main():
    # dev
    dxInstance = AvistaDigitalExchange(
        "token", True)

    # capturePublishDataResult = await test_dataCapture_publishData.runTest(dxInstance=dxInstance)

    # iotPublishDataResult = await test_iot_publishData.runTest(dxInstance=dxInstance)
