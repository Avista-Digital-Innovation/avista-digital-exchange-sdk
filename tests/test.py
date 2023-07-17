
from src.avista_digital_exchange_sdk import AvistaDigitalExchange
from . import test_dataCapture_publishData
from . import test_iot_publishData
from . import capturePublish
from . import subscribeToCapture
from . import subscribeToIotEndpoint


async def main():
    # dev
    # dxInstance = AvistaDigitalExchange(
    #     "token", True)
    await capturePublish.main()

    # capturePublishDataResult = await test_dataCapture_publishData.runTest(dxInstance=dxInstance)

    # iotPublishDataResult = await test_iot_publishData.runTest(dxInstance=dxInstance)


async def captureSubscription():
    await subscribeToCapture.main()


async def iotEndpointSubscription():
    await subscribeToIotEndpoint.main()
