def count_splits(sequence):

    l = len(sequence)
    count_0 = sequence.count('0')
    count_1 = sequence.count('1')
    splits = 0
    balance = 0

    if count_0 != count_1:
        return splits
    
    for num in sequence[:-1]:
        if num == '0':
            balance -= 1
        else:
            balance += 1
        if balance == 0:
            splits+=1
    
    return splits


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999