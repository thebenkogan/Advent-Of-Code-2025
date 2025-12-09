from aoc import nums, read_input
from shapely import Polygon, box

lines = read_input()
ps = [tuple(nums(line)) for line in lines]
poly = Polygon(ps)

best1 = 0
best2 = 0
for i in range(len(ps)):
    for j in range(i + 1, len(ps)):
        (x1, y1), (x2, y2) = ps[i], ps[j]
        a = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        best1 = max(best1, a)

        rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if poly.contains(rect):
            best2 = max(best2, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(best1)
print(best2)
