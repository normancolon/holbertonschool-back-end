#!/usr/bin/env python3
import asyncio
from typing import List

# Import the async_generator from the module where it's defined
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Use async comprehension to collect 10 random numbers from an async generator."""
    return [i async for i in async_generator()]

# This section is for testing and is not part of the coroutine module.
if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
