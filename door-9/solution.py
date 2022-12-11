import re

def main():
    with open('door-9/input.txt', 'r') as input:
        rope = [(0, 0) for x in range(10)]
        tailVisited = set()
        tailVisited.add(rope[1])
        tail2Visited = set()
        tail2Visited.add(rope[-1])
        for line in input:
            stripped = line.strip()
            instruction = (stripped.replace(re.findall(r'\d+', stripped)[0], '').strip(), int(re.findall(r'\d+', stripped)[0]))
            for x in range(instruction[1]):
                if instruction[0] == 'R':
                    rope[0] = (rope[0][0]+1, rope[0][1])
                elif instruction[0] == 'U':
                    rope[0] = (rope[0][0], rope[0][1]+1)
                elif instruction[0] == 'L':
                    rope[0] = (rope[0][0]-1, rope[0][1])
                elif instruction[0] == 'D':
                    rope[0] = (rope[0][0], rope[0][1]-1)
                for i, knot in enumerate(rope[1:]):
                    rope[i+1] = evaluate(rope[i], knot)
                tailVisited.add(rope[1])
                tail2Visited.add(rope[-1])
        input.close()
        print(len(tailVisited))
        print(len(tail2Visited))

def move(diff: int) -> int:
    move = 1
    if diff == 0: move = 0
    elif diff % 2 == 0: move = diff/2
    else: move = diff
    return int(move)
    
def evaluate(head, tail) -> tuple:
    difference = ((head[0] - tail[0]), (head[1] - tail[1]))
    if abs(difference[0]) < 2 and abs(difference[1]) < 2 : 
        return tail
    delta = tuple(map(move, difference))
    return (tail[0] + delta[0], tail[1] + delta[1])

def printResult(tailVisited):
    size = (max(map(lambda x: x[0], tailVisited))+2,max(map(lambda x: x[1], tailVisited))+2)
    for y in range(size[1], 0, -1):
        print(f'{y-1}: ', end='')
        for x in range(size[0]):
            if (x,y-1) in tailVisited: print('#', end='')
            else: print('.', end='')
        print()
    print(f'   {"".join(map(str, list(range(size[0]))))}')

def printMatrix(head, tail, instruction):
    size = (max(head[0], tail[0])+3, max(head[1], tail[1])+3)
    for y in range(size[1], 0, -1):
        print(f'{y-1}: ', end='')
        for x in range(size[0]):
            if (x, y-1) == head:
                print('H', end='')
            elif (x, y-1) == tail:
                print('T', end='')
            else: print('.', end='')
        print()
    print(f'   {"".join(map(str, list(range(size[0]))))}')
    print(f'Head: {head} Tail: {tail} Instruction: {instruction}')
    print()

main()