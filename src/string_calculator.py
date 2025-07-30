import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ',|\n'
    if numbers.startswith("//"):
        delimiter_part, numbers = numbers[2:].split('\n', 1)
        delimiter = re.escape(delimiter_part)

    parts = re.split(delimiter, numbers)
    nums = list(map(int, parts))

    negatives = [n for n in nums if n < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {','.join(map(str, negatives))}")

    return sum(n for n in nums if n <= 1000)