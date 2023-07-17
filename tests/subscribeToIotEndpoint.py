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
        "", True)
    print("Instantiated AvistaDigitalExchange object with authentication token")

    # Start Data Capture
    try:
        digitalExchange.iot.queryByTimeRange(
            "iotEndpointId.e141dd76-c9c5-452f-b644-f94907d82fbd", ["Temperature", "Humidity", "PM2_5"], '2022-12-01T10:11:12.123Z', '2023-12-13T23:11:12.123Z')

    except Exception as error:
        print(f"iot.queryByTimeRange failed with error: {error}")
        raise error

if __name__ == "__main__":
    asyncio.run(main())
