#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> None:
    task = task_wait_random(max_delay)
    await task
    # Print the class of the task to confirm it's an asyncio.Task
    print(task.__class__)

asyncio.run(test(5))
