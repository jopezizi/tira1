def find_rounds(numbers):
    rounds = []
    numbers_set = set(numbers)
    find = 1
    while numbers_set:
        round = []
        for num in numbers:
            if num == find:
                round.append(num)
                find += 1
                numbers_set.remove(num)
        rounds.append(round)
    return rounds



if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]