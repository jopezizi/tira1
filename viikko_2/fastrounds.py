def count_rounds(numbers):
    rounds = 1

    pos = {}
    for i, num in enumerate(numbers):
        pos[num] = i

    for num in range(2, len(numbers)+1):
        if pos[num] < pos[num-1]:
            rounds += 1
    
    return rounds

if __name__ == "__main__":
    print(count_rounds([2,5,4,1,3])) # 4
    print(count_rounds([3,1,2])) # 2
    print(count_rounds([1,2,3,4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000