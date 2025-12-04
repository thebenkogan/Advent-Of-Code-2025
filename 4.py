from aoc import DIAG_DIRS, read_input


def remove(grid):
    new_grid = [[c for c in line] for line in grid]
    total = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != "@":
                continue

            rolls = 0
            for dx, dy in DIAG_DIRS:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                    continue
                if grid[ny][nx] == "@":
                    rolls += 1

            if rolls < 4:
                new_grid[y][x] = "x"
                total += 1

    return new_grid, total


lines = read_input()
grid = [[c for c in line] for line in lines]
grid, total = remove(grid)
print(total)

while True:
    grid, t = remove(grid)
    total += t
    if t == 0:
        break

print(total)
