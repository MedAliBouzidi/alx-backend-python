#!/usr/bin/env python3
"""
    This module contains a function that takes a string k and an int OR float v
    as arguments and returns a tuple. The first element of the tuple is
    the string k and the second element is the square of the int OR float v.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function returns a tuple containing the string k
    and the square of the int OR float v.
    """
    return (k, v**2)
