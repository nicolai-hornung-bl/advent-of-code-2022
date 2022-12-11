import re

def main():
    with open('door-10/input.txt', 'r') as input:
        r1 = 1
        program = [l.strip().split(' ') for l in input]
        input.close()
    
    pc_b = -1
    pc = 0
    cycle = 0
    signal_strength = list()
    pos = (0, 0)
    print(f'Cycle {cycle+1}\t\t-> ', end='')
    while True:
        if pc == len(program): break
        cycle +=1
        signal_strength.append((cycle, r1, cycle*r1))

        if abs(r1-pos[0]) <= 1: 
            print('#', end='')
        else:
            print('.', end='')
        if pos[0] == 39:
            pos = (0, pos[1]+1)
            print(f' <- Cycle {cycle}')
            print(f'Cycle {cycle+1}\t-> ', end='')
        else:
            pos = (pos[0]+1, pos[1])

        if program[pc][0] == 'noop':
            pc_b = pc
            pc += 1
        elif program[pc][0] == 'addx':
            if pc_b != pc:
                pc_b = pc
            else:
                r1 += int(program[pc][1])
                pc_b = pc
                pc += 1
    interest = [20, 60, 100, 140, 180, 220]
    print('\n')
    for x in interest: print(f'Cycle {x}: {signal_strength[x-1]}')
    print(sum([signal_strength[i-1][2] for i in interest]))

main()