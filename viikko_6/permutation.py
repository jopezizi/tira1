class PermutationTracker:
    def __init__(self):
        self.seen = set()
        self.dupes = False
        self.maxval = 0

    def append(self, number):
        if number in self.seen:
            self.dupes = True
        self.seen.add(number)
        if number > self.maxval:
            self.maxval = number

    def check(self):
        return False if self.dupes else len(self.seen) == self.maxval

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False
    
    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000