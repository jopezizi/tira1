def connected(nodes, edges):
    graph = {node: [] for node in nodes}
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    seen = set()
    dfs(nodes[0], graph, seen)
    return len(nodes) == len(seen)
def dfs(node, graph, seen):
    if node in seen:
        return
    seen.add(node)

    for next_n in graph[node]:
        dfs(next_n, graph, seen)


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges)) # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges)) # True 