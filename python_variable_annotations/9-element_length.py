#!/usr/bin/env python3
"""Module to calculate the length of elements in an iterable."""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Generate a list of tuples containing items and their lengths from an iterable.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (like strings or lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence from `lst`
                                    and its length.
    """
    return [(i, len(i)) for i in lst]
