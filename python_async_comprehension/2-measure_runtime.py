#!/usr/bin/env python3
import asyncio
import time

# Import the async_comprehension coroutine from the module where it's defined
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of executing async_comprehension four times in parallel."""
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time

# This section is for testing and is not part of the coroutine module.
if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(runtime)

    asyncio.run(main())
