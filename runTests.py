
import tracemalloc
import asyncio
from tests import test


async def main():
    await test.main()

tracemalloc.start()
asyncio.run(main())
tracemalloc.stop()
