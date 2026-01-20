def count_rounds(numbers):
    rounds = 0
    find = 1
    for num in numbers:
        if num == find:
            find += 1
        else:
            rounds += 1
            if num == find:
                find += 1
    rounds += 1
    return rounds


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000