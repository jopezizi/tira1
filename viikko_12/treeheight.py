class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.max_depth = 0
            return

        node = self.root
        depth = 0

        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    if depth + 1 > self.max_depth:
                        self.max_depth = depth + 1
                    node.left = Node(value)
                    return
                node = node.left
                depth += 1
            else:
                if not node.right:
                    if depth + 1 > self.max_depth:
                        self.max_depth = depth + 1
                    node.right = Node(value)
                    return
                node = node.right
                depth += 1

    def height(self):
        return self.max_depth

if __name__ == "__main__":
    numbers = TreeSet()
    numbers.add(3)
    print(numbers.height())
    numbers.add(2)
    print(numbers.height())
    numbers.add(6)
    print(numbers.height())
    numbers.add(4)
    print(numbers.height())
    numbers.add(3)
    print(numbers.height())
    numbers.add(1)
    print(numbers.height())