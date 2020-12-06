import sys

print(sum(
    len(set.intersection(*[set(line) for line in chunk.strip().split('\n')])) \
            for chunk in sys.stdin.read().split('\n\n')))
