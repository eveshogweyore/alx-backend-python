#!/usr/bin/env python3
"""A duck type iterable object module."""
import typing


def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """A duck type iterable object function."""
    return [(i, len(i)) for i in lst]
