def hash_value(string):
    table = "abcdefghijklmnopqrstuvwxyz"

    total = 0
    b = 1
    for char in string:
        total += table.find(char) * 23 ** (len(string)-b)
        b += 1
    
    return total % 2**32

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440