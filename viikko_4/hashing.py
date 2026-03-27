def hash_value(string):
    a = 23
    m = 2**32

    val = 0
    for char in string:
        code = ord(char) - ord ('a')
        val = (val * a + code) % m

    return val
if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440