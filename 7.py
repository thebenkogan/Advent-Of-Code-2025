from collections import deque
from functools import cache
from aoc import read_input

lines = read_input()
grid = [[c for c in line] for line in lines]

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "S":
            sx, sy = x, y

q = deque([(sx, sy)])
seen = set()
total = 0
while len(q) > 0:
    x, y = q.popleft()

    if (x, y) in seen:
        continue
    seen.add((x, y))

    if y + 1 == len(grid):
        continue

    if grid[y][x] == "^":
        total += 1
        q.append((x - 1, y))
        q.append((x + 1, y))
    else:
        q.append((x, y + 1))


print(total)


@cache
def num_timelines(x, y):
    if y == len(grid):
        return 1

    if grid[y][x] != "^":
        return num_timelines(x, y + 1)
    else:
        return num_timelines(x - 1, y) + num_timelines(x + 1, y)


print(num_timelines(sx, sy))
