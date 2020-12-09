import itertools
import sys

numbers = [int(line.strip()) for line in sys.stdin]
print(next(
    n for i,n in enumerate(numbers[25:]) if n not in \
            {sum(c) for c in itertools.combinations(numbers[i:i+25], 2)}))
