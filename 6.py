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

total = 0
offset = 0
for i, w in enumerate(ws):
    n = 1 if ops[i] == "*" else 0
    column = [line[offset : offset + w][::-1] for line in lines[:-1]]
    for j in range(w):
        num = int("".join([s[j] for s in column]))
        n = n * num if ops[i] == "*" else n + num
    total += n
    offset += w + 1
    i += 1

print(total)
