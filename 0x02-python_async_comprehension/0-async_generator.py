#!/usr/bin/env python3
""" 0. Async Generator """
import asyncio
import random


async def async_generator():
    """
    Function that loops 10 times, each time asynchronously yields a random
    number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)