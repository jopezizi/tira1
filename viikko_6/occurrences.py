class OccurrenceTracker:
    def __init__(self):
        self.seen = {}
        self.unique = {}

    def append(self, number):
        if number not in self.seen:
            self.seen[number] = 1
            if 1 not in self.unique:
                self.unique[1] = 1
            else:
                self.unique[1] += 1
        else:
            occ = self.seen[number]
            if occ + 1 in self.unique:
                self.unique[occ + 1] += 1
                self.unique[occ] -= 1
            else:
                self.unique[occ + 1] = 1
                self.unique[occ] -= 1

            if self.unique[occ] == 0:
                self.unique.pop(occ)
            self.seen[number] += 1
            

    def count(self):
        return(len(self.unique))

if __name__ == "__main__":
    tracker = OccurrenceTracker()
 
    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2
 
    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1
 
    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3
    
    tracker = OccurrenceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(i % 100 + 1)
        total += tracker.count()
    print(total) # 198901