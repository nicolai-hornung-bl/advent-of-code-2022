with open('door-5/input.txt', 'r') as input:
    ship1 = []
    ship2 = []
    for line in input:
        if "move" in line:
            ins = list(map(int, line.strip().replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")))
            for x in range(ins[0]):
                ship1[ins[2]-1].append(ship1[ins[1]-1].pop())
            ship2[ins[2]-1].extend(ship2[ins[1]-1][-ins[0]:])
            ship2[ins[1]-1] = ship2[ins[1]-1][:-ins[0]]
        else:
            for c in map(lambda y: (int((y[0]-1)/4), y[1]), filter(lambda x: (x[0] - 1) % 4 == 0, enumerate(line))):
                if len(ship1) < c[0] + 1: ship1.append([])
                if len(ship2) < c[0] + 1: ship2.append([])
                if c[1].isalpha(): 
                    ship1[c[0]].insert(0, c[1])
                    ship2[c[0]].insert(0, c[1])
    print(ship1)
    print("".join(list(map(lambda x: x[-1], ship1))))
    print(ship2)
    print("".join(list(map(lambda x: x[-1], ship2))))
    input.close()