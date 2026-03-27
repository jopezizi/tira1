def count_rooms(grid):
    floors = [list(row) for row in grid]
    count = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if floors[row][column] == '.':
                count += 1
                room = [(row,column)]
                floors[row][column] = '#'

                while room:
                    r, c = room.pop()

                    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                        r2, c2 = r+dy, c+dx

                        if floors[r2][c2] == '.' and 0 <= r2 < len(grid) and 0 <= c2 < len(grid[0]):
                            floors[r2][c2] = '#'
                            room.append((r2,c2))

    return count

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2