import random

def count_nested(intervals):
    intervals = sorted(intervals, key=lambda item:(item[0], -item[1]))
    
    if len(intervals) < 2:
        return 0
    
    count = 0
    open_iv = []
    for iv in intervals:
        if len(open_iv) == 0:
            open_iv.append(iv)
            continue
        else:
            if (iv[0] <= open_iv[0][0] and iv[1] >= open_iv[0][1]) or open_iv[0][1] < iv[1]:
                open_iv.pop()
                open_iv.append(iv)
                continue
            if open_iv[0][0] <= iv[0] and open_iv[0][1] >= iv[1]:
                count += 1
        
    return count


if __name__ == "__main__":
    print(count_nested([(142,163),(65,123),(77,264)])) # 1
    print(count_nested([(464,555),(131,331),(388,579)])) # 1
    print(count_nested([])) # 0
    print(count_nested([(1, 2)])) # 0
    print(count_nested([(1, 2), (3, 4)])) # 0
    print(count_nested([(1, 3), (2, 4)])) # 0
    print(count_nested([(1, 4), (2, 3)])) # 1
    print(count_nested([(1, 4), (1, 3)])) # 1
    print(count_nested([(1, 4), (2, 4)])) # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0

    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 99999