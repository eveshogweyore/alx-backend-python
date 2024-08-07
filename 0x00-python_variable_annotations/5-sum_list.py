#!/usr/bin/env python3
"""A sum of floats module."""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """A sum of floats function."""
    result: float = 0.0
    for number in input_list:
        result += number
    return result
