import sys

t = str.maketrans('FBLR', '0101')
print(max(int(line.translate(t), 2) for line in sys.stdin))
