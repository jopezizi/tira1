


def count_strings(n):
    res = [1] * 26

    for i in range(n-1):
        new = [0] * 26
        for j in range(26):
            if j > 0:
                new[j] += res[j-1]
            if j < 25:
                new[j] += res[j+1]
        
        res = new

    return sum(res)



if __name__ == "__main__":
    print(count_strings(1)) # 26
    print(count_strings(2)) # 50
    print(count_strings(3)) # 98
    print(count_strings(4)) # 192

    print(count_strings(42)) # 36766943673096
    print(count_strings(100)) # 7073450400109633000218032957656