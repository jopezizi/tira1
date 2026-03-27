import itertools

def find_route(distances):
    cities = len(distances)
    perm = itertools.permutations(range(cities))
    mindist = 100000
    route = []
    for p in perm:
        c_route = [1]
        if p[0] != 0:
            continue
        dist = 0
        for i in range(len(p)-1):
            start = p[i]
            end = p[i+1]
            trip = distances[start][end]
            dist += trip
            c_route.append(p[i+1]+1)
        
        dist += distances[p[-1]][0]
        c_route.append(1)
        if dist < mindist:
            mindist = dist
            route = c_route
    
    return mindist, route







if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]