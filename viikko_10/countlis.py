def count_sequences(numbers):
    l = len(numbers)

    sub = [1] * l
    count = [1] * l
    for i in range(l):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if sub[j] + 1 > sub[i]:
                    sub[i] = sub[j] + 1
                    count[i] = count[j]
                elif sub[j] +1 == sub[i]:
                    count[i] += count[j]
    
    longest = max(sub)
    total = 0
    for i in range(l):
        if sub[i] == longest:
            total += count[i]
    
    return total

if __name__ == "__main__":
    print(count_sequences([1, 2, 3])) # 1
    print(count_sequences([3, 2, 1])) # 3
    print(count_sequences([1, 1, 1, 1, 1])) # 5

    print(count_sequences([1, 8, 2, 7, 3, 6])) # 1
    print(count_sequences([1, 1, 2, 2, 3, 3])) # 8
    print(count_sequences([4, 1, 5, 6, 3, 4, 3, 8])) # 3