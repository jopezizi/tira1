from itertools import permutations

def count_numbers(length, numbers):
    nums = sorted([int(d) for d in numbers if int(d) > 0])
    
    if length == 1:
        return len(numbers)
    
    seen = {}

    def incr(left, last):
        if left == 0:
            return 1
        
        curr = (left, last)
        if curr in seen:
            return seen[curr]
        
        count = 0
        for num in nums:
            if num >= last:
                count += incr(left-1,num)
        
        seen[curr] = count
        return count
        
    return incr(length, -1)

if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758