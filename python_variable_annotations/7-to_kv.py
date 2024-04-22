#!/usr/bin/env python3
"""Module to create a tuple with a string and the square of a number."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple consisting of a string and the square of a number.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to square and include as a float in the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k` and the second element
                           is the square of `v` as a float.
    """
    return (k, float(v**2))
