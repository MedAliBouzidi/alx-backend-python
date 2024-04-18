#!/usr/bin/env python3
"""
    This module contains a function that takes a list of mixed
    floats and integers as argument and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function returns the sum of a list of mixed floats and integers."""
    return sum(mxd_lst)
