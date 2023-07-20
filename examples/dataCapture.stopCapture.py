import asyncio
from avista_digital_exchange_sdk import AvistaDigitalExchange

# NOTE: The capture must be in 'CAPTURING' state to be stopped.
captureId = CAPTURE_ID
authenticationToken = AUTHENTICATION_TOKEN


async def main():
    # Create an instance of the AvistaDigitalExchange SDK
    # You may use a user authentication token or the authentication token of the Data Capture
    digitalExchange = AvistaDigitalExchange(authenticationToken)
    print("Instantiated AvistaDigitalExchange instance with authentication token")

    try:
        print("Calling dataCapture.stopCapture")
        result = await digitalExchange.dataCapture.stopCapture(
            captureId=captureId)
    except:
        print("dataCapture.stopCapture failed")

if __name__ == "__main__":
    asyncio.run(main())
