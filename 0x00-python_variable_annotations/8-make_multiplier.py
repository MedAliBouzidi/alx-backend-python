#!/usr/bin/env python3
"""
    This module contains a function that takes a float multiplier as argument
    and returns a function that multiplies a float by the multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function returns a function that multiplies a float by the multiplier.
    """
    return lambda x: x * multiplier
