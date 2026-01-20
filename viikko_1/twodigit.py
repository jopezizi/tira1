
def count_numbers(a, b):
    counter = 0
    numbers = [2, 5]
    i = 0
    while i < len(numbers):
        current = numbers[i]
        i+=1

        if current >= a:
            counter += 1
        
        next_1 = current * 10 + 2
        next_2 = current * 10 + 5

        if next_1 <= b:
            numbers.append(next_1)
        if next_2 <= b:
            numbers.append(next_2)
    return counter



if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 51