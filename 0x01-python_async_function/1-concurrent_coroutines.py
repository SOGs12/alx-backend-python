#!/usr/bin/env python3
"""
This contains the wait_n function
"""
import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """
    wait_n should return the list of all the delays (float values)
    The list of the delays should be in ascending order
    without using sort() because of concurrency.
    :param n:
    :param max_delay:
    :return:
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
