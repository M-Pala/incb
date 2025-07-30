import re

def extract_delimiters(header: str) -> str:
    if header.startswith('['):
        # multiple delimiters or long ones
        delimiters = re.findall(r'\[([^]]+)\]', header)
        return '|'.join(map(re.escape, delimiters))
    return re.escape(header)

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ',|\n'
    if numbers.startswith("//"):
        header, numbers = numbers[2:].split('\n', 1)
        delimiter = extract_delimiters(header)

    parts = re.split(delimiter, numbers)
    nums = list(map(int, parts))
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {','.join(map(str, negatives))}")
    return sum(n for n in nums if n <= 1000)