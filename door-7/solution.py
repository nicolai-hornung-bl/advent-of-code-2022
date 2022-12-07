import re

def main():
    with open('door-7/input.txt', 'r') as input:
        root = file('/', 0, list(), None, True)
        current = None
        for line in input:
            stripped = line.strip()
            if stripped == '$ ls':
                continue
            elif stripped.startswith('$ cd'):
                token = stripped.replace('$ cd ', '')
                if token == '/':
                    current = root
                elif token == '..':
                    current = current.parent
                else:
                    current = current.children[current.children.index(token)]
            elif stripped.startswith('dir'):
                current.children.append(file(stripped.replace('dir ', ''), 0, list(), current, True))
            else:
                current.children.append(file(stripped.replace(re.findall(r'\d+', stripped)[0], '').strip(), int(re.findall(r'\d+', stripped)[0]), None,   current, False))
        
        print(root.getSizeUnderTotal(100000))
        print(root.getDirsOver(30000000-(70000000-root.getSize()))[0])

class file:
    def __init__(self, name: str, size: int, children: list, parent: 'file', isdirectory: bool) -> None:
        self.name = name
        self.size = size
        self.children = children
        self.parent = parent
        self.isdirectory = isdirectory
    
    def __eq__(self, other) -> bool:
        return (self.name == other.name and self.isdirectory == other.isdirectory)

    def __eq__(self, other: str) -> bool:
        return self.name == other

    def __repr__(self) -> str:
        if self.isdirectory: return f'dir {self.name} {len(self.children)} {self.getSize()}'
        else: return f'{self.name} {self.size}'

    def getSize(self) -> int:
        if not self.isdirectory:
            return self.size
        elif len(self.children) == 0:
            return 0
        else: 
            sum = 0
            for child in self.children:
                sum += child.getSize()
            return sum

    def getChildrenFlat(self) -> list:
        children = list()
        for child in self.children:
            children.append(child)
            if child.isdirectory: children.extend(child.getChildrenFlat())
        return children

    def getDirsOver(self, min: int) -> list:
        return sorted(list(filter(lambda x, min=min: x.isdirectory and x.getSize() >= min, self.getChildrenFlat())), key=lambda y: y.getSize())

    def getSizeUnderTotal(self, max: int) -> int:
        sum = 0
        for child in filter(lambda x: x.isdirectory, self.getChildrenFlat()):
            if child.getSize() <= max: sum += child.getSize()
        return sum

main()