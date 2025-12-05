from aoc import read_input


lines = read_input(split_lines=False)
ranges, ids = lines.split("\n\n")
ids = [int(n) for n in ids.split("\n")]
rs = []
for r in ranges.split("\n"):
    a, b = r.split("-")
    rs.append(range(int(a), int(b) + 1))

total = 0
for i in ids:
    for r in rs:
        if i in r:
            total += 1
            break

print(total)


def merge(rs):
    new_rs = []
    rs = sorted(rs, key=lambda r: r.start)
    i = 0
    while i < len(rs):
        start, stop = rs[i].start, rs[i].stop
        while i < len(rs) - 1 and rs[i + 1].start <= stop:
            i += 1
            stop = max(stop, rs[i].stop)
        new_rs.append(range(start, stop))
        i += 1
    return new_rs


rs = merge(rs)
print(sum(len(r) for r in rs))
