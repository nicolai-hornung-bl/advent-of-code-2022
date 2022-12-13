import re

class monkey:

    def __init__(self, starting_items: list, operation, test) -> None:
        self.items = starting_items
        self.op_string = operation
        self.test_params = test
        self.count = 0

    def operation(self, x):
        return eval(self.op_string)
    
    def test(self, item):
        return self.test_params[0] if item % self.test_params[1] == 0 else self.test_params[2]

    def incr(self):
        self.count += 1
    
    def __repr__(self):
        return f'Items: {self.items}'


with open('door-11/input.txt', 'r') as input:
    monkey_string = list(map(lambda y: list(filter(lambda z: z != '', map(str.strip, y.split('\n')))), filter(lambda x: x != '', re.split("Monkey \d+:\n", " ". join([line for line in input])))))
    monkeys = []
    supermodulo = 1
    for m in monkey_string:
        operation = str(m[1].split('=')[1].strip().replace('old', 'x'))
        test = (int(re.findall('\d+', m[3])[0]), int(re.findall('\d+', m[2])[0]), int(re.findall('\d+', m[4])[0]))
        supermodulo *= test[1]
        monkeys.append(
            monkey(
                starting_items=list(map(int, re.findall('\d+', m[0]))),
                operation=operation,
                test=test
            )
        )

rounds = 10000

for round in range(1, rounds+1):
    for m in monkeys:
        for item in m.items:
            item = m.operation(item)
            item = int(item % supermodulo)
            #  item = int(item /3)
            monkeys[m.test(item)].items.append(item)
            m.incr()
        m.items = []

counts = sorted(list(map(lambda m: m.count, monkeys)), reverse=True)
print(counts[0] * counts[1])