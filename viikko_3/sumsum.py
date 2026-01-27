def count_sum(numbers):
    total = 0

    for i, num in enumerate(numbers):
        total += num * (i+1) * (len(numbers)-i)

    return total




if __name__ == "__main__":
    print(count_sum([1, 2, 3])) # 20
    print(count_sum([42])) # 42
    print(count_sum([1, 1, 1, 1])) # 20
    print(count_sum([2, 1, 7, 8, 5, 1, 3, 1])) # 484

    numbers = list(range(1, 10**5))
    print(count_sum(numbers)) # 8333333332500000000