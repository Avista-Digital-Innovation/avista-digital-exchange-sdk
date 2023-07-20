import asyncio
from avista_digital_exchange_sdk import AvistaDigitalExchange

authenticationToken = AUTHENTICATION_TOKEN
captureId = CAPTURE_ID


async def main():
    # Create an instance of the AvistaDigitalExchange SDK
    # You may use a user authentication token or the authentication token of the Data Capture
    digitalExchange = AvistaDigitalExchange(authenticationToken)
    print("Instantiated AvistaDigitalExchange instance with authentication token")

    try:
        print("Calling dataCapture.subscribeToData")
        # The for-loop will run each time a data publish event is received.
        async for result in digitalExchange.dataCapture.subscribeToData(
                captureId=captureId):
            print("DataCapture.subscribeToData: Data received.")
            print("Do something with data...")
    except Exception as error:
        print(f"dataCapture.subscribeToData failed with error: {error}")
        raise error

if __name__ == "__main__":
    asyncio.run(main())
