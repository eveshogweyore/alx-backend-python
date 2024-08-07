#!/usr/bin/env python3
"""A simple module to demostrate complex types."""
import typing


def to_kv(
    k: str,
    v: typing.Union[int, float]
) -> typing.Tuple[str, float]:
    """A simple function to demonstrate complex types."""
    return (k, v ** 2)
