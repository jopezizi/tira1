class Contest:
    def __init__(self, names, task_count):
        self.submissions = {name:{task:0 for task in range(1,task_count+1)} for name in names}
        self.max = task_count
        self.total = {name:0 for name in names}
        self.times = {name:0 for name in names}
        self.timer = 0

    def add_submission(self, name, task, score):
        if task in range(1, self.max+1):
            if self.submissions[name][task] < score:
                self.total[name] -= self.submissions[name][task]
                self.total[name] += score
                self.times[name] = self.timer
                self.submissions[name][task] = score
                self.timer += 1

    def create_scoreboard(self):
        total_scores = [(name, score) for name, score in self.total.items()]
        return sorted(total_scores, key= lambda item: (-item[1], self.times[item[0]], item[0]))

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]