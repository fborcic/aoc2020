import sys
import re

cnt = 0
for line in sys.stdin:
    min_, max_, letter, pwd = \
            re.search('^(\d*)-(\d*) (.): (.*)$', line.strip()).groups()
    cnt += int(min_) <= pwd.count(letter) <= int(max_)

print(cnt)
