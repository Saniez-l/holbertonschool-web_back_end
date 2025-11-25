#!/usr/bin/env python3
"""
Execute multiple tasks created by task_wait_random
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return delays in ascending order."""

    tasks = []
    delays = []

    # créer n tasks
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    # récupérer les résultats dans l'ordre d'exécution
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
