def analyze_route(grid):
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    d = 0
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'R':
                break
        else:
            continue
        break

    seen = set()
    squares = set()
    squares.add((x,y))

    while True:
        status = (x,y,d)

        if status in seen:
            return (len(squares), False)
        
        seen.add(status)
        dir_x, dir_y = directions[d]
        new_x, new_y = x+dir_x, y+dir_y

        if not (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid)):
            return(len(squares), True)
        
        if grid[new_y][new_x] == "#":
            d = (d+1) % 4
        else:
            x, y = new_x, new_y
            squares.add((x,y))
        

if __name__ == "__main__":
    grid0 = ["#.",
             "R."]
    print(analyze_route(grid0)) # (2, True)

    grid02 = ["R"]
    print(analyze_route(grid02)) # (1, True)

    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)