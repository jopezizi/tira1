class WordFinder:
    def set_grid(self, grid):
        self.grid = []
        for row in grid:
            self.grid.append(row)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def count(self, word):
        height, width, length = self.height, self.width, len(word)

        self.directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        self.matches = set()

        for row in range(self.height): #käydään läpi rivit
            for column in range(self.width): #käydään läpi sarakkeet
                if self.grid[row][column] in (word[0],word[-1]): #katsotaan, onko käsiteltävä kirjain sanan ensimmäinen tai viimeinen
                    for dr, dc in self.directions:
                        last_r = row + (length-1) * dr  #mennään sanan pituuden verran eteenpäin ruudukossa.
                        last_c = column + (length-1) * dc
                        if 0 <= last_r < self.height and 0 <= last_c < self.width: #tarkastetaan, ettei mennä ruudukon yli vasemmalta tai oikealta
                            match = True
                            coordinates = []
                            for i in range(length): # käydään läpi koordinaatti kerrallaan, matchaavatko muutkin kirjaimet
                                current_row = row + i * dr
                                current_column = column + i * dc
                                if self.grid[current_row][current_column] != word[i]:
                                    match = False
                                    break
                                coordinates.append((current_row, current_column))
                            if match:
                                self.matches.add(tuple(sorted(coordinates))) #poistetaan kaksoisesiintymät ja lisätään koordinaatit listaan
        return len(self.matches)

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