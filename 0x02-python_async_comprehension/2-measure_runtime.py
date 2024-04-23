#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions """
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather. and return the elapsed time.
    """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return asyncio.get_event_loop().time() - start
