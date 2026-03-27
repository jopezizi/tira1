class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_tree(grid):


    
if __name__ == "__main__":
    grid = [r"...........",
            r"...........",
            r"......5....",
            r"...../.\...",
            r"....3...\..",
            r"....|....1.",
            r"....2......"]
    tree = find_tree(grid)
    print(tree)
    # Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = [r"....1.....",
            r".../.\....",
            r"..2...\...",
            r"..|....3..",
            r"..7.../|\.",
            r"./.\.4.5.6",
            r"8...9....."]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])