import sys
program = [(inst, int(num)) for inst, num in \
           (line.strip().split() for line in sys.stdin)]

try:
    for n, instruction in enumerate(program):
        inst_obs, num_obs = instruction
        if  inst_obs == 'acc':
            continue

        program_shadow = program[:]
        program_shadow[n] = (['nop','acc'][inst_obs == 'nop'], num_obs)

        visited = set()
        acc = 0
        pc = 0

        while pc not in visited:
            visited.add(pc)
            inst, num = program_shadow[pc]
            pc += num*(inst == 'jmp') + (inst in ('acc', 'nop'))
            acc += num*(inst == 'acc')
except IndexError:
    pass

print(acc)
