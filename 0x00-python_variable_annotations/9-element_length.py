#!/usr/bin/env python3
"""
    This module contains a function that takes a Iterable sequence as argument
    and returns the length of the sequence as a Tuple.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function returns a list of tuples containing the sequence
    and the length of the sequence.
    """
    return [(i, len(i)) for i in lst]
