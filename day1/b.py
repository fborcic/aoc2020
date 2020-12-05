import sys
import itertools

entries = [int(l.strip()) for l in sys.stdin]
for a, b, c in itertools.product(entries, repeat=3):
    if a + b + c == 2020:
        print(a*b*c)
        break
