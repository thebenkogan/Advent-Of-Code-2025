from aoc import nums, read_input

lines = read_input()
ns = [nums(line) for line in lines[:-1]]
ops = [c for c in lines[-1].replace(" ", "")]

total = 0
for i, op in enumerate(ops):
    n = 1 if op == "*" else 0
    for row in ns:
        n = n * row[i] if op == "*" else n + row[i]
    total += n

print(total)

ws = []  # ws[i] = width of column i
spaces = 0
for c in lines[-1]:
    if c == " ":
        spaces += 1
    elif spaces > 0:
        ws.append(spaces)
        spaces = 0
ws.append(spaces + 1)

js = []  # js[i] = True if column i is left justified
offset = 0
i = 0
while offset < len(lines[0]):
    column = [line[offset : offset + ws[i]] for line in lines[:-1]]
    js.append(any(line[-1] == " " for line in column))
    offset += ws[i] + 1
    i += 1

total = 0
for i, op in enumerate(ops):
    n = 1 if op == "*" else 0
    column = [str(row[i]) for row in ns]
    if not js[i]:
        column = [s[::-1] for s in column]
    max_len = max(len(s) for s in column)
    for j in range(max_len):
        num = int("".join([s[j] if j < len(s) else "" for s in column]))
        n = n * num if op == "*" else n + num
    total += n

print(total)
