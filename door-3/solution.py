def getPrio(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

def getCommon(lines):
    temp = list(map(set, lines))
    return temp[0].intersection(*temp[1:]).pop()

with open('door-3/input.txt', 'r') as input:
    sum1 = 0
    sum2 = 0
    group = []
    for line in input:
        sum1 += getPrio(getCommon([line[0:int((len(line)/2))], line[int((len(line))/2):]]))
        if len(group) < 2:
            group.append(line.strip())
        else:
            group.append(line.strip())
            sum2 += getPrio(getCommon(group))
            group = []
    input.close
    print(sum1)
    print(sum2)
