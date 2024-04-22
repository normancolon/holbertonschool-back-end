#!/usr/bin/env python3
"""Module to compute the floor of a float."""

from math import floor as math_floor


def floor(n: float) -> int:
    """Calculate the floor of a floating-point number and return it as an integer.

    Args:
        n (float): The floating-point number for which to find the floor.

    Returns:
        int: The floor of the number.
    """
    return math_floor(n)
