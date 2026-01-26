def count_sublists(numbers):
    counter = 0
    evenstreak = 0
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 2 == 0:
            evenstreak += 1
        else:
            counter += (evenstreak*(evenstreak+1)) // 2
            evenstreak = 0
    counter += (evenstreak*(evenstreak+1)) // 2
    return counter

if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000