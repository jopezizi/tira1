def create_string(pages):
    final = ''
    pages = sorted(set(pages))
    intervals = {}

    for p in pages:
        if p-1 not in pages:
            current = p
            while current+1 in pages:
                current += 1
            
            intervals[p] = current

    for s, e in intervals.items():
        if s == e:
            final += f"{str(s)},"
        else:
            final += f"{str(s)}-{str(e)},"
    
    return final[:-1]
        

if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]