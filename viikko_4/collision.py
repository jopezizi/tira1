def hash_value(string):
    table = "abcdefghijklmnopqrstuvwxyz"
 
    total = 0
    b = 1
    for char in string:
        total += table.find(char) * 23 ** (len(string)-b)
        b += 1
    
    return total % 2 ** 32
 

def find_other(string):
    table = "abcdefghijklmnopqrstuvwxyz"
    val = hash_value(string)
    chars = []
    chars.append(table[-1])


    return "".join(reversed(chars))
    

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682