import sys
program = [(inst, int(num)) for inst, num in \
           (line.strip().split() for line in sys.stdin)]

visited = set()
acc = 0
pc = 0

while pc not in visited:
    visited.add(pc)
    inst, num = program[pc]
    pc += num*(inst == 'jmp') + (inst in ('acc', 'nop'))
    acc += num*(inst == 'acc')

print(acc)
