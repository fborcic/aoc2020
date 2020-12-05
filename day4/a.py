import sys

required = 'byr iyr eyr hgt hcl ecl pid'.split()
print(sum(all(w+':' in passport for w in required)\
        for passport in sys.stdin.read().split('\n\n')))

