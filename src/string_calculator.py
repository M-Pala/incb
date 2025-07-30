import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    parts = re.split(',|\n', numbers)
    return sum(map(int, parts))