#!/usr/bin/env python3

import asyncio

# Assuming wait_random is properly defined in the imported module
wait_random = __import__('0-basic_async_syntax').wait_random


async def main():
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

if __name__ == "__main__":
    asyncio.run(main())
