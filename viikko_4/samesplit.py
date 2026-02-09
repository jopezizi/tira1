def count_splits(numbers):
    left = {}
    right = {}
    common = 0  
    count = 0
    for r in range(len(numbers)):
        if numbers[r] not in right:
            right[numbers[r]] = 0
        right[numbers[r]] += 1
    
    left_d= set()
    right_d= set(right.keys())

    for l in range(len(numbers)):
        if numbers[l] not in left:
            left[numbers[l]] = 0
            left_d.add(numbers[l])
        left[numbers[l]] += 1
        right[numbers[l]] -= 1

        if right[numbers[l]] == 0:
            right.pop(numbers[l])
            right_d.remove(numbers[l])
        
        if left_d == right_d:
            count += 1
    
    return count

if __name__ == "__main__":
    print(count_splits([1, 4, 4]))
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1