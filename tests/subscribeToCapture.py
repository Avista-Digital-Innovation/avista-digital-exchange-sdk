# captureDataPublishSample.py
# Example generated at 2023-06-30T16:36:58.057Z

# Import ADX SDK
# Reference: https://pypi.org/project/avista-digital-exchange-sdk/
import asyncio
from src.avista_digital_exchange_sdk import AvistaDigitalExchange, DxTypes
import time
from typing import List, Dict


async def main():
    print("Running main...")
    # Create an instance of the ADX SDK
    # You may use a user authentication token or the authentication token of the Data Capture
    digitalExchange = AvistaDigitalExchange(
        "")
    print("Instantiated AvistaDigitalExchange object with authentication token")

    # Specify the capture you are publishing data to
    captureId = "dataCapture.68877650-42f8-4381-9b63-c70b550c3632"

    # Start Data Capture
    try:
        print("Calling dataCapture.listenForCaptureData")
        async for result in digitalExchange.dataCapture.listenForCaptureData(
                captureId=captureId):
            print("DataCapture.listenForCaptureData: Data received.")

    except Exception as error:
        print(f"dataCapture.listenForCaptureData failed with error: {error}")
        raise error

if __name__ == "__main__":
    asyncio.run(main())
