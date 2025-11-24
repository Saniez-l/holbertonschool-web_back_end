#!/usr/bin/env python3
"""
Module that defines annotated list with float
values and return sum with float value
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of mixed list."""
    return sum(mxd_lst)
