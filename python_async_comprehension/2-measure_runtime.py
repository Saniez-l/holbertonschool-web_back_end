#!/usr/bin/env python3
"""
measure the total runtime and return it
"""

import asyncio
import time

# Import de la fonction de la tâche précédente
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension 4 time in parallèle via asyncio.gather.
    measure the total runtime and return it
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
