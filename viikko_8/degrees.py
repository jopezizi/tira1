def find_degrees(nodes, edges):
    degrees = {}
    for d1, d2 in edges:
        if d1 not in degrees:
            degrees[d1] = 1
        else:
            degrees[d1] += 1
    
        if d2 not in degrees:
            degrees[d2] = 1
        else:
            degrees[d2] += 1

    result = [item for item in degrees.values()]
    if len(result) < len(nodes):
        for i in range(len(nodes)-len(result)):
            result.append(0)
    return sorted(result)

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(find_degrees(nodes, edges)) # [2, 2, 3, 3, 4]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_degrees(nodes, edges)) # [0, 0, 0, 0, 0]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_degrees(nodes, edges)) # [1, 1, 1, 1, 4]

    nodes = [1,2,3]
    edges = [(2,3)]
    print(find_degrees(nodes, edges))