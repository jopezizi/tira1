import random, time

def find_mode1(numbers):
    start = time.time()
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    end = time.time()
    return mode, end-start

def find_mode2(numbers):
    start = time.time()
    numbers.sort()
    mode = numbers[0]
    mode_c = 1

    cur_n = numbers[0]
    count = 1

    for i in range(1,len(numbers)):
        if numbers[i] == cur_n:
            count += 1
        else:
            if count > mode_c:
                mode_c = count
                mode = cur_n
            
            cur_n = numbers[i]
            count = 1
    end = time.time()
    return mode, end-start



sample = random.choices(range(1,1001),k=10**7)
print(find_mode1(sample))
print(find_mode2(sample))