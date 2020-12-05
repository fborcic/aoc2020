import sys

t = str.maketrans('FBLR', '0101')
existing = {int(line.translate(t), 2) for line in sys.stdin}
print(next(
    i for i in range(min(existing), max(existing)+1)\
            if i not in existing
    ))
