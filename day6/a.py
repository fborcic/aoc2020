import sys

print(sum(
    len(set(chunk)-{'\n'}) for chunk in sys.stdin.read().split('\n\n')))
