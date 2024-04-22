#!/usr/bin/env python3
'''
Function to create multiple asyncio tasks and return their results.
'''
import asyncio

# Make sure to adjust the import statement based on your project structure
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Creates and gathers multiple tasks using task_wait_random and returns the results.

    Args:
    n (int): Number of tasks to create.
    max_delay (int): Maximum delay to use in task_wait_random calls.

    Returns:
    list: A list of float values representing the delays, in order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return sorted(completed_delays)
