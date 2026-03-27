import itertools

def find_codes(pattern):
    used = {n for n in pattern if n!= '?'}
    available = [str(c) for c in range(1,10) if c not in used]

    blank = pattern.count('?')
    if blank == 0:
        return [pattern]
    
    result = []
    for p in itertools.permutations(available, blank):
        chars = list(pattern)
        curr = 0

        for i in range(len(chars)):
            if chars[i] == '?':
                if p[curr] not in used:
                    chars[i] = p[curr]
                    curr +=1
        if '?' not in chars:
            result.append(''.join(chars))

    result.sort()
    return result

if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024