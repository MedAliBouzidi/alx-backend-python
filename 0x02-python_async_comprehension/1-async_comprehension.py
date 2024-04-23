#!/usr/bin/env python3
""" 1. Async Comprehension """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers.
    """
    return [num async for num in async_generator()]
