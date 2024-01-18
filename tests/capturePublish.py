# captureDataPublishSample.py
# Example generated at 2023-06-30T16:36:58.057Z

# Import ADX SDK
# Reference: https://pypi.org/project/avista-digital-exchange-sdk/
import asyncio
from src.avista_digital_exchange_sdk import AvistaDigitalExchange, DxTypes
import time


async def main():
    print("Running main...")
    # Create an instance of the ADX SDK
    # You may use a user authentication token or the authentication token of the Data Capture
    digitalExchange = AvistaDigitalExchange(
        "8eb938fa-33be-49d2-9c8d-0ada6a94b4db")
    print("Instantiated AvistaDigitalExchange object with authentication token")

    # Specify the capture you are publishing data to
    captureId = "dataCapture.68877650-42f8-4381-9b63-c70b550c3632"

    # Start Data Capture
    # try:
    #     print("Calling dataCapture.startCapture")
    #     startCaptureResult = await digitalExchange.dataCapture.startCapture(
    #         captureId=captureId)
    #     print(f"dataCapture.startCapture result: {startCaptureResult}")
    # except Exception as error:
    #     print(f"dataCapture.startCapture failed with error: {error}")
    #     raise error

    # Example preparing and publishing 10 data records in a single request
    print("Preparing data to publish...")
    for j in range(1000):
        dataRecords = []
        for i in range(2):
            print(f'Building record {i}')
            # Connect your values from your data sources here
            attributeValues = {
                # Attribute data for asset ID 'asset1'
                "a1attr1": i,
                "a2attr1": i*2
            }

            # Add the data record to the current batch
            dataRecords.append(buildDataRecord(
                timestamp=getCurrentMilliseconds(),
                timeUnit=DxTypes.TimeUnitEnum.MILLISECONDS,
                attributeValues=attributeValues))

            # Wait a second before continuing
            await asyncio.sleep(1)

        try:
            print("Calling dataCapture.publishData")
            publishDataResult = await digitalExchange.dataCapture.publishData(
                captureId=captureId, data=dataRecords)
            print(f"dataCapture.publishData result: {publishDataResult}")
        except Exception as error:
            print(f"dataCapture.publishData failed with error: {error}")
            raise error

    # Stop Data Capture
    # try:
    #     print("Calling dataCapture.stopCapture")
    #     stopCaptureResult = await digitalExchange.dataCapture.stopCapture(
    #         captureId=captureId)
    #     print(f"dataCapture.stopCapture result: {stopCaptureResult}")
    # except Exception as error:
    #     print(f"dataCapture.stopCapture failed with error: {error}")
    #     raise error
    # return stopCaptureResult


def getCurrentMilliseconds() -> int:
    # Get the current time in epoch milliseconds
    return int(f'{time.time() * 1000}'.split('.')[0])


def buildDataRecord(
        timestamp: int,
        timeUnit: DxTypes.TimeUnitEnum,
        attributeValues: dict) -> DxTypes.CaptureDataRecordInput:
    record = DxTypes.CaptureDataRecordInput(timestamp=timestamp,
                                            timeUnit=timeUnit,
                                            attributeValues=attributeValues)
    return record


if __name__ == "__main__":
    asyncio.run(main())
