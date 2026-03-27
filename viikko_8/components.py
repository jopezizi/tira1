class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def visit(self, node, components, counter):
        if node in components:
            return
        components[node] = counter

        for next_node in self.graph[node]:
            self.visit(next_node, components, counter)

def find_components(nodes, edges):
        c = Components(nodes)
        for e1, e2 in edges:
            c.add_edge(e1,e2)
        counter = 0
        components = {}

        for node in c.nodes:
            if node not in components:
                counter += 1
                c.visit(node, components, counter)
        result = [[] for i in range (max(components.values()))]  
        for node in components:
            result[components[node] -1 ].append(node)

        for sub in result:
            sub.sort()
        return result


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]