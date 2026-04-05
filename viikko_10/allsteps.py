
def count_steps(x):
    nums = {1 : 1}

    for i in range(2, x+1):
        count = 0
        if i -3 in nums:
            count += nums[i-3]
        if i / 2 in nums and i%2==0:
            count += nums[i/2]
        nums[i] = count

    return nums[x]


if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311