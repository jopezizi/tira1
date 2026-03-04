def count_pairs(numbers):
    nums = sorted(numbers)
    
    left = 0
    right = (len(nums)+1)//2
    count = 0

    while left < (len(nums)+1)//2 and right < len(nums):
        if nums[left] * 2 <= nums[right]:
            count += 1
            left +=1
            right +=1
        else:
            right +=1
    
    return count
if __name__ == "__main__":
    print(count_pairs([44,32,39,77])) # 1
    print(count_pairs([14,8,20])) # 1
    print(count_pairs([4,8,52])) # 1
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176