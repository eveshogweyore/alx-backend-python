#!/usr/bin/env python3
"""A module to refactor function."""
import typing


# The types of the elements of the input are not known
def safe_first_element(
    lst: typing.Sequence[typing.Any]
) -> typing.Union[typing.Any, None]:
    """A refactored function to use type annotation."""
    if lst:
        return lst[0]
    else:
        return None
