import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ',|\n'
    if numbers.startswith("//"):
        delimiter_part, numbers = numbers[2:].split('\n', 1)
        delimiter = re.escape(delimiter_part)

    parts = re.split(delimiter, numbers)
    return sum(map(int, parts))