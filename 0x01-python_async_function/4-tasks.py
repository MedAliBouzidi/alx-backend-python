#!/usr/bin/env python3
""" Multiple concurrent coroutines """
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a random delay between 0 and max_delay n times,
    return list of delays
    """
    task_wait_random = __import__("3-tasks").task_wait_random
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
