import sys
import re

cnt = 0
for line in sys.stdin:
    a, b, letter, pwd = \
            re.search('^(\d*)-(\d*) (.): (.*)$', line.strip()).groups()
    a, b = int(a)-1, int(b)-1
    cnt += (pwd[a:a+1] == letter) != (pwd[b:b+1] == letter)

print(cnt)
