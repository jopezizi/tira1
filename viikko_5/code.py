import time, random


def count_dict(numbers):
    start = time.time()
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1
    end = time.time()
    return rounds, end-start

def count_list(numbers):
    start = time.time()
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1
    end = time.time()
    return rounds, end-start

numbers = list(range(1,10**7))
random.shuffle(numbers)

print(count_dict(numbers))
print(count_list(numbers))