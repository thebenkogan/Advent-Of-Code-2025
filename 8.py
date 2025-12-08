from aoc import nums, read_input

lines = read_input()
js = [tuple(nums(line)) for line in lines]


def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


dists = []
for i in range(len(js)):
    for j in range(i + 1, len(js)):
        d = dist(js[i], js[j])
        dists.append((d, js[i], js[j]))
dists = sorted(dists)

circuits = {j: {j} for j in js}
i = 0
for _ in range(1000):
    _, j1, j2 = dists[i]
    if j1 not in circuits[j2]:
        union = circuits[j1].union(circuits[j2])
        for j in union:
            circuits[j] = union
    i += 1

cs = []
seen = set()
for c in circuits.values():
    if id(c) not in seen:
        cs.append(c)
        seen.add(id(c))

cs = sorted(cs, reverse=True, key=lambda c: len(c))
print(len(cs[0]) * len(cs[1]) * len(cs[2]))

while True:
    _, j1, j2 = dists[i]
    if j1 not in circuits[j2]:
        union = circuits[j1].union(circuits[j2])
        if len(union) == len(js):
            print(j1[0] * j2[0])
            break
        for j in union:
            circuits[j] = union
    i += 1
