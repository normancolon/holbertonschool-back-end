#!/usr/bin/env python3
'''
Function to measure the execution time of an asynchronous routine.
'''
import asyncio
import time

# Make sure to adjust the import statement based on your project structure
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n with given parameters and calculates the average time per call.

    Args:
    n (int): The number of concurrent calls to wait_n.
    max_delay (int): The maximum delay to use in wait_random calls inside wait_n.

    Returns:
    float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
