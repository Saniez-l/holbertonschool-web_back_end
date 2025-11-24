#!/usr/bin/env python3
"""
Module  a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return internal"""
    """indique que la fonction retourne une fonction (Callable)
    qui prend un float et retourne un float."""
    def internal(number: float):
        """Return number * multiplier"""
        """utiliser le multiplier défini dans la
        fonction externe, c'est ce qu'on appelle une closure."""
        return number * multiplier
    return internal
