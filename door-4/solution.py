with open('door-4/input.txt', 'r') as input:
    total_subsets = 0
    total_overlaps = 0
    for line in input:
        # Gets line into "[[14, 15], [14, 41]]" format
        parseline = [list(map(int, item)) for item in list(map(lambda x: x.split('-'), line.strip().split(',')))]
        # Enumerates each section range into a set
        sets = [set(range(item[0], item[1] + 1)) for item in parseline]
        # Check if assignments are subsets of each other
        if sets[0].issubset(sets[1]) or sets[1].issubset(sets[0]): total_subsets += 1
        # Check if assignments aren't disjoint
        if not sets[0].isdisjoint(sets[1]): total_overlaps += 1
    print(total_subsets) 
    print(total_overlaps)