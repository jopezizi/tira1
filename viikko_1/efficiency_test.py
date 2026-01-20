import random, time

numbers = [random.randint(0,100) for n in range(10**7)]
# toteutus 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

# testi toteutus 1
start = time.time()
test1 = count_even1(numbers)
end = time.time()
print("Toteutus 1 tulos:", test1, "Aika:", end-start, "s")

# testi toteutus 2
start = time.time()
test1 = count_even2(numbers)
end = time.time()
print("Toteutus 2 tulos:", test1, "Aika:", end-start, "s")