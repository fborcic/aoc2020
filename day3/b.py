import sys

res = 1
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
lines = [l.strip() for l in sys.stdin]

for right, down in slopes:
    res *= sum(lines[y][right*y//down % len(lines[y])] == '#' \
             for y in range(0, len(lines), down))

print(res)
