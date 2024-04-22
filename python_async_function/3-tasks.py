#!/usr/bin/env python3
'''
Function that creates an asyncio Task from an asynchronous coroutine.
'''
import asyncio

# Adjust the import path as needed for your project structure
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Creates and returns an asyncio.Task which completes after a random delay.

    Args:
    max_delay (int): The maximum delay in seconds that the wait_random coroutine can wait.

    Returns:
    asyncio.Task: A task that will complete after the wait_random coroutine has finished.
    """
    return asyncio.create_task(wait_random(max_delay))
