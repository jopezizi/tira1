class WordFinder:
    def set_grid(self, grid):
        self.grid = []
        for row in grid:
            self.grid_complete.append(row)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def count(self, word):
        height, width, length = self.h, self.width, len(word)

        
        self.directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        beginning = (r,c)




if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0  