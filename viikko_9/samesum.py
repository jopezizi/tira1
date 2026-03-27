import itertools

def check_sum(numbers):
    target = sum(numbers) // 2
    check = False

    if sum(numbers) % 2 != 0:
        return check
    
    for i in range(1,len(numbers)+1):
        for c in itertools.combinations(numbers,i):
            if sum(c) == target:
                check = True
                break
    
    return check






if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4])) # True
    print(check_sum([1, 2, 3, 5])) # False
    print(check_sum([0])) # True
    print(check_sum([2, 2])) # True
    print(check_sum([2, 4])) # False
    print(check_sum([1, 5, 6, 3, 5])) # True
    print(check_sum([1, 5, 5, 3, 5])) # False
    print(check_sum([10**9, 2*10**9, 10**9])) # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123])) # False