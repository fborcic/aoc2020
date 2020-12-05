import sys
print(sum(line.strip()[n*3%(len(line)-1)] == '#' \
    for n, line in enumerate(sys.stdin)))
