import sys
import itertools

entries = [int(l.strip()) for l in sys.stdin]
for a, b in itertools.product(entries, repeat=2):
    if a + b == 2020:
        print(a*b)
        break
