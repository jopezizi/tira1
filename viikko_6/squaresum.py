class DataAnalyzer:
    def __init__(self):
        self.y2 = 0
        self.yx = 0
        self.y = 0
        self.x2 = 0
        self.x = 0
        self.n = 0

    def add_point(self, x, y):
        self.y2 += y**2
        self.yx += y*x
        self.y += y
        self.x2 += x**2
        self.x += x
        self.n += 1

    def calculate_error(self, a, b):
        return (
            self.y2 - 2*a*self.yx - 2*b*self.y +a**2 * self.x2
            + 2*a*b*self.x + self.n*b**2
        )

if __name__ == "__main__":
    analyzer = DataAnalyzer()

    analyzer.add_point(1, 1)
    analyzer.add_point(3, 2)
    analyzer.add_point(5, 3)
    print(analyzer.calculate_error(1, 0)) # 5
    print(analyzer.calculate_error(1, -1)) # 2
    print(analyzer.calculate_error(3, 2)) # 293

    analyzer.add_point(4, 2)
    print(analyzer.calculate_error(1, 0)) # 9
    print(analyzer.calculate_error(1, -1)) # 3
    print(analyzer.calculate_error(3, 2)) # 437