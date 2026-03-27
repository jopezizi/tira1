import itertools as it

def min_count(weights, max_weight):
    if not weights:
        return 0
    
    if any(weight > max_weight for weight in weights):
        return -1
    
    min_count = len(weights) + 1

    for p in it.permutations(weights):
        boxcount = 1
        current = 0

        for weight in p:
            if current + weight <= max_weight:
                current += weight
            else:
                boxcount +=1
                current = weight

        min_count = min(min_count, boxcount)

    return min_count


if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3