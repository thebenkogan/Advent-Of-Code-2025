from aoc import nums, read_input

*shapes, regions = read_input(split_lines=False).split("\n\n")
for shape in shapes:
    shape = shape.splitlines()[1:]

regions = regions.split("\n")
good = 0
for r in regions:
    w, h, *reqs = nums(r)
    # assume each pattern takes 9 units of area, see if it's enough
    if sum(reqs) * 9 <= w * h:
        good += 1

print(good)
