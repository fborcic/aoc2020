import sys
import re

rules = [('byr', lambda v: v.isdigit() and 1920 <= int(v) <= 2002),
         ('iyr', lambda v: v.isdigit() and 2010 <= int(v) <= 2020),
         ('eyr', lambda v: v.isdigit() and 2020 <= int(v) <= 2030),
         ('hgt', lambda v: v[:-2].isdigit() and
             (v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193 or
              v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76)),
         ('hcl', lambda v: re.search(r'^#[\da-f]{6}$', v) is not None),
         ('ecl', lambda v: v in 'amb blu brn gry grn hzl oth'.split()),
         ('pid', lambda v: len(v) == 9 and v.isdigit())]

def check_rule(rule, passport):
    label, func = rule
    match = re.search(label+':(\S*)', passport)
    return match is not None and func(match.group(1))

print(sum(
       all(check_rule(rule, passport) for rule in rules) \
        for passport in sys.stdin.read().split('\n\n')))

