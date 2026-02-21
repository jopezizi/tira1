class DistanceTracker:
    def __init__(self):
        self.numbers = {}
        self.distances = {}
        self.cumulative = {}
        self.i = 0

    def append(self, number):
        if number not in self.numbers:
            self.numbers[number] = 1
            self.distances[number] = 0
            self.cumulative[number] = self.i
        else:
            self.distances[number] += self.i * self.numbers[number] - self.cumulative[number]
            self.cumulative[number] += self.i
            self.numbers[number] += 1
        self.i += 1

    def sum(self, number):
        if number not in self.distances:
            return 0
        return self.distances[number]

if __name__ == "__main__":
    tracker = DistanceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    tracker.append(3)
    tracker.append(1)
    tracker.append(2)
    tracker.append(1)

    print(tracker.sum(1)) # 24
    print(tracker.sum(2)) # 5
    print(tracker.sum(3)) # 1

    tracker.append(1)
    tracker.append(2)
    tracker.append(3)

    print(tracker.sum(1)) # 42
    print(tracker.sum(2)) # 16
    print(tracker.sum(3)) # 14