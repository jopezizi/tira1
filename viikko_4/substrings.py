def count_substrings(string):
    seen = set()
    current = ""

    for start_i in range(len(string)):
        for end_i in range(start_i,len(string)):
            current += string[end_i]
            seen.add(current)
        current = ""
        
    return len(seen)


if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110