from collections import deque

class FlipList:
    def __init__(self):
        self.left_to_right = True
        self.q = deque() 

    def __repr__(self):
        result = list(self.q)
        if not self.left_to_right:
            result.reverse()
        return str(result)

    def add_first(self, x):
        if self.left_to_right:
            self.q.appendleft(x)
        else:
            self.q.append(x)

    def add_last(self, x):
        if self.left_to_right:
            self.q.append(x)
        else:
            self.q.appendleft(x)

    def flip(self):
        self.left_to_right = not self.left_to_right

if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers) # [1, 2, 3]

    numbers.add_first(4)
    print(numbers) # [4, 1, 2, 3]

    numbers.flip()
    print(numbers) # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers) # [3, 2, 1, 4, 5]