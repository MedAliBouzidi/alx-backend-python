#!/usr/bin/env python3
""" Multiple concurrent coroutines """
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a random delay between 0 and max_delay n times,
    return list of delays
    """
    wait_random = __import__("0-basic_async_syntax").wait_random
    return [await wait_random(max_delay) for _ in range(n)]
