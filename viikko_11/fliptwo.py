from collections import deque

def find_first(size, steps):
    q = deque([i for i in range(1,size+1)])
    
    for i in range(steps):
        rep1 = q.popleft()
        rep2 = q.popleft()
        q.append(rep2)
        q.append(rep1)

    return q.popleft()

        






if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295