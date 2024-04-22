#!/usr/bin/env python3
""" Return a Syncio task """


from asyncio import Task, create_task


def task_wait_random(max_delay: int) -> Task:
    """Return a Syncio task"""
    wait_random = __import__("0-basic_async_syntax").wait_random
    return create_task(wait_random(max_delay))
