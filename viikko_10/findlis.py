from collections import deque

def find_sequence(numbers):
    l = len(numbers)

    sub = [1] * l
    paths = [-1] * l

    for i in range(l):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if sub[j] + 1 > sub[i]:
                    sub[i] = sub[j] + 1
                    paths[i] = j
    
    longest = max(sub)
    ind = sub.index(longest)

    sublist = []
    while ind >= 0:
        sublist.append(numbers[ind])
        ind = paths[ind]
    
    return sublist[::-1]



if __name__ == "__main__":
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8]
    print(find_sequence([8,6,1,1,9,4,7]))