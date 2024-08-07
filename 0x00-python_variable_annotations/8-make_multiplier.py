#!/usr/bin/env python3
"""A simple module to demonstrate complex types."""
import typing


def make_multiplier(
    multiplier: float
) -> typing.Callable[[float], float]:
    """A simple function to demonstrate complex types."""
    return lambda n: n * multiplier
