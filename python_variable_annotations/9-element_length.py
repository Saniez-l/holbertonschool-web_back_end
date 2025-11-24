#!/usr/bin/env python3
"""
Module that defines a type-annotated function element_length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, each containing an element from lst
    and its length.
    """
    return [(i, len(i)) for i in lst]
