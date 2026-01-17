import re

def find_segments(data):
    segments = []
    current = data[0]
    segment_length = 0

    for char in data:
        if char == current:
            segment_length += 1

        else:
            segments.append((segment_length, current))
            current = char
            segment_length = 1
    segments.append((segment_length, current))
    return segments







if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]