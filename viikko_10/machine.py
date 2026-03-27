from collections import deque

def min_steps(x):
    if x == 1:
        return 0
    
    q = deque([(1,0)])
    seen = {1}

    while q:
        current, steps = q.popleft()

        for next_v in [current + 3, current*2]:
            if next_v == x:
                return steps + 1
            if next_v < x and next_v not in seen:
                seen.add(next_v)
                q.append((next_v, steps + 1))
    return -1
if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    print(min_steps(42)) # -1
    print(min_steps(100)) # 7
    print(min_steps(1000)) # 13