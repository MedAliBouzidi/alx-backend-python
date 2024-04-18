#!/usr/bin/env python3
"""
    This module contains a function that returns the first element
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function returns the first element of a sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
