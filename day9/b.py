import itertools
import sys

numbers = [int(line.strip()) for line in sys.stdin]
first = next(n for i,n in enumerate(numbers[25:]) if n not in \
            {sum(c) for c in itertools.combinations(numbers[i:i+25], 2)})

start, end = None, None
for i, n in enumerate(numbers):
    for j in range(len(numbers)-i):
        current = sum(numbers[i:i+j])
        if current == first:
            start, end = i, i+j
        elif current > first:
            break

    if start is not None:
        break

print(min(numbers[start:end])+max(numbers[start:end]))
