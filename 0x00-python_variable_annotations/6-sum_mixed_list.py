#!/usr/bin/env python3
"""A simple addition module."""
import typing


def sum_mixed_list(
    mxd_lst: typing.List[typing.Union[int, float]]
) -> float:
    """A simple addition function."""
    result: float = 0.0
    for number in mxd_lst:
        result += number
    return result
