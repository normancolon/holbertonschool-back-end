#!/usr/bin/env python3
"""Module to sum a list containing both integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of integers and floats and return the sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats to sum.

    Returns:
        float: The sum of the elements in the list, converted to a float.
    """
    return float(sum(mxd_lst))
