import sys
import re

def bagfs(bag, rules):
    return rules[bag] == [] or 1+sum(n*bagfs(subbag, rules) for n, subbag in rules[bag])

rules = {}
for line in sys.stdin:
    key, rest = re.search(r'^([a-z ]*) bags contain ([\w\s,]*).$', line).groups()
    inside = re.findall(r'(\d+) ([a-z ]*) bags?,?', rest)
    rules[key] = [(int(n), name) for n, name in inside]

print(bagfs('shiny gold', rules)-1)


