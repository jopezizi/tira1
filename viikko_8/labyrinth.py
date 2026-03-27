def find_route(grid):
    start = None
    end = None

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'A':
                start = (r, c)
            elif grid[r][c] == 'B':
                end = (r, c)

    queue = [(start[0], start[1], 0)]
    visited = {start}
    count = 0

    while count < len(queue):
        r, c, d = queue[count]
        count += 1

        if (r, c) == end:
            return d

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d + 1))

    return None

if __name__ == "__main__":
    grid = ["########",
            "#.#.B..#",
            "#A#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 6

    grid = ["########",
            "#B#...A#",
            "#.#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 9

    grid = ["########",
            "####..B#",
            "#.A#.#.#",
            "#..#...#",
            "########"]
    print(find_route(grid)) # None