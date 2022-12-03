from functools import total_ordering

@total_ordering
class elf:
    def __init__(self, food):
        self.food = food

    def __str__(self):
        return f"Food: {self.food}, Calories: {self.getTotalCalories()}"

    def __lt__(self, other):
        return self.getTotalCalories() < other.getTotalCalories()
        
    def __eq__(self, other):
        return self.getTotalCalories() == other.getTotalCalories()
    
    def getTotalCalories(self):
        return sum(self.food)

    def addFood(self, item):
        self.food.append(item)

elves = []

with open('door-1/input.txt', 'r') as input:
    items = []
    for line in input:
        if line.strip():
            items.append(int(line))
        else:
            if len(items) > 0:
                elves.append(elf(items))
                items = []
    input.close

for elf in elves:
    print(elf)

print()

print(max(elves))

print()

print(sum(map(lambda elf: elf.getTotalCalories(), sorted(elves)[-3:])))