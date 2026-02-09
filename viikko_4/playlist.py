def count_parts(songs):
    count = 0
    left = 0
    seen = set()
    
    for right in range(len(songs)):
        while songs[right] in seen:
            seen.remove(songs[left])
            left += 1
        seen.add(songs[right])
        count += right - left + 1
    
    return count



if __name__ == "__main__":
    print(count_parts([1, 4,4 ])) # 4
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000