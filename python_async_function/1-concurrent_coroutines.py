#!/usr/bin/env python3
'''
Async coroutine that spawns multiple wait_random coroutines and returns their results in order of completion.
'''
import asyncio
from random import uniform

# Make sure to adjust the import statement based on your project structure
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawn wait_random coroutine n times with the specified max_delay.
    Returns a list of delays in the order that the tasks complete.

    Args:
    n (int): Number of times to spawn wait_random.
    max_delay (int): Maximum delay to pass to wait_random.

    Returns:
    list: A list of float values representing the delays, in order of completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = []
    for future in asyncio.as_completed(tasks):
        result = await future
        completed_delays.append(result)
    return completed_delays
