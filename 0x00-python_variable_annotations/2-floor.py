#!/usr/bin/env python3
"""A math floor module."""


def floor(n: float) -> int:
    """A math floor function."""
    if isinstance(n, int):
        return n

    if n > 0:
        return int(n)
    else:
        t_n = int(n)
        if n != t_n:
            return t_n - 1
        else:
            return t_n
