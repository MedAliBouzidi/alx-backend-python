#!/usr/bin/env python3
"""
    This module contains a function that returns
    the value of a key in a dictionary.
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    This function returns the value of a key in a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
