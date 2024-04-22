#!/usr/bin/env python3
"""Module to create a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Generate a function that multiplies its input by a predefined multiplier.

    Args:
        multiplier (float): The multiplier to apply in the generated function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the result of multiplying
                                  it by the `multiplier`.
    """
    def multiplier_function(value: float) -> float:
        """Multiply a float by the outer multiplier.

        Args:
            value (float): A float to multiply.

        Returns:
            float: The product of the input value and the multiplier.
        """
        return value * multiplier

    return multiplier_function
