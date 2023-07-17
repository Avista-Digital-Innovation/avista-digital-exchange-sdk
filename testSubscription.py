
import tracemalloc
import asyncio
from tests import test


async def main():
    await test.captureSubscription()
    # await test.iotEndpointSubscription()

tracemalloc.start()
asyncio.run(main())
tracemalloc.stop()
