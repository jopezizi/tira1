class SumList:
    def __init__(self):
        self.numbers = {0:[0,0]}
        self.index = 1
        self.cumulative = 0

    def append(self, number):
        self.cumulative += number
        self.numbers[self.index] = [number, self.cumulative]
        self.index += 1

    def sum(self, a, b):
        return self.numbers[b+1][1] - self.numbers[a][1]

if __name__ == "__main__":
    numbers = SumList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    print(numbers.sum(0, 4)) # 15
    print(numbers.sum(1, 1)) # 2
    print(numbers.sum(1, 3)) # 9
    print(numbers.sum(2, 3)) # 7
    print(numbers.sum(0, 3)) # 10

    numbers.append(1)
    print(numbers.sum(0, 5)) # 16
    print(numbers.sum(5, 5)) # 1