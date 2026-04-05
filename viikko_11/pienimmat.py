import random, heapq, time

def test1(numbers):
    start = time.time()
    nums = sorted(numbers)
    result = 0

    for i in range(len(nums)//10):
        result += nums[i]
    
    end = time.time()
    return f"TESTI 1: Tulos: {result}, Aika: {end - start} sekuntia"

def test2(numbers):
    start = time.time()
    heap = []
    num_copy = list(numbers)

    for x in num_copy:
        heapq.heappush(heap, x)

    result = 0

    for i in range(len(numbers)//10):
        h = heapq.heappop(heap)
        result += h
    end = time.time()
    return f"TESTI 2: Tulos: {result}, Aika: {end - start} sekuntia"

def test3(numbers):
    start = time.time()
    num_copy = list(numbers)
    heapq.heapify(num_copy)

    result = 0
    for i in range(len(numbers)//10):
        h = heapq.heappop(num_copy)
        result += h

    end = time.time()
    return f"TESTI 3: Tulos: {result}, Aika: {end - start} sekuntia"

random.seed(1)
n = 10 ** 7
sample = range(1,10**9+1)
numbers = random.sample(sample,n)
print(test1(numbers))
print(test2(numbers))
print(test3(numbers))
