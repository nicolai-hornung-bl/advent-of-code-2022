def main():
    with open('door-8/input.txt', 'r') as input:
        trees = []
        for line in input:
            trees.append(list(map(int, list(line.strip()))))
        input.close()
        treesCoord = []
        for line in enumerate(trees):
            treesCoord.append([((line[0], y), h) for y, h in enumerate(line[1])])
        print(getVisibleTrees(treesCoord))
        print(getBestTreehouse(treesCoord))

def getBestTreehouse(trees):
    transposed = transpose(trees)
    max = 0
    for line in trees:
        for tree in line:
            score = getVisibleTreehouse(tree, trees[tree[0][0]], transposed[tree[0][1]])
            if score > max: 
                max = score
    return max

def getVisibleTreehouse(tree: tuple, line: list, column: list) -> int:
    score = 1
    directions = [
        line[line.index(tree):],
        list(reversed(line[:line.index(tree)+1])),
        column[column.index(tree):],
        list(reversed(column[:column.index(tree)+1]))
    ]
    for dir in directions:
        score*= getVisibleTreehouseLine(dir)
    return score

def getVisibleTreehouseLine(line: list) -> int:
    treehouse = line[0]
    line.remove(treehouse)
    if len(line) == 0:
        return 0
    visibility = 0
    for tree in line:
        if treehouse[1] > tree[1]:
            visibility += 1
        elif treehouse[1] <= tree[1]:
            visibility += 1
            break
    return visibility

def getVisibleTrees(trees) -> int:
    visible = set()
    transposed = transpose(trees)
    for line in enumerate(trees):
        visible.update(getVisibleLine(line))
        visible.update(getVisibleLine((line[0], reversed(line[1]))))
    for line in enumerate(transposed):
        visible.update(getVisibleLine(line))
        visible.update(getVisibleLine((line[0], reversed(line[1]))))
    return len(visible)

def getVisibleLine(line: list) -> set:
    visible = set()
    prev = ((-1,-1), -1)
    for tree in line[1]:
        if tree[1] > prev[1]:
            visible.add((tree[0]))
            prev = tree
    return visible

def transpose(trees):
    transposed = list()
    for i in range(len(trees[0])):
        row = list()
        for sublist in trees:
            row.append(sublist[i])
        transposed.append(row)
    return transposed

main()