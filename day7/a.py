import sys
import re

inverse_rules = {}
to_check = set()
for line in sys.stdin:
    key, rest = re.search(r'^([a-z ]*) bags contain ([\w\s,]*).$', line).groups()
    allowed = set(re.findall(r'\d* ([a-z ]*) bags?,?', rest))
    for color in allowed:
        if color in inverse_rules:
            inverse_rules[color].add(key)
        else:
            inverse_rules[color] = {key,}
    if 'shiny gold' in allowed:
        to_check.add(key)

possibilities = set()
while to_check:
    possibilities.update(to_check)
    to_check_next = set()
    for bag in to_check:
        if bag in inverse_rules:
            to_check_next.update(inverse_rules[bag])
    to_check = to_check_next

print(len(possibilities))



