#!/usr/bin/env python3
"""A sum of floats module."""


def sum_list(input_list: list[float]) -> float:
    """A sum of floats function."""
    result: float = 0.0
    for number in input_list:
        result += number
    return result
